from utils import scape_web, write_markdown_file

if __name__ == "__main__":
    web_content = scape_web()
    write_markdown_file("output.md", web_content)