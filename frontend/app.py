import streamlit as st
from chat_logic import send_message
from chat_ui import display_chat
from config import EXAMPLE_QUESTIONS

st.set_page_config(page_title="AI Study Assistant", page_icon="📚")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("📚 AI Study Assistant")

# Sidebar
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.header("Try Questions")
    for q in EXAMPLE_QUESTIONS:
        if st.button(q):
            send_message(q, st.session_state.messages)
            st.rerun()

# User Input
user_input = st.chat_input("Ask something...")
if user_input:
    send_message(user_input, st.session_state.messages)

# Display chat
display_chat(st.session_state.messages)

# Download
if st.session_state.messages:
    chat_text = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.messages])
    st.download_button("Download Chat", chat_text, file_name="ai_study_chat.txt")