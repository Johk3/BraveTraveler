import React from "react"
import CanvasJSReact from "../canvasjs.react"


class Graphs extends React.Component {
  state = {
    data: "",
  }

  constructor() {
    super()
  }

  componentDidMount() {
    this.fetchData()
    this.interval = setInterval(() => {
      this.fetchData()
    }, 5000)
  }

  componentWillUnmount() {
    clearInterval(this.interval)
  }

  fetchData() {
    fetch("https://api.chucknorris.io/jokes/random")
      .then(res => {
        return res.json()
      })
      .then(res => {
        this.setState({
          data: res.value
        })
      })
  }

  render() {
    var CanvasJSChart = CanvasJSReact.CanvasJSChart;
    var dps = []
    dps.push({x: 1,y: 1});	

    return(
      <div>
        <h4>{this.state.data}</h4>
        <CanvasJSChart options={dps}/>
      </div>
    )
  }
}

export default Graphs
