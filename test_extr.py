# test_extractor.py
import unittest
from queue import Queue
from consumer import extract_links
from producer import fetch_html

class TestLinkExtractor(unittest.TestCase):

    def test_extract_links_from_html(self):
        html = '''
        <html><body>
        <a href="https://example.com">Example</a>
        <a href="/relative/link">Relative</a>
        </body></html>
        '''
        base_url = "https://testsite.com"
        links = extract_links(html, base_url)
        self.assertIn("https://example.com", links)
        self.assertIn("https://testsite.com/relative/link", links)
        self.assertEqual(len(links), 2)

    def test_fetch_html_success(self):
        # Note: This hits a real site. Keep lightweight.
        queue = Queue()
        fetch_html("https://www.example.com", queue)
        result = queue.get()
        self.assertIsInstance(result, tuple)
        self.assertIn("https://www.example.com", result[0])
        self.assertIn("<html", result[1].lower())

if __name__ == "__main__":
    unittest.main()
