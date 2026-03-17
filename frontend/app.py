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
    st.image("https://cdn-icons-png.flaticon.com/512/3449/3449462.png", width=80) # Ikon Buku/AI
    st.title("Study Guide")
    st.info("Gunakan chatbot ini untuk bertanya seputar Python, AI, dan Machine Learning.")
    
    st.divider() # Garis pemisah yang rapi
    
    st.header("Options")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.header("💡 Try Questions")
    for q in EXAMPLE_QUESTIONS:
        if st.button(q, use_container_width=True):
            with st.spinner("Thinking..."):
                send_message(q, st.session_state.messages)
            st.rerun()

# User Input
user_input = st.chat_input("Ask something...")
if user_input:
    with st.spinner("🤖 Asisten sedang merangkum jawaban..."):
        send_message(user_input, st.session_state.messages)
    st.rerun()

# Welcome Message
if not st.session_state.messages:
    st.chat_message("assistant").write("Halo! Saya asisten belajarmu. Ada konsep AI atau kode Python yang ingin kamu tanyakan hari ini?")

# Display chat
display_chat(st.session_state.messages)

# Download
if st.session_state.messages:
    chat_text = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.messages])
    st.download_button("Download Chat", chat_text, file_name="ai_study_chat.txt")