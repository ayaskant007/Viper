import requests
import certifi
from bs4 import BeautifulSoup
from urllib.parse import urljoin

queue = ["https://google.com", "https://www.facebook.com", "https://www.youtube.com"]
visited = set()
limit = 10


while len(queue) > 0 and len(visited) < limit:
    url= queue.pop(0)

    if url not in visited:
        visited.add(url)
        print(url)
        try:
            response = requests.get(url, verify=certifi.where())
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.get_text()
            body = soup.body


            relative_links = []

            for link in soup.find_all('a'):
                href_link = link.get("href")  # Get it once

                if href_link!=None:
                    href_link = str(href_link)
                    if href_link.startswith(("http", "https", "www")):
                        relative_links.append(href_link)
                    else:
                        full_url = urljoin(url, href_link)
                        relative_links.append(full_url)


            site_info = {
                "title": title,
                # "body": body,
                "links": relative_links
            }   

            print(site_info)
            queue.extend(relative_links)

        except Exception as e:
            print(e)


    
    