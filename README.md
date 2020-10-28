

##Install

pip install streamlit-agraph

##Use
```python
import agraph
import streamlit

nodes = ["Harry","Sally","Peter","Chris"]`
edges = [("Harry","Sally"),("Peter","Chris")]

return_value = agraph(nodes=nodes,
                      edges=edges, 
                      nodeHighlightBehavior="true",
                      node_color="blue", node_size=1000,
                      highlightStrokeColor="blue",
                      highlightColor="lightblue" )
```


