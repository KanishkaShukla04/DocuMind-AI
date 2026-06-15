import os
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from app.rag.retriever import retrieve


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def answer_question(question, history=None):

    if history is None:
        history = []

    results = retrieve(question)

    # No relevant chunks found
    if not results["documents"] or not results["documents"][0]:
        return {
            "answer": "I could not find relevant information.",
            "citations": []
        }

    # Use only top retrieved chunks
    context = "\n\n".join(
        results["documents"][0][:5]
    )

    chat_history = "\n".join(
        [
            f"{item['role']}: {item['content']}"
            for item in history
        ]
    )

    prompt = f"""
You are a document assistant.

Previous conversation:
{chat_history}

Answer ONLY using the provided context.

If the answer is not explicitly present in the context,
respond exactly:

I could not find relevant information.

Rules:
- Do not use outside knowledge.
- Do not guess.
- Do not infer missing facts.
- Only use information found in the context.
- Return the answer in Markdown format.
- Use headings, bullet points, and short paragraphs when appropriate.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    answer = response.content

    citations = []
    seen = set()

    for meta in results["metadatas"][0][:5]:

        key = (
            meta["document_name"],
            meta["page"]
        )

        if key not in seen:
            seen.add(key)

            citations.append({
                "document": meta["document_name"],
                "page": meta["page"],
                "image_path": meta["image_path"]
            })

    return {
        "answer": answer,
        "citations": citations
    }