from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List, Dict, Any

from app.rag.chat_engine import answer_question


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    question: str
    history: List[Dict[str, Any]] = Field(
        default_factory=list
    )


@router.post("/")
def chat(request: ChatRequest):

    return answer_question(
        request.question,
        request.history
    )