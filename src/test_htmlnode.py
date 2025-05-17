import unittest
from htmlnode import HTMLNode, HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node, node2)
        self.assertNotEqual(node, HTMLNode("div", "This is a div", [], {"class": "container"}))
        self.assertNotEqual(node, HTMLNode("div", "This is a different div", [], {"class": "container"}))
        self.assertNotEqual(node, HTMLNode("div", "This is a div", [], {"class": "different"}))

if __name__ == "__main__":
    unittest.main()