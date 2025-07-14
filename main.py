from fastapi import FastAPI
from models import PromptRequest, PromptResponse
from firewall import analyze_prompt
from dotenv import load_dotenv


load_dotenv()

api = FastAPI(
    title="PromptShield API",
    description="An intelligent firewall for LLM prompts using rules and AI moderation.",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@api.post('/check', response_model=PromptResponse)
def check_prompt(payload:PromptRequest):
    result =  analyze_prompt(payload.prompt)
    return result