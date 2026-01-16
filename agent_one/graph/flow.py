
from langgraph.graph import StateGraph, START, END

from agent_one.node.chatbot_node import ChatBotNode
from agent_one.state.state import State


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

        self.graph_builder.add_node("ChatBot", self.chatbot_node.process)
        self.graph_builder.add_edge(START, "ChatBot")
        self.graph_builder.add_edge("ChatBot", END)


    def graph_setup(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        Currently supports 'chatbot' use case.
        """

        if usecase == "ChatBot":
            self.chatbot_graph()

        else:
            raise ValueError(f"Unsupported usecase: {usecase}")

        return self.graph_builder.compile()