from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(
    title="DocuMind AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(
    "/page_images",
    StaticFiles(directory="page_images"),
    name="page_images"
)

app.include_router(upload_router)
app.include_router(chat_router)
@app.get("/")
def home():
    return {
        "message": "DocuMind AI Running"
    }