
def write_markdown_file(file_path:str, content:str|list)->str:
    
    if isinstance(content, list):
        page_content = ""
    
        for _content in content:
            page_content += _content
        
    with open(file_path, "w", encoding="utf-8") as file:
        print("Writing markdown file...")
        file.write(page_content)
        
    print("Markdown file written successfully!")
            