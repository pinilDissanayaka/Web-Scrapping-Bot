import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()
scraped_content = []

def scrape_page(url: str)-> list:
    if url in visited_urls:
        return  
    
    print(f"Scraping: {url}")
    visited_urls.add(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    page_content = soup.get_text(separator='\n', strip=True)
    scraped_content.append(page_content) 

    
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])  
        if next_url.startswith(url): 
            scrape_page(next_url)

    return scraped_content  

            
            
            
def scape_web(base_url:str)->list:
    web_content=scrape_page(base_url)
    
    return web_content