import React from 'react';
import logo from './logo.svg';
import './App.css';
import Typography from '@material-ui/core/Typography';
import Link from '@material-ui/core/Link';
import Graphs from './Components/Graphs';


function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://jastonmatter.com">
        JastonMatter
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  )
}

function App() {
    return(
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>
          BraveTraveler - Monitoring
        </h1>
        <Graphs/>
        <Copyright/>
      </header>
    </div>
    )
  }

export default App;
