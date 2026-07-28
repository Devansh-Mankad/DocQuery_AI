import streamlit as st

def render_sidebar() -> None:
    """Render the left sidebar with navigation, stats, and generation controls."""
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-header">
                <div class="sidebar-logo">📚</div>
                <div>
                    <div class="sidebar-title">DocQuery AI</div>
                    <div class="sidebar-version">Version 1.0</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

        if st.button("➕  New Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.markdown(
            "<div class='sidebar-section'>Conversation</div>",
            unsafe_allow_html=True,
        )

        user_questions = [
            msg["content"]
            for msg in st.session_state.get("messages", [])
            if msg["role"] == "user"
        ]

        if not user_questions:
            st.markdown(
                "<div class='sidebar-empty'>No conversation yet</div>",
                unsafe_allow_html=True,
            )
        else:
            for question in reversed(user_questions[-8:]):
                preview = question if len(question) <= 38 else question[:38] + "…"
                st.markdown(
                    f"<div class='history-card'>💬 {preview}</div>",
                    unsafe_allow_html=True,
                )

        st.markdown(
            "<div class='sidebar-section'>Knowledge Base</div>",
            unsafe_allow_html=True,
        )

        for label in ("📄 Documents", "🧩 Chunks", "🔎 Embeddings", "🗂 ChromaDB"):
            st.markdown(
                f"<div class='sidebar-card'>{label}</div>",
                unsafe_allow_html=True,
            )

        st.markdown(
            "<div class='sidebar-section'>Statistics</div>",
            unsafe_allow_html=True,
        )

        messages = st.session_state.get("messages", [])
        user_count      = sum(1 for m in messages if m["role"] == "user")
        assistant_count = sum(1 for m in messages if m["role"] == "assistant")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Questions", user_count)
        with col2:
            st.metric("Answers", assistant_count)

        st.markdown(
            "<div class='sidebar-section'>System</div>",
            unsafe_allow_html=True,
        )
        st.success("🟢 Gemma 4 Loaded")
        st.success("🟢 ChromaDB Connected")
        st.success("🟢 Embedding Ready")

        st.markdown(
            "<div class='sidebar-section'>Generation</div>",
            unsafe_allow_html=True,
        )

        st.session_state.temperature = st.slider(
            "Temperature", min_value=0.0, max_value=1.0, value=0.30, step=0.05
        )
        st.session_state.top_k = st.slider(
            "Top K", min_value=1, max_value=10, value=5
        )
        st.session_state.max_tokens = st.slider(
            "Max Tokens", min_value=128, max_value=2048, value=512, step=64
        )

        st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
        st.caption("Powered by Gemma 4 • ChromaDB")