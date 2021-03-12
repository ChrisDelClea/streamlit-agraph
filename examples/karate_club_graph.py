# karate_club_graph.py
# An example of basic and common interoperability between 
# streamlit-agraph and networkx.
#
# Use the following command to launch the app
# streamlit run <path-to-script>.py

import networkx as nx
from streamlit_agraph import agraph, Node, Edge, Config

# Generate the networkx implementation of Zachary's Karate Club graph
# (https://en.wikipedia.org/wiki/Zachary%27s_karate_club)
G = nx.karate_club_graph()

# Create the equivalent Node and Edge lists
nodes = [Node(id=i, label=str(i), size=200) for i in range(len(G.nodes))]
edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i,j) in G.edges]


config = Config(width=500, 
                height=500, 
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6",
                collapsible=True,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True}
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
