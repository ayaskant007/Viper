import requests
import certifi
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from whoosh.index import create_in
from whoosh.fields import *
import os
import time


if os.path.isdir("index_dir"):
    print("Folder exists.")
else:
    os.mkdir("index_dir")


my_schema = Schema(url=ID(stored=True, unique=True),
                   title=TEXT(stored=True), content=TEXT)
ix = create_in("index_dir", my_schema)
writer = ix.writer()


queue = [
    "https://google.com",
    "https://youtube.com",
    "https://facebook.com",
    "https://instagram.com",
    "https://chatgpt.com",
    "https://x.com",
    "https://reddit.com",
    "https://wikipedia.org",
    "https://whatsapp.com",
    "https://bing.com",
    "https://tiktok.com",
    "https://yahoo.co.jp",
    "https://yandex.ru",
    "https://yahoo.com",
    "https://amazon.com",
    "https://gemini.google.com",
    "https://baidu.com",
    "https://bet.br",
    "https://linkedin.com",
    "https://netflix.com",
    "https://naver.com",
    "https://temu.com",
    "https://pinterest.com",
    "https://live.com",
    "https://dzen.ru",
    "https://office.com",
    "https://bilibili.com",
    "https://microsoft.com",
    "https://weather.com",
    "https://twitch.tv",
    "https://fandom.com",
    "https://vk.com",
    "https://news.yahoo.co.jp",
    "https://canva.com",
    "https://globo.com",
    "https://t.me",
    "https://mail.ru",
    "https://duckduckgo.com",
    "https://samsung.com",
    "https://ebay.com"
]

visited = set()
limit = 30


while len(queue) > 0 and len(visited) < limit:
    url = queue.pop(0)

    if url not in visited:
        visited.add(url)
        print(url)
        try:
            response = requests.get(url, verify=certifi.where())
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.get_text()
            body = soup.body
            content = body.get_text(
                separator=" ", strip=True) if body else "No content available."

            relative_links = []

            for link in soup.find_all('a'):
                href_link = link.get("href")  # Get it once

                if href_link != None:
                    href_link = str(href_link)
                    if href_link.startswith(("http", "https", "www")):
                        relative_links.append(href_link)
                    else:
                        full_url = urljoin(url, href_link)
                        relative_links.append(full_url)

            site_info = {
                "title": title,
                "body": content,
                "links": relative_links
            }

            print(site_info)
            queue.extend(relative_links)

            writer.add_document(title=title, url=url, content=content)
            
            time.sleep(3) # Be nice to the servers and avoid getting blocked by adding a delay between requests.
        except Exception as e:
            print(e)

writer.commit()

#TODO: Add rotating user agents and proxy support to further reduce the chances of getting blocked by servers.

