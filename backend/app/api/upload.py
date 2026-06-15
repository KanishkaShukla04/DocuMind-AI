from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import uuid

from app.parser.pdf_parser import extract_text_from_pdf
from app.parser.page_images import convert_pdf_to_images
from app.parser.metadata import save_metadata
from app.classifier.gemini_classifier import classify_document
from app.rag.indexer import index_document


router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/")
async def upload_documents(
    files: list[UploadFile] = File(...)
):

    results = []

    for file in files:

        extension = Path(file.filename).suffix

        filename = f"{uuid.uuid4()}{extension}"

        filepath = UPLOAD_DIR / filename


        with open(filepath, "wb") as f:
            content = await file.read()
            f.write(content)


        document_id = filename.split(".")[0]


        pages = extract_text_from_pdf(
            str(filepath),
            document_id
        )
        full_text = "\n".join(
    page["text"]
    for page in pages)


        try:
           classification = classify_document(full_text)
        except Exception as e:
            print("Classification Error:", str(e))

    classification = {
        "document_type": "unknown",
        "topic": "unknown",
        "sensitivity": "unknown"}


    images = convert_pdf_to_images(
            str(filepath),
            document_id
        )


    metadata = {
      "document_id": document_id,
      "filename": file.filename,
      "total_pages": len(pages),
      "classification": classification,
      "pages": []}


    for i, page in enumerate(pages):

            metadata["pages"].append({
                "page": page["page"],
                "text": page["text"],
                "image_path": images[i]
            })


    save_metadata(
            document_id,
            metadata
        )


    index_document(metadata)


    results.append({
    "filename": file.filename,
    "status": "indexed",
    "steps": [
        "uploaded",
        "parsing",
        "classifying",
        "indexed"
    ],
    "document_id": document_id,
    "pages": len(pages)
})


    return {
    "documents": results
}