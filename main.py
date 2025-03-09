import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited_urls = set()

def scrape_page(url):
    if url in visited_urls:
        return  # Avoid visiting the same page multiple times
    
    print(f"Scraping: {url}")
    visited_urls.add(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text content
    page_content = soup.get_text(separator='\n', strip=True)
    print(page_content[:500])  # Print first 500 characters for preview

    # Extract all links and recursively scrape them
    for link in soup.find_all('a', href=True):
        next_url = urljoin(url, link['href'])  # Convert relative URLs to absolute
        if next_url.startswith(url):  # Ensure we stay within the base domain
            scrape_page(next_url)

# Provide the base URL here
base_url = "https://nolooptech.com/"
scrape_page(base_url)
