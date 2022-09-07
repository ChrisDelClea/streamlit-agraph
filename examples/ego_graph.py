# ego_graph.py
# An example of how to plot a node's ego network 
# (egonet). This indirectly showcases slightly more involved 
# interoperability between streamlit-agraph and networkx.

# An egonet can be # created from (almost) any network (graph),
# and exemplifies the # concept of a subnetwork (subgraph):
# A node's egonet is the (sub)network comprised of the focal node 
# and all the nodes to whom it is adjacent. The edges included
# in the egonet are those nodes are both included in the aforementioned
# nodes. 

# Use the following command to launch the app
# streamlit run <path-to-script>.py

# standard library dependencies
from operator import itemgetter

# external dependencies
import networkx as nx
from streamlit_agraph import agraph, Node, Edge, Config

# First create a graph using the Barabasi-Albert model
n = 2000
m = 2
G = nx.generators.barabasi_albert_graph(n, m)

# Then find the node with the largest degree; 
# This node's egonet will be the focus of this example.
node_and_degree = G.degree()
most_connected_node = sorted(G.degree, key=lambda x: x[1], reverse=True)[0]
degree = G.degree(most_connected_node)

# Create egonet for the focal node
hub_ego = nx.ego_graph(G, most_connected_node[0])

# Now create the equivalent Node and Edge lists
nodes = [Node(id=i, label=str(i), size=200) for i in hub_ego.nodes]
edges = [Edge(source=i, target=j, type="CURVE_SMOOTH") for (i,j) in G.edges
        if i in hub_ego.nodes and j in hub_ego.nodes]


config = Config(width=500, 
                height=500, 
                directed=True,
                nodeHighlightBehavior=False, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=False,
                node={'labelProperty':'label'},
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
