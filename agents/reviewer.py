from ai.client import get_llm_response
from ai.prompts import REVIEW_PROMPT
from ai.schemas import CodeReviewOutput

def analyze_code(language: str, code: str) -> dict:
    """Orchestrates the Bug, Security, Performance, and Best Practice analysis."""
    prompt = REVIEW_PROMPT.format(language=language, code=code)
    try:
        result = get_llm_response(prompt, CodeReviewOutput)
        return result
    except Exception as e:
        raise Exception(f"AI Review Failed: {str(e)}")