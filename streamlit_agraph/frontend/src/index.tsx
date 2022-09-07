import React from "react"
import ReactDOM from "react-dom"
import { StreamlitProvider } from "streamlit-component-lib-react-hooks"
import StreamlitVisGraph from "./StreamlitVisGraph"


ReactDOM.render(
  <React.StrictMode>
    <StreamlitProvider>
      <StreamlitVisGraph/>
    </StreamlitProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
