
Based on [react-d3-graph](https://www.npmjs.com/package/react-d3-graph)


## Install

`pip install streamlit-agraph`

## Use
```python
import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") )
nodes.append( Node(id="Captain_Marvel", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") )
edges.append( Edge(source="Captain_Marvel", target="Spiderman", type="CURVE_SMOOTH") )

config = Config(width=500, 
                height=500, 
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                directed=True, 
                collapsible=True,
                # coming soon (set for all): node_size=1000, node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

```

![](https://github.com/ChrisChross/streamlit-agraph/blob/master/imgs/example.png)

![](https://github.com/ChrisChross/streamlit-agraph/blob/master/imgs/example2.png)

![](https://github.com/ChrisChross/streamlit-agraph/blob/master/imgs/example3.png)

