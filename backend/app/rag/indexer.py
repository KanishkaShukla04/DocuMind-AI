from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.vector_store import collection


def index_document(metadata):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    for page in metadata["pages"]:

        chunks = splitter.split_text(
            page["text"]
        )

        for idx, chunk in enumerate(chunks):

            collection.add(
                documents=[chunk],
                ids=[
                    f"{metadata['document_id']}_{page['page']}_{idx}"
                ],
                metadatas=[
                    {
                        "document_name": metadata["filename"],
                        "page": page["page"],
                        "image_path": page["image_path"]
                    }
                ]
            )