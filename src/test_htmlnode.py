import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = { "href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("p", "This is a value", children=None, props=props)
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_props_none(self):
        props = None
        node = HTMLNode("p", "This is a value", children=None, props=props)
        html = node.props_to_html()
        self.assertEqual(html, "")

    def test_props_empty(self):
        props = {}
        node = HTMLNode("p", "This is a value", children=None, props=props)
        html = node.props_to_html()
        self.assertEqual(html, "")