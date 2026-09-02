from ai.client import get_llm_response
from ai.prompts import FIX_PROMPT
from ai.schemas import CodeFixOutput
import json

def generate_fix(language: str, code: str, issues: list) -> dict:
    """Generates the corrected code based on the identified issues."""
    issues_text = json.dumps(issues, indent=2)
    prompt = FIX_PROMPT.format(language=language, code=code, issues=issues_text)
    try:
        result = get_llm_response(prompt, CodeFixOutput)
        return result
    except Exception as e:
        raise Exception(f"AI Fix Generation Failed: {str(e)}")