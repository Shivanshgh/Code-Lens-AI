import streamlit as st
import os
from dotenv import load_dotenv

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="CodeLens AI - Code Review Agent",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
    st.sidebar.markdown("---")
    st.sidebar.caption("Built with Gemini · AST · Streamlit")
    st.sidebar.caption("v1.0 — Internship MVP")
)

from config.settings import check_api_key
from database.db import init_db
from ui.dashboard import render_dashboard
from ui.review import render_review_page
from ui.history import render_history_page

def main():
    load_dotenv()
    init_db()
    
    st.sidebar.title("🔍 CodeLens AI")
    st.sidebar.caption("Find bugs. Understand them. Fix them.")
    
    if not check_api_key():
        st.error("⚠️ GEMINI_API_KEY is not set. Please add it to your .env file or Streamlit secrets.")
        st.stop()

    page = st.sidebar.radio("Navigation", ["Dashboard", "Code Review", "History"])
    
    st.sidebar.divider()
    st.sidebar.info("CodeLens AI is a static analysis and AI-powered code assistant. Do not use for highly sensitive proprietary code.")
    
    if page == "Dashboard":
        render_dashboard()
    elif page == "Code Review":
        render_review_page()
    elif page == "History":
        render_history_page()

if __name__ == "__main__":
    main()
