import json
from streamlit_agraph.node import Node
from streamlit_agraph.edge import Edge

def load_graph_data():
    nodes = []
    edges = []
    with open("./data/marvel.json", encoding="utf8") as f:
        marvel_file = json.loads(f.read())
        nodes.append(
            Node(id=marvel_file["name"],
                 label=marvel_file["name"],
                 shape="circularImage",
                 image=marvel_file["img"])
        )
        for sub_graph in marvel_file["children"]:
            nodes.append(Node(id=sub_graph["name"]))
            edges.append(Edge(source=sub_graph["name"], target=marvel_file["name"], label="subgroup_of"))
            for node in sub_graph["children"]:
                nodes.append(Node(id=node["hero"],
                                  title=node["link"],
                                  shape="circularImage",
                                  image=node["img"],
                                  group=sub_graph["name"],
                                  )
                             )
                edges.append(Edge(source=node["hero"], target=sub_graph["name"], label="blongs_to"))
    return nodes, edges
