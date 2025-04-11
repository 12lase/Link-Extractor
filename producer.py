# producer.py
import requests
import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Optional: Custom headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

def fetch_html(url, queue, max_retries=3, min_delay=1, max_delay=3):
    attempt = 0
    while attempt < max_retries:
        try:
            print(f"[Producer] Fetching: {url} (Attempt {attempt + 1})")
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            queue.put((url, response.text))

            # Random delay to mimic human browsing
            time.sleep(random.uniform(min_delay, max_delay))
            return  # success, exit the function

        except requests.RequestException as e:
            print(f"[Producer] Failed to fetch {url}: {e}")
            attempt += 1
            wait_time = random.uniform(1, 2)
            print(f"[Producer] Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)

    print(f"[Producer] Giving up on {url} after {max_retries} attempts.")

def start_producer(urls, queue, max_workers=5):
    print(f"[Producer] Starting with {len(urls)} URLs, using {max_workers} threads.")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_html, url, queue) for url in urls]

        # Optionally wait for all to finish
        for future in as_completed(futures):
            pass  # We don't need the return, just ensuring all are done

    queue.put(None)  # Signal end of work
    print("[Producer] All tasks completed.")
