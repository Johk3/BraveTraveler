import React from 'react';
import logo from './logo.svg';
import CanvasJSReact from './canvasjs.react'
import './App.css';

var CanvasJSChart = CanvasJSReact.CanvasJSChart;


class App extends React.Component {
  constructor() {
    super();
    this.generateDataPoints = this.generateDataPoints.bind(this);
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
        <div style={{columns: "2"}}>
          <CanvasJSChart options={options}/>
          <CanvasJSChart options={options}/>
          <CanvasJSChart options={options}/>
          <CanvasJSChart options={options}/>
        </div>
      </header>
    </div>
    )
  }
}

export default App;
