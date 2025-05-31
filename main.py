from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

app=FastAPI()


class TextInput(BaseModel):
    text: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_home():
    return FileResponse("static/index.html")

@app.post("/summarize")
async def summ_text(data: TextInput):
    text = "summarize: " + data.text.strip().replace('\n', '')
    result = summarizer(text, min_length=10, max_length=50)
    return {"summary": result[0]['summary_text']}


