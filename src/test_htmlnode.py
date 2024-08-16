import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_html_eq(self):
        html = HTMLNode("a", "link to the site", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        html2 = HTMLNode("a", "link to the site", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(html, html2)

class TestHTMLNode2(unittest.TestCase):
    def test_html_empty(self):
        html = HTMLNode(None, None, None, None)
        html2 = HTMLNode(None, None, None, None)
        self.assertNotEqual(html, html2)

class TestHTMLNode3(unittest.TestCase):
    def test_html_noteq(self):
        test_node = HTMLNode("a", "link", None, None)
        html = HTMLNode("a", "link to the site", [test_node, test_node, test_node], {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        html2 = HTMLNode("a", "link to the site", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertNotEqual(html, html2)  # Changed to assertNotEqual since they are supposed to be different

if __name__ == "__main__":
    unittest.main()

