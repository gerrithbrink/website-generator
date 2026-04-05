import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props_to_html_success(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(tag='test_tag',value='test_value',props=props)
        self.assertEqual(node.props_to_html(),  ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag='test_tag',value='test_value')
        self.assertEqual(node.props_to_html(),  '')



if __name__ == "__main__":
    unittest.main()