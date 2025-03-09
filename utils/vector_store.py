import os
from turtle import st
from .config import embeddings, llm
from langchain_experimental.text_splitter import SemanticChunker
from langchain_chroma import Chroma


def create_vector_store(store_path: str, web_name: str, content: list|str):
    if isinstance(content, str):
        content = [content]
    
    
    chunker=SemanticChunker(embeddings=embeddings)
    
    docs=chunker.create_documents(content)
    
    vector_store = Chroma(
        collection_name=f"{web_name}",
        embedding_function=embeddings,
        persist_directory=store_path, 
    )
    
    vector_store.add_documents(docs)
    
    
def get_retriever(store_path: str, web_name: str):
    vector_store = Chroma(
        collection_name=f"{web_name}",
        embedding_function=embeddings,
        persist_directory=store_path,  
    )
    
    return vector_store.as_retriever()
    
    

        


