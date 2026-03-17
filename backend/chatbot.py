import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5")  # versi stabil

def get_ai_response(message):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        print("Gemini API error:", e)
        return f"Error contacting Gemini API: {e}"