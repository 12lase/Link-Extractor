# 🔗 Link Extractor (Multithreaded Web Scraper)

This is a simple Python project that extracts all the links from one or more websites. It uses multithreading to make it faster and follows a **producer–consumer** setup:

- 🧵 The **producer** gets the HTML from websites
- 🧪 The **consumer** reads the HTML and pulls out all `<a href="...">` links
- 💾 All the links are saved into a text file

---

## 💡 How It Works (File Overview)

link_extractor/ 
├── main.py # Runs everything together using threads
├── test.py # Lets you test a single website from the terminal 
├── producer.py # Downloads HTML from websites 
├── consumer.py # Parses the HTML and extracts the links 
├── urls.txt # A list of URLs to scrape (used by main.py) 
├── output.txt # Where the extracted links are saved 
