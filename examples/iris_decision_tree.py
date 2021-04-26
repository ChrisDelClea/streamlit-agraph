import json

import pygraphviz as pgv
import streamlit as st
from sklearn import tree
from sklearn.datasets import load_iris
from streamlit_agraph import Config, Edge, Node, agraph

with st.spinner("Loading iris dataset"):
    iris = load_iris()
    
with st.spinner("Train decision tree classifier"):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, 
                                out_file=None,
                                feature_names=iris.feature_names)  

G = pgv.AGraph().from_string(dot_data)


nodes = []
edges = []
for node in G.nodes():
    nodes.append(Node(id=node, 
                      label=node.attr['label'].split('\\n')[0], 
                      symbolType='square'))
for edge in G.edges():
        edges.append(
            Edge(source=edge[0],
                 target=edge[1], 
                type="STRAIGHT")
        )
        
layout = st.sidebar.selectbox('layout',['dot',
                                        'neato', 
                                        'circo', 
                                        'fdp', 
                                        'sfdp'])

rankdir = st.sidebar.selectbox("rankdir", ['BT', 'TB', 'LR', 'RL'])
ranksep = st.sidebar.slider("ranksep",min_value=0, max_value=10)
nodesep = st.sidebar.slider("nodesep",min_value=0, max_value=10)

config = Config(width=2000, 
                height=1000,
                graphviz_layout=layout,
                graphviz_config={"rankdir": rankdir, "ranksep": ranksep, "nodesep": nodesep},
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6",
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True},
                maxZoom=2,
                minZoom=0.1,
                staticGraphWithDragAndDrop=False,
                staticGraph=False,
                initialZoom=1
                ) 


return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

