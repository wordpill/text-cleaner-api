import re
from math import ceil

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Text Cleaner Micro API")

WORDS_PER_MINUTE = 200  # average adult reading speed


class TextInput(BaseModel):
    text: str


@app.get("/")
def health():
    return {"success": True, "message": "Text Cleaner API is running. POST to /clean"}


@app.post("/clean")
def clean_text(payload: TextInput):
    # Collapse all whitespace (spaces, tabs, line breaks) into single spaces
    cleaned = re.sub(r"\s+", " ", payload.text).strip()

    word_count = len(cleaned.split()) if cleaned else 0
    read_time_minutes = max(1, ceil(word_count / WORDS_PER_MINUTE)) if word_count else 0

    return {
        "success": True,
        "cleaned_text": cleaned,
        "word_count": word_count,
        "read_time_minutes": read_time_minutes,
    }
