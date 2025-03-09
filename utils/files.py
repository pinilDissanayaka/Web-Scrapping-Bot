
def write_markdown_file(file_name:str, content:list)-> str:
    
    page_content = ""
    
    for _content in content:
        page_content += _content
        
    with open(file_name, "w", encoding="utf-8") as file:
        print("Writing markdown file...")
        file.write(page_content)
        
    return file_name