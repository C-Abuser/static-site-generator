import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq_leafs(self):
        leaf_node = LeafNode("a","Link", {"href": "https://google.com"})
        self.assertEqual(leaf_node.to_html(),"<a href='https://google.com'>Link</a>")

class TestLeafNode2(unittest.TestCase):
    def test_noteq_leafs(self):
        leaf_node = LeafNode("p", "This is the paragraph for the test!",None)
        self.assertNotEqual(leaf_node.to_html(),"<p>This s the paragraph for the test!</p>")

class TestLeafNode3(unittest.TestCase):
    def test_raw_leafs(self):
        leaf_node = LeafNode(None,"Raw Text",None)
        self.assertEqual(leaf_node.to_html(), "Raw Text")

class TestLeafNode(unittest.TestCase):
    def test_empty_leafts(self):
        leaf_node = LeafNode("","",None)
        self.assertEqual(leaf_node.to_html(),"< ></>")
if __name__ == "__main__":
    unittest.main()
