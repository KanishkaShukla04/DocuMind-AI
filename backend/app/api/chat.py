from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.chat_engine import answer_question


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    question: str
    history: list = []


@router.post("/")
def chat(request: ChatRequest):

    return answer_question(
        request.question,
        request.history
    )