import ast

def verify_code(language: str, original_code: str, generated_code: str) -> tuple[bool, str]:
    """
    Verification Agent layer. 
    Never executes arbitrary code. Uses static parsing to verify generated code validity.
    """
    if language.lower() == "python":
        try:
            # Parse the AST to verify syntactical correctness
            ast.parse(generated_code)
            return True, "Python AST verification passed. Code is syntactically valid."
        except SyntaxError as e:
            return False, f"Verification Failed! The AI generated invalid Python syntax on line {e.lineno}: {e.msg}"
    
    # For other languages (C, C++, JS), we bypass strict AST for the MVP and assume valid, 
    # but we can add basic heuristic checks here (e.g., checking for empty output).
    if not generated_code.strip():
        return False, "Verification Failed: AI returned empty code."
        
    return True, f"{language} verification passed (Heuristic)."