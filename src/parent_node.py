from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,None)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tags are mandatory!")
        if self.children == None:
            raise ValueError("Empty children!")

        result = f"<{self.tag} {self.props_to_html()}>"

        for child in self.children:
            result += child.to_html()

        result += f"</{self.tag}>"

        return result
