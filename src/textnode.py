from enum import Enum

class TextType(Enum):
    TEXT="Text"
    BOLD="Bold"
    ITALIC="Italic"
    CODE="Code"
    LINK="Link"
    IMAGE="Image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self == other:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

    