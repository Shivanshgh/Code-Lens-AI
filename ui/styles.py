import streamlit as st

def inject_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #0E1117 0%, #12151C 100%);
    }

    .hero-banner {
        background: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #EC4899 100%);
        padding: 32px 40px;
        border-radius: 16px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px rgba(99,102,241,0.25);
    }
    .hero-banner h1 { color: white; margin: 0; font-size: 2.2rem; font-weight: 800; }
    .hero-banner p { color: rgba(255,255,255,0.9); margin: 6px 0 0 0; font-size: 1.05rem; }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #161B22, #1C222B);
        border: 1px solid #30363D;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: transform 0.2s ease;
    }
    div[data-testid="stMetric"]:hover { transform: translateY(-3px); border-color: #6366F1; }

    .severity-badge {
        display: inline-block; padding: 4px 12px; border-radius: 20px;
        font-size: 12px; font-weight: 700; margin-right: 6px;
        text-transform: uppercase; letter-spacing: 0.5px;
    }
    .sev-critical{background:linear-gradient(135deg,#F85149,#DA3633);color:#fff;}
    .sev-high{background:linear-gradient(135deg,#DB6D28,#BD561D);color:#fff;}
    .sev-medium{background:linear-gradient(135deg,#D29922,#9E7115);color:#000;}
    .sev-low{background:linear-gradient(135deg,#388BFD,#2568C4);color:#fff;}
    .sev-info{background:linear-gradient(135deg,#6E7681,#545D68);color:#fff;}

    .category-badge {
        display: inline-block; padding: 4px 12px; border-radius: 20px;
        font-size: 12px; font-weight: 600; background: #21262D;
        border: 1px solid #30363D; color: #C9D1D9;
    }

    .stExpander {
        border: 1px solid #30363D !important;
        border-radius: 12px !important;
        margin-bottom: 10px;
        background: #161B22 !important;
    }
    .stExpander:hover { border-color: #6366F1 !important; }

    .stButton>button {
        border-radius: 10px; font-weight: 700; border: none;
        background: linear-gradient(135deg, #6366F1, #8B5CF6);
        color: white; transition: all 0.2s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 4px 16px rgba(99,102,241,0.4);
        transform: translateY(-1px);
    }

    h1, h2, h3 { font-weight: 800 !important; }
    section[data-testid="stSidebar"] { background: #0D1117; border-right: 1px solid #21262D; }

    .stTextArea textarea { border-radius: 10px !important; border: 1px solid #30363D !important; }

    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-thumb { background: #30363D; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

def hero_banner(title, subtitle):
    st.markdown(f"""
    <div class="hero-banner">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
