from typing import List, Set
from streamlit_agraph.config import Config
from streamlit_agraph.triple import Triple
from streamlit_agraph.node import Node
from streamlit_agraph.edge import Edge

class TripleStore:
  def __init__(self) ->None:
    self.nodes_set: Set[Node] = set()
    self.edges_set: Set[Edge] = set()
    self.triples_set: Set[Triple] = set()

  def add_triple(self, node1, link, node2, image=""):
    nodeA = Node(id=node1, image=image)
    nodeB = Node(id=node2)
    edge = Edge(source=nodeA.id, target=nodeB.id, title=link)  # linkValue=link
    triple = Triple(nodeA, edge, nodeB)
    self.nodes_set.update([nodeA, nodeB])
    self.edges_set.add(edge)
    self.triples_set.add(triple)

  def getTriples(self)->Set[Triple]:
    return self.triples_set

  def getNodes(self)->Set[Node]:
    return self.nodes_set

  def getEdges(self)->Set[Edge]:
    return self.edges_set