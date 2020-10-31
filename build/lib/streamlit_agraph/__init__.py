import os
import streamlit.components.v1 as components
import json


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



def agraph(nodes, edges, nodeHighlightBehavior="true", node_color="lightreen", node_size=120, highlightStrokeColor="blue", highlightColor="lightblue", key=None):

    nodes_data = [{"id": f"{node}"} for node in nodes]
    edges_data = [ {"source": f"{edge[0]}", "target": f"{edge[1]}"} for edge in edges]
    data = { "nodes": nodes_data, "links": edges_data }
    data_json = json.dumps(data)
    component_value = _agraph(data=data_json, nodeHighlightBehavior=nodeHighlightBehavior, node_color=node_color, node_size=node_size, highlightStrokeColor=highlightStrokeColor, highlightColor=highlightColor, key=key, default=0)

    return component_value

# app: `$ streamlit run agraph/__init__.py`
if not _RELEASE:
    import json
    import streamlit as st

    st.subheader("Component with constant args")

    nodes = ["Harry","Sally","Peter","Chris"]
    edges = [("Harry","Sally"),("Peter","Chris")]

    myConfig = { "nodeHighlightBehavior": "true", "node": { "color": "lightgreen", "size": 120, "highlightStrokeColor": "blue",}, "link": { "highlightColor": "lightblue",}, }

    return_value = agraph(nodes=nodes, edges=edges, nodeHighlightBehavior="true", node_color="#82E0AA", node_size=750, highlightStrokeColor="blue", highlightColor="lightblue" )

    # st.write(return_value)
    # st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
