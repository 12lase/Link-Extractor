# consumer.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading

# Shared lock so multiple consumers don’t write to the file at the same time
write_lock = threading.Lock()

def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    return [urljoin(base_url, a['href']) for a in soup.find_all("a", href=True)]

def start_consumer(queue, output_file="output.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        while True:
            item = queue.get()

            if item is None:
                print("[Consumer] No more items. Exiting.")
                break

            url, html = item
            print(f"[Consumer] Extracting from: {url}")

            try:
                links = extract_links(html, url)
                with write_lock:
                    f.write(f"# Links from: {url}\n")
                    for link in links:
                        f.write(link + "\n")
                    f.write("\n")
                print(f"[Consumer] Saved {len(links)} links from {url}")
            except Exception as e:
                print(f"[Consumer] Error parsing {url}: {e}")
