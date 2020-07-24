import React from "react"

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
    return(
      <h4>{this.state.data}</h4>
    )
  }
}

export default Graphs
