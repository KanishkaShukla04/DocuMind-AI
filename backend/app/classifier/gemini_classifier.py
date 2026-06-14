import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def classify_document(text: str):

    prompt = f"""
Return ONLY valid JSON.

{{
  "document_type": "",
  "topic": "",
  "sensitivity_level": "",
  "contains_tables": false,
  "contains_images": false,
  "contains_handwriting": false,
  "summary": ""
}}

Document:

{text[:5000]}
"""

    response = llm.invoke(prompt)

    cleaned = response.content.strip()
    cleaned = cleaned.replace("```json", "")
    cleaned = cleaned.replace("```", "")
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)

    except Exception as e:
        return {
            "error": str(e),
            "raw": cleaned
        }