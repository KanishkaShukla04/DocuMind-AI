from app.rag.retriever import retrieve

results = retrieve(
    "What skills are mentioned?"
)

print(results)