import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    div[data-testid="stMetric"] { background:#161B22; border:1px solid #30363D; border-radius:10px; padding:15px; }
    .severity-badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:12px; font-weight:600; margin-right:6px; }
    .sev-critical{background:#F85149;color:#fff;} .sev-high{background:#DB6D28;color:#fff;}
    .sev-medium{background:#D29922;color:#000;} .sev-low{background:#388BFD;color:#fff;} .sev-info{background:#6E7681;color:#fff;}
    .category-badge { display:inline-block; padding:3px 10px; border-radius:12px; font-size:12px; background:#21262D; border:1px solid #30363D; }
    .stExpander { border:1px solid #30363D !important; border-radius:8px !important; margin-bottom:8px; }
    .stButton>button { border-radius:8px; font-weight:600; }
    </style>
    """, unsafe_allow_html=True)
