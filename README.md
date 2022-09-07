
Based on [react-graph-vis](https://github.com/crubier/react-graph-vis)


## Install

`pip install streamlit-agraph`

## Example App 
Check out the example [App](https://chrisdelclea-word-knowledge-graph-main-luylof.streamlitapp.com)!
## Use
```python
import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
nodes.append( Node(id="Spiderman", 
                   label="Peter Parker", 
                   size=25, 
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   size=25,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

config = Config(width=500, 
                height=500, 
                # **kwargs
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)

```

You may also want to use the TripleStore (untested & incomplete - yet): 

```python
# Currently not workin since update to agraph 2.0 - work in progress
from rdflib import Graph
from streamlit_agraph import TripleStore, agraph

graph = Graph()
graph.parse("http://www.w3.org/People/Berners-Lee/card")
store = TripleStore()

for subj, pred, obj in graph:
    store.add_triple(subj, pred, obj, "")
    
agraph(list(store.getNodes()), list(store.getEdges()), config)
```

Also graph algos can dirctly supported via the networkx API (untested & incomplete - yet):
```python
from streamlit_agraph import GraphAlgos

algos = GraphAlgos(store)
algos.shortest_path("Spiderman", "Captain_Marvel")
algos.density()
```

Formating the graph with hierachies is also possible, see `examples/iris_decision_tree.py`:

![marvel.png](imgs/marvel.png)



