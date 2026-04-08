from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type is TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type is TextType.BOLD:
        return LeafNode(tag='b',value=text_node.text)
    elif text_node.text_type is TextType.CODE:
        return LeafNode(tag='code',value=text_node.text)
    elif text_node.text_type is TextType.ITALIC:
        return LeafNode(tag='i',value=text_node.text)
    elif text_node.text_type is TextType.LINK:
        props = {
            "href": text_node.url
        }
        return LeafNode('a', text_node.text, props)
    elif text_node.text_type is TextType.IMAGE:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode(tag='img',value='', props=props) 
    else:
        raise Exception('Invalid text type')
    