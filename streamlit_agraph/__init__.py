import os
import csv
import json

from operator import itemgetter
import streamlit.components.v1 as components
import streamlit as st

from streamlit_agraph import data
from streamlit_agraph.config import Config
from streamlit_agraph.triple import Triple
from streamlit_agraph.node import Node
from streamlit_agraph.edge import Edge
from streamlit_agraph.triplestore import TripleStore

_RELEASE = True

if _RELEASE:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _agraph = components.declare_component("agraph", path=build_dir)
else:
    _agraph = components.declare_component(
        "agraph",
        url="http://localhost:3001",
    )
      
def agraph(nodes, edges, config):
    nodes_data = [ node.to_dict() for node in nodes]
    edges_data = [ edge.to_dict() for edge in edges]
    config_json = json.dumps(config.__dict__)
    data = { "nodes": nodes_data, "edges": edges_data}
    data_json = json.dumps(data)
    component_value = _agraph(data=data_json, config=config_json)
    return component_value

hierarchical = {
      "enabled":False,
      "levelSeparation": 150,
      "nodeSpacing": 100,
      "treeSpacing": 200,
      "blockShifting": True,
      "edgeMinimization": True,
      "parentCentralization": True,
      "direction": 'UD',        # UD, DU, LR, RL
      "sortMethod": 'hubsize',  # hubsize, directed
      "shakeTowards": 'leaves'  # roots, leaves
    }


if not _RELEASE:
    st.title("Streamlit Agraph 2.0")
    # nodes.append( Node(id="Spiderman", shape="circularImage", size=25, image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png"))
    # nodes.append( Node(id="Captain_Marvel", color="black", size=25, shape="circularImage", image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))
    # nodes.append( Node(id="Chris", color="white", size=25, shape="circularImage", image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_wolverine.png"))
    # edges.append( Edge(source="Captain_Marvel", target="Spiderman", label="friend_of") )
    # edges.append( Edge(source="Captain_Marvel", target="Chris", label="friend_of") )
    nodes, edges = data.load_graph_data()
    config = Config(width=750, height=750) # layout={"hierarchical":True} directed=True #
    return_value = agraph(nodes, edges, config=config)
    st.write(return_value)
