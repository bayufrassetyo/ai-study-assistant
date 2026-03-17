import streamlit as st

def display_chat(messages_list):
    for role, message in messages_list:
        with st.chat_message(role):
            color = "blue" if role == "user" else "green"
            prefix = "You" if role == "user" else "AI"
            st.markdown(f"<span style='color:{color}'><b>{prefix}:</b> {message}</span>", unsafe_allow_html=True)