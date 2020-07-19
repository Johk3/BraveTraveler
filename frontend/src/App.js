import React from 'react';
import logo from './logo.svg';
import CanvasJSReact from './canvasjs.react'
import './App.css';
import { Button } from '@material-ui/core';

var CanvasJSChart = CanvasJSReact.CanvasJSChart;


class App extends React.Component {
  state = {
    data: "",
    paused: false
  }

  constructor() {
    super();
    this.generateDataPoints = this.generateDataPoints.bind(this);
  }

  componentDidMount() {
    if (!this.state.paused){
    this.getData()
    this.interval = setInterval(() => {
      this.getData()
    }, 5000)
    }
  }

  componentWillUnmount() {
    clearInterval(this.interval)
  }

  getData() {
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

  generateDataPoints(noOfDps) {
    var xVal = 1, yVal = 100;
    var dps = [];
    for(var i = 0; i < noOfDps; i++) {
      yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
      dps.push({x: xVal,y: yVal});	
      xVal++;
    }
    return dps;
  }

  pauseStart() {
    if(this.state.paused){
      this.state.paused = false
    } else {
      this.state.paused = true
    }
  }

  render() {
    const options = {
      theme: "dark1", // "light1", "dark1", "dark2"
      animationEnabled: true,
      zoomEnabled: true,
      title: {
        text: "Audio Interception",
      },
      axisY: {
        includeZero: false,
        title: "Decibels",
      },
      axisX: {
        title: "Iterations",
      },
      data: [{
        type: "area",
        dataPoints: this.generateDataPoints(500),
      }]
    }

    return(
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          BraveTraveler - Monitoring
        </h1>
        <p>{this.state.data}</p>
        <Button onClick={this.pauseStart} color="secondary" variant="contained">PAUSE</Button>
        <CanvasJSChart options={options}/>
        <CanvasJSChart options={options}/>
        <CanvasJSChart options={options}/>
        <CanvasJSChart options={options}/>
      </header>
    </div>
    )
  }
}

export default App;
