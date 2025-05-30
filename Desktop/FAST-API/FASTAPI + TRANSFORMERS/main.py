from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

sentiment_analyzer = pipeline("sentiment-analysis")

app = FastAPI()

class TextInput(BaseModel):
    text: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_home():
    return FileResponse("static/index.html")

@app.post("/analyze")
async def analyze_statement(data: TextInput):
    result = sentiment_analyzer(data.text)
    return {"result": result}
