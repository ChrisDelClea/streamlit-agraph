
Based on [react-d3-graph](https://www.npmjs.com/package/react-d3-graph)


## Install

`pip install streamlit-agraph`

## Use
```python
import streamlit
from streamlit_agraph import agraph

nodes = ["Harry","Sally"]
edges = [("Harry","Sally")]

return_value = agraph(nodes=nodes,
                      edges=edges, 
                      nodeHighlightBehavior="true",
                      node_color="blue", node_size=1000,
                      highlightStrokeColor="blue",
                      highlightColor="lightblue" )
```

![](https://github.com/ChrisChross/streamlit-agraph/blob/master/imgs/example.png)

