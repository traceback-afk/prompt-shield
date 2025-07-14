from pydantic import BaseModel
from typing import List


class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    status: str
    reasons: List[str]