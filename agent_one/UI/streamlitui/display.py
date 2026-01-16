from unittest import result
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    
    def display_result(self):
        """
        Displays the results of the AI agent's processing in the Streamlit UI.
        """

        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "ChatBot":
            
            for event in graph.stream({"messages":("user", user_message)}):
                print(event.values())

                for value in event.values():
                    print(value['messages'])

                    with st.chat_message("user"):
                        st.write(user_message)

                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)

        else:
            st.error(f"Display not implemented for use case: {self.usecase}")
    


    '''def display_result(self, user_message):
        # Add user message
        self.state["messages"].append(HumanMessage(content=user_message))

        # Call ChatBot node
        chatbot_node = self.graph.nodes["ChatBot"]
        self.state = chatbot_node(self.state)  # process messages via LLM

        # Display messages in Streamlit
        for msg in self.state["messages"]:
            if isinstance(msg, HumanMessage):
                with st.chat_message("user"):
                    st.write(msg.content)
            
            elif isinstance(msg, AIMessage):
                with st.chat_message("assistant"):
                    st.write(msg.content)

        else:
            st.error(f"Display not implemented for use case: {self.usecase}")'''