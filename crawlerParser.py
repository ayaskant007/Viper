import requests
import certifi
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# print(certifi.where())
queue = ["https://google.com"]
visited = set()

full_url = urljoin(queue[0], "/services")

try:
    response = requests.get(queue[0])
    # print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.get_text()
    body = soup.body
    # print(title)

    links = []
    for link in soup.find_all('a'):
        links.append(link.get("href"))
        print(link.get("href"))

    for i in links:
        if i.startswith("http" or "https" or "www"):
            print(f"full relative urls are: {i}")
        else:
            full_url = urljoin(queue[0], i)
            print(f"incomplete urls such as {full_url} were fixed.")


    site_info = {
        "title": title,
        "body": body,
        "links": links
    }

    print(site_info)

except Exception as e:
    print(e)


    
    