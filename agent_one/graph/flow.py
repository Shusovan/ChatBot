from langgraph.graph import StateGraph

from state.state import State


class GraphBuilder:

    def __init__(self, model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def chatbot_graph(self):
        """
        Builds a simple chatbot graph with LLM and message handling.
        This method initializes a chatbot node using the 'ChatBotNode' class
        and connects it to the LLM model provided during initialization.
        """
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge("START", "chatbot")
        self.graph_builder.add_edge("chatbot", "END")