import os
from langchain_groq import ChatGroq

class GroqLLM:

    def __init__(self, user_controls_input):
        self.user_control_input = user_controls_input


    def get_llm_model(self):

        try:
            groq_api_key = self.user_control_input.get("GROQ_API_KEY")
            groq_model_name = self.user_control_input.get("model_choice")

            if not groq_api_key:
                raise ValueError("GROQ API Key is required to initialize Groq LLM.")
        
            llm = ChatGroq(model=groq_model_name, api_key=groq_api_key, temperature=0.7, max_tokens=1024)

        except Exception as e:
            print(f"Error initializing Groq LLM: {e}")

        return llm