from app.classifier.gemini_classifier import classify_document

sample_text = """
Kanishka Shukla

AI Engineer and Full Stack Developer

Skills:
Python
JavaScript
TypeScript
Next.js
React
LangChain
Gemini
Machine Learning
"""

result = classify_document(sample_text)

print(result)