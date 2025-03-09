from dotenv import load_dotenv
from typing_extensions import TypedDict, Annotated, Sequence
from langgraph.graph.message import add_messages
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.messages import BaseMessage


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


config={"configurable": {"thread_id": "2"}}