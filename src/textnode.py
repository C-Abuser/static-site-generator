class TextNode():
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eg__(self,secondNode):
        if self.text == secondNode.text and self.text_type == secondNode.text_type and self.url == secondNode.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type},{self.url})"


