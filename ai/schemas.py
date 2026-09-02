from pydantic import BaseModel, Field
from typing import List, Optional

class Issue(BaseModel):
    severity: str = Field(description="Critical, High, Medium, Low, Info")
    category: str = Field(description="Bug, Security, Performance, Maintainability, Best Practice")
    title: str = Field(description="Short, clear title of the issue")
    line: Optional[int] = Field(description="Line number if applicable, else null")
    description: str = Field(description="Detailed explanation of the issue")
    impact: str = Field(description="Why this matters (e.g., potential crash, data leak)")
    suggestion: str = Field(description="How to fix it")

class CodeReviewOutput(BaseModel):
    score: int = Field(description="Code quality score 0-100")
    summary: str = Field(description="Short overall summary of the review")
    issues: List[Issue] = Field(description="List of detected issues")

class CodeFixOutput(BaseModel):
    fixed_code: str = Field(description="The complete updated source code with fixes applied")
    changes: List[str] = Field(description="Bullet points explaining what was changed and why")