from datetime import datetime
import streamlit as st

def initialize_chat() -> None:
    """Ensure the messages list exists in session state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_user_message(content: str) -> None:
    st.session_state.messages.append(
        {"role": "user", "content": content, "time": _now()}
    )

def add_assistant_message(content: str) -> None:
    st.session_state.messages.append(
        {"role": "assistant", "content": content, "time": _now()}
    )

def _now() -> str:
    return datetime.now().strftime("%H:%M")

def render_chat() -> None:
    """Render all messages in the conversation history."""
    for index, message in enumerate(st.session_state.messages):
        _render_message(message, index)

def _render_message(message: dict, index: int) -> None:
    is_user = message["role"] == "user"
    avatar  = "👤" if is_user else "🤖"
    title   = "You" if is_user else "DocQuery AI"

    with st.container():
        st.markdown(
            f"""
            <div class="chat-card">
                <div class="chat-header">
                    <div class="chat-user">
                        <div class="chat-avatar">{avatar}</div>
                        <div>
                            <div class="chat-title">{title}</div>
                            <div class="chat-time">{message["time"]}</div>
                        </div>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(message["content"])

        if not is_user:
            _render_feedback_buttons(index)

        st.markdown("</div>", unsafe_allow_html=True)


def _render_feedback_buttons(index: int) -> None:
    """Render copy / like / dislike action row under assistant messages."""
    col1, col2, col3, _ = st.columns([1, 1, 1, 6])
    with col1:
        st.button("📋", key=f"copy_{index}", help="Copy response")
    with col2:
        st.button("👍", key=f"like_{index}", help="Good response")
    with col3:
        st.button("👎", key=f"dislike_{index}", help="Bad response")


def render_typing_animation() -> None:
    """Display the animated 'thinking' indicator while the model is generating."""
    st.markdown(
        """
        <div class="chat-card">
            <div class="chat-header">
                <div class="chat-user">
                    <div class="chat-avatar">🤖</div>
                    <div>
                        <div class="chat-title">DocQuery AI</div>
                        <div class="chat-time">Thinking…</div>
                    </div>
                </div>
            </div>
            <div class="typing">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )