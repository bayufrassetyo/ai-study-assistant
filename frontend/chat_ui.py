import streamlit as st

def display_chat(messages_list):
    for role, message in messages_list:
        with st.chat_message(role):
            st.write(message)