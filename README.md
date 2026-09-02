# 🔍 CodeLens AI

**AI-powered code review, debugging, and fixing assistant.**

CodeLens AI is a production-style MVP built for detecting bugs, security vulnerabilities, performance bottlenecks, and bad practices across multiple programming languages. It leverages a modern agentic workflow by combining Google's Gemini LLM for analysis, Python AST for syntax verification, and Streamlit for a fast, responsive UI.

## 🚀 Features
- **Multi-language Support:** Python, JavaScript, C, and C++.
- **Agentic Pipeline:** Separates bug detection, security, performance, and best practices logically via structured LLM instructions.
- **Verification Layer:** For Python, automatically checks if the AI-generated code is syntactically valid using the `ast` module before displaying it to the user.
- **Structured AI Output:** Utilizes Pydantic schemas to strictly format Gemini outputs into robust, usable JSON.
- **Side-by-Side Diff:** Easily compare original code with the suggested AI fix.
- **History Tracker:** Automatically saves reviews locally to SQLite.

## 🛠️ Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/codelens-ai.git
   cd codelens-ai