import requests
from bs4 import BeautifulSoup

def scrape_topic(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content = ""
    for p in soup.select('p'):
        content += p.get_text()

    file_path = f"{topic.lower().replace(' ', '_')}.txt"
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(content)
    
    return file_path
