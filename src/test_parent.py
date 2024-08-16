import unittest

from parent_node import ParentNode

class TestParentNode(unittest.TestCase):
    def eq_parents(self):
        parent = ParentNode("p",  [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ])
        self.assertEqual(eq_parent.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

class TestParentNode2(unittest.TestCase):
    def not_eq_parent(self):
        parent = ParentNode("div", [
            LeafNode("a","link"),
            LeafNode("div", "wrapper"),
            LeafNode("p", "paragraph")
        ])
        self.assertNotEqual(parent, "<a><div>Baganda</div></a>")

class TestParentNode3(unittest.TestCase):
    def empty_leafs(self):
        parent = ParentNode(None,None)
        self.asserNotEqual(parent.to_hmtl(), "<a>link</a>")
if __name__ == "__main__":
    unittest.main()
