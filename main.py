from fastapi import FastAPI
from models import PromptRequest, PromptResponse
from firewall import analyze_prompt
from dotenv import load_dotenv


load_dotenv()

api = FastAPI()

@api.post('/check', response_model=PromptResponse)
def check_prompt(payload:PromptRequest):
    result =  analyze_prompt(payload.prompt)
    return result