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

    const onClickGraph = function() {
    };

    const onClickNode = function(nodeId: any) {
      Streamlit.setComponentValue({"action": "onClickNode", "node": nodeId});
    };

    const onDoubleClickNode = function(nodeId: any) {
      // This doesn't seem to work
      Streamlit.setComponentValue({"action": "onDoubleClickNode", "node": nodeId});
    };

    const onRightClickNode = function(event: any, nodeId: any) {
      Streamlit.setComponentValue({"action": "onRightClickNode", "node": nodeId});
    };

    const onMouseOverNode = function(nodeId: any) {
    };

    const onMouseOutNode = function(nodeId: any) {
    };

    const onClickLink = function(source: any, target: any) {
        Streamlit.setComponentValue({"action": "onClickLink", "sourceNode": source, "targetNode":target});
    };

    const onRightClickLink = function(event: any, source: any, target: any) {
      Streamlit.setComponentValue({"action": "onRightClickLink", "sourceNode": source, "targetNode":target});
    };

    const onMouseOverLink = function(source: any, target: any) {
    };

    const onMouseOutLink = function(source: any, target: any) {
    };

    const onNodePositionChange = function(nodeId: any, x: any, y: any) {
      Streamlit.setComponentValue({"action": "onNodePositionChange", "node":nodeId , "x": x, "y":y});
    };

    return (
      <Graph
        id="graph-id"
        data={data}
        config={config}
        onClickNode={onClickNode}
        onDoubleClickNode={onDoubleClickNode}
        onRightClickNode={onRightClickNode}
        onClickLink={onClickLink}
        onRightClickLink={onRightClickLink}
      />
    )
  }
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(AgraphComponent)
