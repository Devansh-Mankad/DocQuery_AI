import platform
import time
from pathlib import Path
import streamlit as st
from components.chat import (
    add_assistant_message,
    add_user_message,
    initialize_chat,
    render_chat,
    render_typing_animation,
)
from components.footer import render_footer
from components.header import render_header
from components.sidebar import render_sidebar
from components.source_panel import render_sources
from rag import RAGPipeline

st.set_page_config(
    page_title="DocQuery AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

def _load_css() -> None:
    css_path = Path("assets/style.css")
    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )
_load_css()

@st.cache_resource
def _load_pipeline() -> RAGPipeline:
    return RAGPipeline()

pipeline = _load_pipeline()

def _init_state() -> None:
    defaults = {
        "sources":        [],
        "response_time":  0.0,
        "total_queries":  0,
        "total_tokens":   0,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)

initialize_chat()
_init_state()

render_header()
render_sidebar()

main_col, info_col = st.columns([5, 2], gap="large")

with main_col:
    if not st.session_state.messages:
        st.markdown(
            """
            <div class="glass-card hero-card">
                <div class="hero-title">Welcome to DocQuery AI</div>
                <div class="hero-subtitle">
                    Ask questions about your indexed documents using
                    Retrieval-Augmented Generation.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        quick_prompts = {
            "📚 Scholarships": "What scholarships are available?",
            "🏠 Hostel":        "Tell me the hostel rules.",
            "🚌 Transport":     "Explain transport facilities.",
            "💼 Placement":     "Explain placement opportunities.",
        }

        rows = [list(quick_prompts.items())[i:i+2] for i in range(0, 4, 2)]
        for row in rows:
            cols = st.columns(2)
            for col, (label, prompt) in zip(cols, row):
                with col:
                    if st.button(label, use_container_width=True):
                        st.session_state.quick_prompt = prompt

    render_chat()

    prompt: str | None = st.chat_input("Ask anything about your documents…")
    if "quick_prompt" in st.session_state:
        prompt = st.session_state.pop("quick_prompt")

    if prompt:
        add_user_message(prompt)

        typing_placeholder = st.empty()
        with typing_placeholder:
            render_typing_animation()

        start = time.perf_counter()
        try:
            result  = pipeline.ask(prompt)
            elapsed = round(time.perf_counter() - start, 2)

            typing_placeholder.empty()
            add_assistant_message(result["answer"])

            st.session_state.sources       = result["sources"]
            st.session_state.response_time = elapsed
            st.session_state.total_queries += 1
            st.session_state.total_tokens  += len(result["answer"].split())
            st.rerun()

        except Exception as exc:
            typing_placeholder.empty()
            st.error(f"Generation failed\n\n{exc}")


with info_col:
    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>Retrieval Information</div></div>",
        unsafe_allow_html=True,
    )
    render_sources(st.session_state.sources)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>Session Statistics</div></div>",
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Queries",  st.session_state.total_queries)
    with c2:
        st.metric("Response", f"{st.session_state.response_time:.2f}s")

    c3, c4 = st.columns(2)
    with c3:
        st.metric("Words",    st.session_state.total_tokens)
    with c4:
        st.metric("Messages", len(st.session_state.messages))

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>Knowledge Base</div></div>",
        unsafe_allow_html=True,
    )

    unique_docs = len({s.get("source", "") for s in st.session_state.sources})
    kb1, kb2 = st.columns(2)
    with kb1:
        st.metric("Documents", unique_docs)
    with kb2:
        st.metric("Retrieved", len(st.session_state.sources))

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>AI Engine</div></div>",
        unsafe_allow_html=True,
    )
    for status in ("🟢 Gemma 4 E2B", "🟢 ChromaDB", "🟢 Sentence Transformers", "🟢 RAG Pipeline Ready"):
        st.success(status)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>Conversation</div></div>",
        unsafe_allow_html=True,
    )

    user_count      = sum(1 for m in st.session_state.messages if m["role"] == "user")
    assistant_count = sum(1 for m in st.session_state.messages if m["role"] == "assistant")

    q1, q2 = st.columns(2)
    with q1:
        st.metric("Questions", user_count)
    with q2:
        st.metric("Answers", assistant_count)

    st.progress(min(user_count / 20, 1.0))
    st.caption("Conversation Progress")

    st.markdown("<br>", unsafe_allow_html=True)

    btn1, btn2 = st.columns(2)

    with btn1:
        if st.button("🗑 Clear Chat", use_container_width=True):
            st.session_state.update(
                messages=[],
                sources=[],
                total_queries=0,
                total_tokens=0,
                response_time=0.0,
            )
            st.rerun()

    with btn2:
        chat_export = "\n\n".join(
            f"{m['role'].capitalize()}: {m['content']}"
            for m in st.session_state.messages
        )
        st.download_button(
            "⬇ Export",
            data=chat_export,
            file_name="conversation.txt",
            mime="text/plain",
            use_container_width=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<div class='glass-card'><div class='gradient-text'>Runtime</div></div>",
        unsafe_allow_html=True,
    )

    runtime_info = {
        "Python":    platform.python_version(),
        "Framework": "Streamlit",
        "LLM":       "Gemma 4 E2B",
        "Vector DB": "ChromaDB",
        "Embedding": "Sentence Transformers",
    }

    for key, value in runtime_info.items():
        left, right = st.columns([2, 3])
        with left:
            st.write(f"**{key}**")
        with right:
            st.write(value)


st.markdown("<br>", unsafe_allow_html=True)

if not st.session_state.messages:
    st.info("👋 Start a conversation by asking a question about your indexed documents.")
elif assistant_count := sum(1 for m in st.session_state.messages if m["role"] == "assistant"):
    st.success(f"Conversation contains {assistant_count} AI response(s).")

st.markdown("<br>", unsafe_allow_html=True)
render_footer()