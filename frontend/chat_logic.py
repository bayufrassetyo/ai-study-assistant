import requests
from datetime import datetime
import random
from config import API_URL

def get_ai_reply(message: str) -> str:
    try:
        response = requests.post(API_URL, json={"message": message})
        response.raise_for_status()
        return response.json().get("reply", "No response from AI.")
    except Exception as e:
        return f"Error contacting backend: {e}"

def send_message(message: str, messages_list: list):
    timestamp = datetime.now().strftime("%H:%M:%S")
    messages_list.append(("user", f"{message} (Sent at {timestamp})"))

    loading_messages = [
        "🤔 AI is thinking...",
        "🔍 Processing your question...",
        "🧠 Consulting the AI brain...",
        "✨ Generating answer..."
    ]
    ai_reply = get_ai_reply(message)
    messages_list.append(("assistant", f"{ai_reply} (Replied at {timestamp})"))