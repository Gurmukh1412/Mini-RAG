import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Mini RAG",
    layout="wide"
)

# -------------------------------------------------
# Elegant Light/Dark Theme
# -------------------------------------------------
st.markdown("""
<style>
:root {
    --bg: #ffffff;
    --surface: #ffffff;
    --border: #e5e7eb;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --accent: #4f46e5;
    --glow: rgba(79, 70, 229, 0.15);
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #020617;
        --surface: #020617;
        --border: #1e293b;
        --text-main: #f8fafc;
        --text-muted: #94a3b8;
        --accent: #6366f1;
        --glow: rgba(99, 102, 241, 0.25);
    }
}

body {
    background-color: var(--bg);
}

.wrapper {
    max-width: 1200px;
    margin: auto;
}

/* ---------- Header ---------- */
.hero {
    text-align: center;
    padding: 5rem 0 3.5rem 0;
}

.hero h1 {
    font-size: 3.2rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: var(--text-main);
}

.hero p {
    font-size: 1.15rem;
    margin-top: 0.8rem;
    color: var(--text-muted);
}

/* ---------- Cards ---------- */
.card {
    background-color: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    transition: box-shadow 0.3s ease, transform 0.25s ease;
}

.card:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 40px var(--glow);
}

.card-title {
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 1.3rem;
    color: var(--text-main);
}

/* ---------- Answer ---------- */
.answer-box {
    margin-top: 1.8rem;
    padding: 1.6rem;
    border-radius: 14px;
    background-color: var(--surface);
    border: 1px solid var(--border);
    box-shadow: 0 10px 30px var(--glow);
}

/* ---------- Buttons ---------- */
button[kind="primary"] {
    background: linear-gradient(
        135deg,
        var(--accent),
        #818cf8
    ) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    border: none !important;
}

/* ---------- Divider ---------- */
hr {
    border-color: var(--border);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Layout Wrapper
# -------------------------------------------------
st.markdown("<div class='wrapper'>", unsafe_allow_html=True)

# -------------------------------------------------
# Hero Section
# -------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🤖 Mini RAG</h1>
    <p>Ready to help the LLM</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Symmetric Layout
# -------------------------------------------------
left, right = st.columns(2, gap="large")

# ------------------ Add Knowledge ------------------
with left:
    st.markdown("""
    <div class="card">
        <div class="card-title">Add Knowledge</div>
    """, unsafe_allow_html=True)

    text = st.text_area(
        "Paste text",
        height=230,
        label_visibility="collapsed"
    )

    add_btn = st.button("Add Knowledge", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if add_btn:
        if text.strip():
            res = requests.post(
                f"{BACKEND_URL}/add",
                json={"text": text}
            )
            if res.status_code == 200:
                st.success("Knowledge added successfully")
            else:
                st.error(res.text)
        else:
            st.warning("Text cannot be empty")

# ------------------ Ask Question ------------------
with right:
    st.markdown("""
    <div class="card">
        <div class="card-title">Ask a Question</div>
    """, unsafe_allow_html=True)

    question = st.text_input(
        "Question",
        placeholder="Ask something about your documents…",
        label_visibility="collapsed"
    )

    k = st.slider("Context documents", 1, 10, 4)

    ask_btn = st.button("Ask Question", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if ask_btn:
        if question.strip():
            res = requests.post(
                f"{BACKEND_URL}/ask",
                json={"question": question, "k": k}
            )

            if res.status_code == 200:
                data = res.json()

                st.markdown("""
                <div class="answer-box">
                    <strong>Answer</strong>
                """, unsafe_allow_html=True)

                st.write(data["answer"])

                if data.get("sources"):
                    st.markdown("**Sources**")
                    for src in data["sources"]:
                        st.write(f"- {src}")

                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error(res.text)
        else:
            st.warning("Question cannot be empty")

# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    "<center style='color:var(--text-muted);'>Mini RAG · Premium Interface · Streamlit</center>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)
