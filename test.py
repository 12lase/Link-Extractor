# test.py
import sys
import threading
from queue import Queue
from producer import start_producer
from consumer import start_consumer

def main():
    if len(sys.argv) < 2:
        print("Usage: python test.py https://example.com")
        return

    url = sys.argv[1]
    link_queue = Queue()
    urls = [url]  # Wrap in list for the producer

    producer_thread = threading.Thread(target=start_producer, args=(urls, link_queue))
    consumer_thread = threading.Thread(target=start_consumer, args=(link_queue,"output.txt"))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("[Test] Completed.")

if __name__ == "__main__":
    main()
