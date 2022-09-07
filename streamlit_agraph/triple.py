from streamlit_agraph.node import Node
from streamlit_agraph.edge import Edge

class Triple:
  def __init__(self, subj: Node, pred: Edge, obj:Node ) -> None:
    self.subj = subj
    self.pred = pred
    self.obj = obj
