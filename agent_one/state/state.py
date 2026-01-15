from pydantic import BaseModel
from typing import Annotated

from langgraph.graph.message import add_messages


class State(BaseModel):
    """
    Represents the state of the AI agent, including the LLM model and message history.
    """
    messages: Annotated[list, add_messages]