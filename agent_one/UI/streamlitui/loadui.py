import streamlit as st
import os

from agent_one.UI.uiconfigfile import Config


class LoadStreamlitUI:

    # initializing the class to load all configuration files
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def render(self):

        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.title(self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecases_options = self.config.get_usecase_options()

            self.user_controls['llm_choice'] = st.selectbox(label="Select LLM Model", options=llm_options, index=0)

            # LLM Selection
            if self.user_controls['llm_choice'] == "Groq":
                model_options = self.config.get_groq_models()
                self.user_controls['model_choice'] = st.selectbox(label="Select Groq Model", options=model_options, index=0)
                self.user_controls['GROQ_API_KEY'] = st.text_input(label="Enter Groq API Key", type="password")

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API Key to proceed.")

            elif self.user_controls['llm_choice'] == "HuggingFace":
                model_options = self.config.get_huggingface_models()
                self.user_controls['model_choice'] = st.selectbox(label="Select HuggingFace Model", options=model_options, index=0)
                self.user_controls['HUGGINGFACE_API_KEY'] = st.text_input(label="Enter HuggingFace API Key", type="password")

                if not self.user_controls['HUGGINGFACE_API_KEY']:
                    st.warning("Please enter your API Key to proceed.")

            # Usecase Selection
            self.user_controls['usecase_choice'] = st.selectbox(label="Select Usecase", options=usecases_options, index=0)

        return self.user_controls