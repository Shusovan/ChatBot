import streamlit as st

from agent_one.UI.streamlitui.loadui import LoadStreamlitUI
from agent_one.graph.flow import GraphBuilder
from agent_one.llm.groqllm import GroqLLM
from agent_one.UI.streamlitui.display import DisplayStreamlit

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

    if user_message:
        try:
            # Configure LLM Models based on user input
            llm_config = GroqLLM(user_controls_input=user_input)
            model = llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize LLM model. Please check your configuration.")
                return
            
            # Initialize and set up the graph based on usecase
            usecase = user_input.get("usecase_choice")

            if not usecase:
                st.error("Use case selection is required.")
                return
            
            graph_builder = GraphBuilder(model=model)

            try:
                graph = graph_builder.graph_setup(usecase=usecase)
                DisplayStreamlit(usecase=usecase, graph=graph, user_message=user_message).display_result()

            except ValueError as ve:
                st.error(str(ve))
                return

        except Exception as e:
            st.error(f"Error configuring LLM Models: {e}")
            return