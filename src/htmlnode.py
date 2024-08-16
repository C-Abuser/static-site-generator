class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children

        if props is None:
            self.props = {}
        else:
            self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        buffer = []

        for k in self.props:
            buffer.append(f"{k}={self.props[k]}")

        return " ".join(buffer)

    def __repr__(self):
       return f"Tag: {self.tag} Value:{self.value} Children:{self.children} Props:{self.props}"


