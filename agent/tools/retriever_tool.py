import os
from langchain.tools.retriever import create_retriever_tool
from utils import get_retriever
from urllib.parse import urlparse


base_url="https://nolooptech.com/"

web_name=urlparse(base_url).netloc

file_path=os.path.join("data", f"{web_name}_output.md")
vector_store_path=os.path.join("vector", f"{web_name}_vector_store")

retriever_tool = create_retriever_tool(
    get_retriever(store_path=vector_store_path, web_name=web_name),
    "retrieve_about_NoLoopTech_Website",
    "Search and return information about retrieve_about No Loop Tech Website.",
)

tools = [retriever_tool]