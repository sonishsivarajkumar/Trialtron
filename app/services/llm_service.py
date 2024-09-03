# app/services/llm_service.py
import openai
from config import settings

openai.api_key = settings.OPENAI_API_KEY

class LLMService:
    @staticmethod
    def generate_content(prompt: str):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1000
        )
        return response.choices[0].text.strip()
