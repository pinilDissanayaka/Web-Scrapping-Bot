import os
from utils import scape_web,  write_markdown_file, create_vector_store
from urllib.parse import urlparse
from utils import embeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from database import Bot, session, Base, engine
from agent import get_chat_response
import asyncio


def create_bot(base_url : str):
    web_content = scape_web(base_url=base_url)
    web_name=urlparse(base_url).netloc
    
    file_path=os.path.join("data", f"{web_name}_output.md")
    vector_store_path=os.path.join("vector", f"{web_name}_vector_store")
    write_markdown_file(file_path=file_path, content=web_content)
    
    create_vector_store(store_path=vector_store_path, web_name=web_name, content=web_content)
    
    
    new_bot=Bot(base_url=base_url, web_name=web_name, data_set_path=file_path, vector_store_path=vector_store_path)
    session.add(new_bot)
    session.commit()
    
    
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    response = asyncio.run(get_chat_response("what is no loop tech?"))
    print(response)
    
    
    
    
    
    

    
    
    
    
    
    


