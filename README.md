# 🔗 Link Extractor (Multithreaded Web Scraper)

This is a simple Python project that extracts all the links from one or more websites. It uses multithreading to make it faster and follows a **producer–consumer** setup:

- 🧵 The **producer** gets the HTML from websites
- 🧪 The **consumer** reads the HTML and pulls out all `<a href="...">` links
- 💾 All the links are saved into a text file

---

## 💡 How It Works (File Overview)

link_extractor/ ├── main.py # Runs everything together using threads ├── test.py # Lets you test a single website from the terminal ├── producer.py # Downloads HTML from websites ├── consumer.py # Parses the HTML and extracts the links ├── urls.txt # A list of URLs to scrape (used by main.py) ├── output.txt # Where the extracted links are saved ├── test_extractor.py # Unit tests for link parsing

---

## 🚀 How to Use It

### 1. 📦 Install the required packages

Open your terminal and run:
```bash
pip install  requests          to fetch websites
pip install  beautifulsoup4    to parse HTML

Test one website
python test.py https://www.nba.com
python test.py https://www.nba.com [output_file].txt

Test main code
Add urls to urls.txt

python main.py
python main.py [output_file].txt


main.py loads the URLs from urls.txt

It starts two threads:
producer.py: fetches the websites
consumer.py: extracts the links from the HTML

The producer sends HTML to the queue
The consumer reads from the queue and saves the links

Everything is saved to a text file like output.txt
