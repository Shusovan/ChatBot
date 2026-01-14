from langgraph.graph import StateGraph

from node.chatbot_node import ChatBotNode
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

        self.chatbot_node=ChatBotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.chatbot_node.process)
        self.graph_builder.add_edge("START", "chatbot")
        self.graph_builder.add_edge("chatbot", "END")


    def graph_setup(self, usecase):
        """
        Sets up the graph based on the selected use case.
        Currently supports 'chatbot' use case.
        """

        if usecase == "chatbot":
            self.chatbot_graph()
            
        else:
            raise ValueError(f"Unsupported use case: {usecase}")

        return self.graph_builder