from langchain_huggingface import ChatHuggingFace


class HuggingFaceLLM:

    def __init__(self, user_controls_input):
        self.user_control_input = user_controls_input

    def get_llm_model(self):

        try:
            huggingface_api_key = self.user_control_input.get("HUGGINGFACE_API_KEY")
            huggingface_model_name = self.user_control_input.get("model_choice")

            if not huggingface_api_key:
                raise ValueError("HuggingFace API Key is required to initialize HuggingFace LLM.")
        
            llm = ChatHuggingFace(model=huggingface_model_name, api_key=huggingface_api_key, temperature=0.7, max_tokens=1024)

        except Exception as e:
            print(f"Error initializing HuggingFace LLM: {e}")

        return llm

