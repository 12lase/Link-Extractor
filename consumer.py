# consumer.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading

# Shared lock so multiple consumers don’t write to the file at the same time
write_lock = threading.Lock()

# BeautifulSoup parses all the html using built in python parser
# returns list of formated links for url passed 
def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    return [urljoin(base_url, a['href']) for a in soup.find_all("a", href=True)]

# Extracts links from queue and outputs them to an output file
def start_consumer(queue, output_file="output.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        while True:
            item = queue.get() # Wait for an item from the queue

            if item is None:
                # Signal from producer that all work is done
                print("[Consumer] No more items. Exiting.")
                break

            url, html = item # Unpack the URL and HTML string
            print(f"[Consumer] Extracting from: {url}")

            try:
                # Parse HTML and extract absolute links
                links = extract_links(html, url)

                # Ensure only one thread writes to the file at a time
                with write_lock:
                    f.write(f"# Links from: {url}\n")
                    for link in links:
                        f.write(link + "\n")
                    f.write("\n")
                print(f"[Consumer] Saved {len(links)} links from {url}")
            except Exception as e:
                print(f"[Consumer] Error parsing {url}: {e}")
