import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

def check_api_key() -> bool:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False