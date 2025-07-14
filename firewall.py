from models import PromptResponse
from rules import rule_nsfw, rule_jailbreak
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

RULES = [rule_nsfw, rule_jailbreak]

def analyze_prompt(prompt: str) -> PromptResponse:
    violations = []
    for rule in RULES:
        reason = rule(prompt)
        if reason:
            violations.append(reason)

    try:
        response = openai.Moderation.create(input=prompt)
        flagged = response["results"][0]["flagged"]
        categories = response["results"][0]["categories"]

        if flagged:
            reasons = [cat.replace("_", " ").capitalize() for cat, is_flagged in categories.items() if is_flagged]
            violations.append(f"Flagged by OpenAI: {', '.join(reasons)}")

    except Exception as e:
        violations.append(f"Moderation API error: {str(e)}")

    status = 'blocked' if violations else 'safe'
    return PromptResponse(status=status, reasons=violations)
