import streamlit as st

_MAX_PREVIEW_CHARS = 220
def render_sources(sources: list[dict]) -> None:
    """
    Render retrieved source documents in the right-hand panel.
    Each source is shown as an expandable card with a text preview,
    similarity score, and metadata metrics.
    """
    if not sources:
        return

    st.markdown(
        "<div class='source-title'>Retrieved Sources</div>",
        unsafe_allow_html=True,
    )

    for rank, source in enumerate(sources, start=1):
        _render_source_card(source, rank)

def _render_source_card(source: dict, rank: int) -> None:
    filename   = source.get("source", "Unknown")
    score      = source.get("score", 0.0)
    raw_text   = source.get("content", "").replace("\n", " ")
    preview    = raw_text[:_MAX_PREVIEW_CHARS] + "…" if len(raw_text) > _MAX_PREVIEW_CHARS else raw_text
    similarity = round(score * 100)

    with st.expander(f"📄 {filename}", expanded=(rank == 1)):
        col_text, col_score = st.columns([4, 1])

        with col_text:
            st.markdown(
                f"<div class='source-preview'>{preview}</div>",
                unsafe_allow_html=True,
            )

        with col_score:
            st.markdown(
                f"""
                <div class="similarity-card">
                    <div class="similarity-value">{similarity}%</div>
                    <div class="similarity-label">Similarity</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.divider()

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Rank", rank)
        with m2:
            st.metric("Similarity", f"{similarity}%")
        with m3:
            st.metric("Source", filename)