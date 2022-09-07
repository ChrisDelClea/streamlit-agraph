import networkx as nx
from networkx.algorithms import community
from streamlit_agraph.triplestore import TripleStore

class GraphAlgos:
  def __init__(self, store:TripleStore):
    self.node_names = [n.id for n in store.nodes_set]
    self.edges = [(e.source, e.target) for e in store.edges_set]
    G = nx.Graph()  # Initialize a Graph object
    G.add_nodes_from(self.node_names)  # Add nodes to the Graph
    G.add_edges_from(self.edges)  # Add edges to the Graph

    self.G = G
    self.density = self.density()
    # self.shortest_path() = self.shortest_path()
    # self.find_communities = self.find_communities()

  def density(self):
    return nx.density(self.G)

  def shortest_path(self, source, target):
    try:
      sp = nx.shortest_path(self.G, source=source, target=target)
    except nx.NetworkXNoPath:
      return  []
    else:
      return sp

  def find_communities(self) -> str:
    # print(nx.info(G))  # Print information about the Graph
    return "hello community"

  # def parse_node(*args):
  #  nodes_data = [{"id": f"{node}"} for node in nodes]