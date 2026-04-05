

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props:
            return f' href="{self.props['href']}" target="{self.props['target']}"'
        else:
            return ''
        
    def __repr__(self) -> str:
        return f'tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}'