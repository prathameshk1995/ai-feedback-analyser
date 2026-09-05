import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found.")


client = genai.Client(api_key=api_key)


def analyze_feedback(feedback: str) -> str:

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=feedback
    )

    return response.text