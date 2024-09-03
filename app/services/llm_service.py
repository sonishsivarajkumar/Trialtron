# app/services/llm_service.py
import openai

class LLMService:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_content(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error generating content: {e}")
            return "Error generating content. Please try again."
