import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  // constructor() {
  //   super();
  // }

  render() {
    return(
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          BraveTraveler - Monitoring
        </h1>
      </header>
    </div>
    )
  }
}

export default App;
