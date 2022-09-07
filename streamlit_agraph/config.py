

class Config:
  def __init__(self, height=750, width=750, graphviz_layout=None, graphviz_config=None, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True, collapsible=True, **kwargs):
    self.height = f"{height}px"
    self.width = f"{width}px"
    # self.graphviz_layout = graphviz_layout
    # self.graphviz_config = graphviz_config
    # self.nodeHighlightBehavior = nodeHighlightBehavior
    # self.highlightColor = highlightColor
    # self.automaticRearrangeAfterDropNode=True
    # self.collapsible=collapsible
    # self.directed=directed
    self.__dict__.update(**kwargs)
    # self.node = { "highlightStrokeColor":"#F7A7A6"} #"highlightColor":"black",
    # self.link = {"highlightColor": "#FDD2BS"}

  def to_dict(self):
    return self.__dict__

  