import streamlit as st

def render_header() -> None:
    """Render the top navigation / branding header."""
    st.markdown(
        """
        <div class="header">
            <div class="header-left">
                <div class="logo">🤖</div>
                <div>
                    <div class="title">DocQuery AI</div>
                    <div class="subtitle">Intelligent Document Assistant</div>
                </div>
            </div>
            <div class="header-right">
                <div class="status">
                    <span class="status-dot"></span>
                    Ready
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )