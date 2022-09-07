# React graph vis

A React component to display beautiful network graphs using vis.js

Show, don't tell: [Demo](https://wokstym.github.io/react-vis-graph-wrapper/)

Make sure to visit [visjs.org](http://visjs.org) for more info.

Rendered graphs are scrollable, zoomable, retina ready, dynamic, and switch layout on double click.

This package is a complete rewrite of [react-graph-vis](https://github.com/crubier/react-graph-vis) started by 
[ZachHaber](https://github.com/ZachHaber) in this [gist](https://gist.github.com/ZachHaber/feb0432fe395a303a4f10671877e5e70) mentioned somewhere deep in issues. 
Component is rewriten to function component for strict mode compliance and typing support is added (currently no types for specific GraphEvents - feel free to contribute)
There was also added additional support for resizing windows.

![A graph rendered by vis js](https://raw.githubusercontent.com/Wokstym/react-vis-graph-wrapper/master/example.png)

Due to the imperative nature of vis.js, updating graph properties causes complete redraw of graph and completely porting it to React is a big project itself!

This component takes three vis.js configuration objects as properties:  

- graph: contains two arrays { edges, nodes }
- options: normal vis.js options as described [here](http://visjs.org/docs/network/#options)
- events: an object that has [event name](http://visjs.org/docs/network/#Events) as keys and their callback as values

# Usage

```javascript
import React from 'react';
import './App.css';

import VisGraph, {
  GraphData,
  GraphEvents,
  Options,
} from 'react-vis-graph-wrapper';

function App() {
  const graph: GraphData = {
    nodes: [
      { id: 1, label: 'Node 1', title: 'node 1 tootip text' },
      { id: 2, label: 'Node 2', title: 'node 2 tootip text' },
      { id: 3, label: 'Node 3', title: 'node 3 tootip text' },
      { id: 4, label: 'Node 4', title: 'node 4 tootip text' },
      { id: 5, label: 'Node 5', title: 'node 5 tootip text' },
    ],
    edges: [
      { from: 1, to: 2 },
      { from: 1, to: 3 },
      { from: 2, to: 4 },
      { from: 2, to: 5 },
    ],
  };

  const options: Options = {
    layout: {
      hierarchical: true,
    },
    edges: {
      color: '#000000',
    },
    height: '500px',
  };

  const events: GraphEvents = {
    select: (event: any) => {
      const { nodes, edges } = event;
      console.log(nodes, edges);
    },
  };
  return (
    <VisGraph
      graph={graph}
      options={options}
      events={events}
      getNetwork={(network: any) => {
        //  if you want access to vis.js network api you can set the state in a parent component using this property
        console.log(network);
      }}
    />
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);

```











You can also check out the demo in the [`example`](https://github.com/Wokstym/react-vis-graph-wrapper/tree/master/example) folder.