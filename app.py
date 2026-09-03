import streamlit as st
import os
from dotenv import load_dotenv

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="CodeLens AI - Code Review Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
    
)

from config.settings import check_api_key
from ui.styles import inject_css
from database.db import init_db
from ui.dashboard import render_dashboard
from ui.review import render_review_page
from ui.history import render_history_page

def main():
    load_dotenv()
    init_db()
    inject_css()
    
    st.sidebar.title("🔍 CodeLens AI")
    st.sidebar.caption("Find bugs. Understand them. Fix them.")
    
    if not check_api_key():
        st.error("⚠️ GEMINI_API_KEY is not set. Please add it to your .env file or Streamlit secrets.")
        st.stop()

    page = st.sidebar.radio("Navigation", ["Dashboard", "Code Review", "History", "About"])
    
    st.sidebar.divider()
    st.sidebar.info("CodeLens AI is a static analysis and AI-powered code assistant. Do not use for highly sensitive proprietary code.")
    
    if page == "Dashboard":
        render_dashboard()
    elif page == "Code Review":
        render_review_page()
    elif page == "History":
        render_history_page()
    elif page == "About":
        
        st.header("⚙️ How CodeLens AI Works")
        st.markdown("""
**Pipeline:** User Code → Static Analysis (AST) → AI Review (Gemini) → Structured Issues (Pydantic) → Fix Generation → Verification → Result

**Agents:** Bug Detector · Security Analyzer · Performance Analyzer · Best Practice Analyzer · Fix Generator · Verification Agent

**Stack:** Streamlit · Google Gemini · Pydantic · SQLite · Python AST
        """)

if __name__ == "__main__":
    main()
