import os
import csv
import json

from operator import itemgetter
import streamlit.components.v1 as components
from typing import List, Set

import networkx as nx
from networkx.algorithms import community

import streamlit as st


_RELEASE = True

if not _RELEASE:
    _agraph = components.declare_component(
        "agraph",
        url="http://localhost:3001",
    )

else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _agraph = components.declare_component("agraph", path=build_dir)


class Config:
  def __init__(self, height=800, width=1000, graphviz_layout=None, graphviz_config=None, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True, collapsible=True, **kwargs):
    self.height = height
    self.width = width
    self.graphviz_layout = graphviz_layout
    self.graphviz_config = graphviz_config
    self.nodeHighlightBehavior = nodeHighlightBehavior
    self.highlightColor = highlightColor
    self.automaticRearrangeAfterDropNode=True
    self.collapsible=collapsible
    self.directed=directed
    self.__dict__.update(kwargs)
    # self.node = { "highlightStrokeColor":"#F7A7A6"} #"highlightColor":"black",
    # self.link = {"highlightColor": "#FDD2BS"}

  def to_dict(self):
    return self.__dict__

class Node:
  def __init__(self,
              id,
              size=250,
              color="#ACDBC9",
              # label=None,
              # labelProperty=None,
              renderLabel=True,
              labelPosition="right",
              svg="",
              symbolType="circle",
              strokeColor="", #F7A7A6
              **kwargs
               ):
    self.id=id
    self.size=size
    self.color=color #FDD2BS #F48B94 #F7A7A6 #DBEBC2
    self.renderLabel=renderLabel
    self.labelPosition=labelPosition #(left,top,bottom,right, center)
    self.svg=svg
    self.symbolType=symbolType  # "cross", "diamond", "square", "star", "triangle", "wye"
    self.strokeColor=strokeColor
    self.__dict__.update(kwargs)

  def to_dict(self):
    return self.__dict__

class Edge:
  def __init__(self, source, target,
              color="#F7A7A6",
              # highlightColor="#F7A7A6", #F7A7A6
              type="STRAIGHT",
              semanticStrokeWidth=False,
              strokeWidth=1.5,
              labelProperty="",
              renderLabel=False,
              labelPosition="right",
              linkValue=1,
               **kwargs
               ):
    self.source=source
    self.target=target
    self.color=color #labelPropertyF48B94 #F7A7A6 #
    self.renderLabel=renderLabel
    self.labelPosition=labelPosition #(left,top,bottom,right, center)
    # self.highlightColor=highlightColor
    self.type=type #CURVE_SMOOTH , CURVE_FULL
    self.semanticStrokeWidth=semanticStrokeWidth #strokeWidth += (linkValue * strokeWidth) / 10;
    self.strokeWidth=strokeWidth
    self.labelProperty=labelProperty
    self.linkValue=linkValue
    self.__dict__.update(kwargs)

  def to_dict(self):
    return self.__dict__

class Triple:
  def __init__(self, subj: Node, pred: Edge, obj:Node ) -> None:
    self.subj = subj
    self.pred = pred
    self.obj = obj

class TripleStore:
  def __init__(self) ->None:
    self.nodes_set: Set[Node] = set()
    self.edges_set: Set[Edge] = set()
    self.triples_set: Set[Triple] = set()

  def add_triple(self, node1, link, node2, picture=""):
    nodeA = Node(node1, svg=picture)
    nodeB = Node(node2)
    edge = Edge(source=nodeA.id, target=nodeB.id, label=link, renderLabel=True)  # linkValue=link
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

def _set_graphviz_layout(nodes, edges, config):
    try:
        import pygraphviz as pgv
    except ImportError as e:
        raise ImportError("requires pygraphviz " "http://pygraphviz.github.io/") from e
      
    G = pgv.AGraph(**getattr(config, 'graphviz_config'))
    node_args = {}
    for node in nodes:
      node_id = getattr(node, 'id')
      G.add_node(node_id)
      node_args[node_id] = node.to_dict()
    for edge in edges:
      G.add_edge(getattr(edge, 'source'), getattr(edge, 'target'))
    G.layout(getattr(config, 'graphviz_layout'))
    
    for n in G.nodes():
      node = G.get_node(n)
      try:
          xs = node.attr["pos"].split(",")
          node_args[node.get_name()].update({'x': float(xs[0]), 
                                              'y': float(xs[1])})
      except:
          print("no position for node", n)
          node_args[node.get_name()].update({'x': 0, 'y': 0})
            
    nodes = [Node(**node_args[n]) for n in G.nodes()]
    
    return nodes, edges
      
def agraph(nodes, edges, config):
    layout = getattr(config, 'graphviz_layout')
    if layout:
      config.d3 = {'disableLinkForce': True}
      nodes, edges = _set_graphviz_layout(nodes, edges, config)

    nodes_data = [ node.to_dict() for node in nodes]
    edges_data = [ edge.to_dict() for edge in edges]

    #nodes_data = [{"id": f"{node}"} for node in nodes]
    #edges_data = [ {"source": f"{edge[0]}", "target": f"{edge[1]}"} for edge in edges]

    config_json = json.dumps(config.__dict__)
    # st.write(config_json)

    data = { "nodes": nodes_data, "links": edges_data}
    # st.write(data)
    data_json = json.dumps(data)
    component_value = _agraph(data=data_json, config=config_json)

    return component_value

# app: `$ streamlit run agraph/__init__.py`
if not _RELEASE:
    import json
    import streamlit as st

    st.subheader("Component with constant args")
    nodes = []
    edges = []
    nodes.append( Node(id="Spiderman", size=1000, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") ) # ,
    nodes.append( Node(id="Captain_Marvel", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
    edges.append(Edge(source="Captain_Marvel", target="Spiderman", type="CURVE_SMOOTH"))
    # nodes.append( Node(id="Chris_Klose", size=400, svg="https://github.com/ChrisChross/streamlit-agraph/blob/master/imgs/Chris.png?raw=true") ) #
    # edges.append(Edge(source="Chris_Klose", target="Spiderman", type="CURVE_SMOOTH"))
    # edges.append( Edge(source="Chris_Klose", target="Spiderman", type="CURVE_SMOOTH") )
   # edges.append(Edge(source="Chris_Klose", target="Captain_Marvel", type="CURVE_SMOOTH" )) # renderLabel=True, labelProperty="best_friend_of"
    #nodes = ["Harry","Sally","Peter","Chris"]
    #edges = [("Harry","Sally"),("Peter","Chris")]

    # myConfig = { "nodeHighlightBehavior": "true", "node": { "color": "lightgreen", "size": 120, "highlightStrokeColor": "blue",}, "link": { "highlightColor": "lightblue",}, }

    config = Config(width=500, height=500, directed=True )
    return_value = agraph(nodes=nodes, edges=edges, config=config)

    # st.write(return_value)
    # st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
