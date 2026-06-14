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


def answer_question(question, history=[]):

    results = retrieve(question)

    context = "\n\n".join(
        results["documents"][0]
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

Answer the user's question using the context.

Return the answer in well-formatted Markdown.

Use:
- Headings
- Bullet points
- Short paragraphs

Do not return plain text.

If the answer is not present,
respond:

I could not find relevant information.

Context:
{context}

Question:
{question}
"""


    response = llm.invoke(prompt)

    answer = response.content


    citations = []

    seen = set()


    for meta in results["metadatas"][0]:

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