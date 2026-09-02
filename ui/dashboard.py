import streamlit as st
import pandas as pd
from database.db import get_dashboard_stats

def render_dashboard():
    st.header("📊 Dashboard")
    stats = get_dashboard_stats()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Reviews Run", stats["total_reviews"])
    col2.metric("Average Quality Score", f"{stats['avg_score']}/100")
    col3.metric("Total Issues Detected", stats["total_issues"])
    
    st.subheader("Recent Reviews")
    if stats["recent"]:
        df = pd.DataFrame(stats["recent"], columns=["Date", "Language", "Score"])
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No reviews yet. Head over to the Code Review tab to get started!")