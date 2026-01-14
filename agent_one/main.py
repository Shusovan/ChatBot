import streamlit as st

from agent_one.UI.streamlitui.loadui import LoadStreamlitUI

def load_agent_one():

    """
    Docstring for load_agent_one
    This function initializes and renders the Streamlit UI for the AI application, configures the LLM Models.
    setup the graphs, and handles user interactions.
    """

    load_ui = LoadStreamlitUI()
    user_input = load_ui.render()

    if not user_input:
        st.error("Failed to load user inputs. Please try again.")
        return
    
    user_message = st.text_area("Enter your message here:", height=150)