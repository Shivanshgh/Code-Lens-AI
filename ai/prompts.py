REVIEW_PROMPT = """
You are an expert AI software engineer, security researcher, and performance analyzer.
Review the following {language} code.

You must analyze the code through these strict lenses:
1. Bug Detection (syntax, logic errors, incorrect conditions)
2. Security (hardcoded secrets, SQLi, command injection, XSS, insecure functions)
3. Performance (unnecessary loops, algorithmic inefficiency)
4. Best Practices (naming, structure, duplicated code, maintainability)

Code to analyze:
{code}
"""

FIX_PROMPT = """
You are an expert AI software engineer.
Given the following {language} code and the list of issues found in it, rewrite the code to fix all issues.

Original code:
{code}

Issues to fix:
{issues}

Return the complete corrected code and a list of the changes you made.
"""
