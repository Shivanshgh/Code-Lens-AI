import google.generativeai as genai
import json
from ai.schemas import CodeReviewOutput, CodeFixOutput

def get_llm_response(prompt: str, schema: type) -> dict:
    """Generic wrapper for Gemini API calling with JSON structure enforcement."""
    # Using gemini-1.5-flash as it is fast, highly capable, and supports JSON modes well.
    model = genai.GenerativeModel('gemini-flash-lite-latest', generation_config={
    "response_mime_type": "application/json",
    "max_output_tokens": 2048,
    })
    
    # We instruct the model on the schema structure manually within the system config
    schema_instructions = f"\n\nOUTPUT FORMAT: You MUST return a valid JSON object matching this JSON Schema:\n{schema.schema_json()}"
    
    response = model.generate_content(prompt + schema_instructions)
    return json.loads(response.text)
