import streamlit as st
import pandas as pd
from database.db import get_all_reviews

def render_history_page():
    st.header("📚 Review History")
    rows = get_all_reviews()
    
    if not rows:
        st.info("No reviews found.")
        return
        
    df = pd.DataFrame(rows, columns=["Date", "Language", "Score", "Issues Count", "Summary"])
    st.dataframe(df, use_container_width=True, hide_index=True)