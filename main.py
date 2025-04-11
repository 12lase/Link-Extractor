import threading
import sys
from queue import Queue
from producer import start_producer
from consumer import start_consumer

def load_urls(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def main():
    output_file = sys.argv[1] if len(sys.argv) > 1 else "output.txt"
    link_queue = Queue()
    urls = load_urls("urls.txt")

    producer_thread = threading.Thread(target=start_producer, args=(urls, link_queue))
    consumer_thread = threading.Thread(target=start_consumer, args=(link_queue, output_file))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print(f"[Main] All work completed. Links saved to {output_file}")

if __name__ == "__main__":
    main()
