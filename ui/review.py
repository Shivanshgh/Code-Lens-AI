import streamlit as st
from agents.reviewer import analyze_code
from agents.fix_generator import generate_fix
from agents.verifier import verify_code
from database.db import save_review
from samples.code_samples import GET_SAMPLE_CODE

def render_review_page():
    from ui.styles import hero_banner
    hero_banner("🔬 Code Review Agent", "Paste your code below and let the AI agents find what's broken.")
    
    # State management
    if "code_input" not in st.session_state:
        st.session_state.code_input = ""
    if "review_result" not in st.session_state:
        st.session_state.review_result = None
    if "fix_result" not in st.session_state:
        st.session_state.fix_result = None

    col1, col2 = st.columns([1, 3])
    with col1:
        language = st.selectbox("Language", ["Python", "JavaScript", "C", "C++"])
        if st.button("Load Vulnerable Sample"):
            st.session_state.code_input = GET_SAMPLE_CODE(language)
            st.session_state.review_result = None
            st.session_state.fix_result = None
            st.rerun()
            
    with col2:
        code = st.text_area("Paste your code here:", value=st.session_state.code_input, height=300)
        st.session_state.code_input = code
        
    if st.button("🚀 Analyze Code", type="primary"):
        if not code.strip():
            st.warning("Please enter some code to analyze.")
            return
            
        if len(code) > 20000:
            st.error("Code exceeds maximum length (20,000 characters) for the MVP.")
            return

        with st.spinner("AI Agents analyzing code (Bugs, Security, Performance)..."):
            try:
                result = analyze_code(language, code)
                st.session_state.review_result = result
                st.session_state.fix_result = None # Clear old fixes
                
                # Save to History
                save_review(language, code, result["score"], len(result["issues"]), result["summary"], result["issues"])
                
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                return

    # Display Review Results
    if st.session_state.review_result:
        res = st.session_state.review_result
        st.divider()
        
        c1, c2 = st.columns([1, 4])
        with c1:
            score = res['score']
            ring_color = "#3FB950" if score >= 80 else "#D29922" if score >= 50 else "#F85149"
            st.markdown(f"""
            <div style="text-align:center;">
                <svg width="120" height="120">
                    <circle cx="60" cy="60" r="50" stroke="#30363D" stroke-width="10" fill="none"/>
                    <circle cx="60" cy="60" r="50" stroke="{ring_color}" stroke-width="10" fill="none"
                        stroke-dasharray="{score*3.14}, 314" stroke-linecap="round" transform="rotate(-90 60 60)"/>
                    <text x="60" y="68" text-anchor="middle" font-size="26" font-weight="800" fill="white">{score}</text>
                </svg>
                <p style="color:#8B949E; margin-top:-8px;">/ 100</p>
            </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.write("**Summary:**")
            st.write(res['summary'])
            
        st.subheader(f"Detected Issues ({len(res['issues'])})")
        
        SEV_CLASS = {"Critical":"sev-critical","High":"sev-high","Medium":"sev-medium","Low":"sev-low","Info":"sev-info"}
        for issue in res['issues']:
            color = "🔴" if issue['severity'] in ["Critical", "High"] else "🟡" if issue['severity'] == "Medium" else "🔵"
            with st.expander(f"{color} [{issue['category']}] {issue['title']} (Line {issue['line'] or 'N/A'})"):
                st.markdown(f'<span class="severity-badge {SEV_CLASS.get(issue["severity"],"sev-info")}">{issue["severity"]}</span> <span class="category-badge">{issue["category"]}</span>', unsafe_allow_html=True)
                st.markdown(f"**Severity:** {issue['severity']}")
                st.markdown(f"**Description:** {issue['description']}")
                st.markdown(f"**Impact:** {issue['impact']}")
                st.markdown(f"**Suggested Fix:** {issue['suggestion']}")
                
        # Fix Generation Trigger
        if len(res['issues']) > 0:
            st.divider()
            if st.button("✨ Auto-Fix All Issues", type="primary"):
                with st.spinner("AI Fix Generator writing corrected code..."):
                    try:
                        fix = generate_fix(language, code, res['issues'])
                        
                        # Verification Layer
                        is_valid, msg = verify_code(language, code, fix['fixed_code'])
                        if not is_valid:
                            st.error(f"**Verification Failed:** The generated fix contained errors and was blocked.\n\n{msg}")
                        else:
                            st.success(f"Verification Passed: {msg}")
                            st.session_state.fix_result = fix
                    except Exception as e:
                        st.error(f"Fix generation failed: {str(e)}")

    # Display Fix Results
    if st.session_state.fix_result:
        fix = st.session_state.fix_result
        st.subheader("🛠️ Corrected Code")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### Original")
            st.code(st.session_state.code_input, language=language.lower())
        with c2:
            st.markdown("### Suggested Fix")
            st.code(fix['fixed_code'], language=language.lower())
            
        st.markdown("### Explanation of Changes")
        for change in fix['changes']:
            st.markdown(f"- {change}")
            
        st.download_button(
            label="💾 Download Corrected Code",
            data=fix['fixed_code'],
            file_name=f"fixed_code.{'py' if language=='Python' else 'js' if language=='JavaScript' else 'c'}",
            mime="text/plain"
        )
