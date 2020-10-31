import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";
import React, { ReactNode } from "react";

import { Graph } from "react-d3-graph";

interface State {
  numClicks: number
}

/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class AgraphComponent extends StreamlitComponentBase<State> {
  public state = { numClicks: 0 }

  public render = (): ReactNode => {

    const data = JSON.parse(this.props.args["data"]);
    const config = JSON.parse(this.props.args["config"]);

// const config = {
//     nodeHighlightBehavior: true
// };

//     const config = {
//         nodeHighlightBehavior: nodeHighlightBehavior,
//         node: {
//             color: node_color,
//             size: node_size,
//             highlightStrokeColor:highlightStrokeColor,
//         },
//         link: {
//             highlightColor: highlightColor,
//         },
//   };

    const onClickGraph = function() {
        window.alert(`Clicked the graph background`);
    };

    const onClickNode = function(nodeId: any) {
        window.alert(`Clicked node ${nodeId}`);
    };

    const onDoubleClickNode = function(nodeId: any) {
        window.alert(`Double clicked node ${nodeId}`);
    };

    const onRightClickNode = function(event: any, nodeId: any) {
        window.alert(`Right clicked node ${nodeId}`);
    };

    const onMouseOverNode = function(nodeId: any) {
        window.alert(`Mouse over node ${nodeId}`);
    };

    const onMouseOutNode = function(nodeId: any) {
        window.alert(`Mouse out node ${nodeId}`);
    };

    const onClickLink = function(source: any, target: any) {
        window.alert(`Clicked link between ${source} and ${target}`);
    };

    const onRightClickLink = function(event: any, source: any, target: any) {
        window.alert(`Right clicked link between ${source} and ${target}`);
    };

    const onMouseOverLink = function(source: any, target: any) {
        window.alert(`Mouse over in link between ${source} and ${target}`);
    };

    const onMouseOutLink = function(source: any, target: any) {
        window.alert(`Mouse out link between ${source} and ${target}`);
    };

    const onNodePositionChange = function(nodeId: any, x: any, y: any) {
        window.alert(`Node ${nodeId} is moved to new position. New position is x= ${x} y= ${y}`);
    };

    return (
      <Graph
        id="graph-id"
        data={data}
        config={config}
        onClickNode={onClickNode}
        onDoubleClickNode={onDoubleClickNode}
        onRightClickNode={onRightClickNode}
        // onClickGraph={onClickGraph}
        onClickLink={onClickLink}
        onRightClickLink={onRightClickLink}
      />
    )
  }

  // private onClicked = (): void => {
  //   // Streamlit via `Streamlit.setComponentValue`.
  //   this.setState(
  //     prevState => ({ numClicks: prevState.numClicks + 1 }),
  //     () => Streamlit.setComponentValue(this.state.numClicks)
  //   )
  // }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(AgraphComponent)
