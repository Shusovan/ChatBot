from state.state import State


class ChatBotNode:
    """
        Basic chatbot node that interacts with an LLM model.
    """

    def __init__(self, llm_model):
        self.llm = llm_model

    def process(self, state:State) -> dict:
        """
            Process the input state and generate a response using the LLM model.
        """

        return {"messages": self.llm.invoke(state['messages'])}