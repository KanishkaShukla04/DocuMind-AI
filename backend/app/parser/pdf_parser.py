import pdfplumber

from app.parser.ocr import extract_text_from_image
from app.parser.page_images import convert_pdf_to_images


def extract_text_from_pdf(pdf_path: str, document_id: str):

    pages = []

    images = convert_pdf_to_images(
        pdf_path,
        document_id
    )


    with pdfplumber.open(pdf_path) as pdf:

        for page_num, page in enumerate(pdf.pages):

            text = page.extract_text() or ""


            if not text.strip():

                text = extract_text_from_image(
                    images[page_num]
                )


            pages.append({
                "page": page_num + 1,
                "text": text
            })


    return pages