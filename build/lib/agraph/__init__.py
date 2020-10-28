import os
import streamlit.components.v1 as components
import json

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_agraph", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _agraph = components.declare_component(
        # We give the component a simple, descriptive name ("agraph"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "agraph",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _agraph = components.declare_component("agraph", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def agraph(nodes, edges, nodeHighlightBehavior="true", node_color="lightreen", node_size=120, highlightStrokeColor="blue", highlightColor="lightblue", key=None):

    nodes_data = [{"id": f"{node}"} for node in nodes]
    edges_data = [ {"source": f"{edge[0]}", "target": f"{edge[1]}"} for edge in edges]
    data = { "nodes": nodes_data, "links": edges_data }
    data_json = json.dumps(data)
    component_value = _agraph(data=data_json, nodeHighlightBehavior=nodeHighlightBehavior, node_color=node_color, node_size=node_size, highlightStrokeColor=highlightStrokeColor, highlightColor=highlightColor, key=key, default=0)

    return component_value

# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run agraph/__init__.py`
if not _RELEASE:
    import json
    import streamlit as st

    st.subheader("Component with constant args")
    nodes = ["Harry","Sally","Peter","Chris"]
    edges = [("Harry","Sally"),("Peter","Chris")]

    myConfig = { "nodeHighlightBehavior": "true", "node": { "color": "lightgreen", "size": 120, "highlightStrokeColor": "blue",}, "link": { "highlightColor": "lightblue",}, }

    return_value = agraph(nodes=nodes, edges=edges, nodeHighlightBehavior="true", node_color="lightreen",node_size=120, highlightStrokeColor="blue", highlightColor="lightblue" )

    # st.write(return_value)
    # st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
