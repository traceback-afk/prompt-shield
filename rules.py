def rule_jailbreak(prompt: str) -> str | None:
    jailbreak_keywords = ['ignore previous instructions', 'jailbreak', 'you are not chatgpt']
    jailbreak_violation_message = 'Possible jailbreak attempt'
    if any(x in prompt.lower() for x in jailbreak_keywords):
        return jailbreak_violation_message
    return None


def rule_nsfw(prompt: str) -> str | None:
    nsfw_content_message = 'Inappropriate or harmful content'
    nsfw_content_keywords = ['nude', 'racist', 'kill', 'nsfw', 'naked']
    if any(x in prompt.lower() for x in nsfw_content_keywords):
        return nsfw_content_message
    return None