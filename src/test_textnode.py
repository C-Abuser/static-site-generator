import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


class TestTextNode2(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Test case 52","italic")
        node2 = TextNode("Test case 52","italic")
        self.assertEqual(node,node2,"Success")

class TextTextNode3(unittest.TestCase):
    def text_noteq(self):
        node = TextNode("FIrst of the tested nodes","bold",None)
        node2 = TextNode("FIrst of the tested nodes","bold","/first/url")
        self.assertNotEqual(node,node2,"Success")

class TestTextNode(unittest.TestCase):
    def text_nothing(self):
        node = TextNode(None,None)
        node2 = TextNode(None,None)
        self.asserEqual(print(node),print(node2))

if __name__ == "__main__":
    unittest.main()
