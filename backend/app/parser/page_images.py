from pdf2image import convert_from_path
from pathlib import Path

IMAGE_DIR = Path("page_images")
IMAGE_DIR.mkdir(exist_ok=True)

def convert_pdf_to_images(pdf_path: str, document_id: str):

    images = convert_from_path(pdf_path)

    saved_paths = []

    doc_folder = IMAGE_DIR / document_id
    doc_folder.mkdir(exist_ok=True)

    for idx, image in enumerate(images):

        page_path = doc_folder / f"page_{idx+1}.png"

        image.save(page_path)

        saved_paths.append(str(page_path))

    return saved_paths