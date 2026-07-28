from datetime import datetime
import streamlit as st

def render_footer() -> None:
    """Render the page footer with branding and copyright."""
    year = datetime.now().year
    st.markdown(
        f"""
        <div class="footer">
            <div class="footer-left">
                <span class="footer-brand">🤖 DocQuery AI</span>
                <span class="footer-divider">•</span>
                <span>Powered by Gemma 4</span>
                <span class="footer-divider">•</span>
                <span>ChromaDB</span>
                <span class="footer-divider">•</span>
                <span>Sentence Transformers</span>
            </div>
            <div class="footer-right">© {year}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )