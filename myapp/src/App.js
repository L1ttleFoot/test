import logo from './logo.svg';
import './App.css';
import {React, useEffect} from 'react'

function App() {

  useEffect(
        () => {
            fetch(`https://test-fawn-mu.vercel.app/`)
            .then(response=>response.json())
            .then(data=>console.log(data))
        },
        [],
    );

    useEffect(
      () => {
          fetch(`https://test-fawn-mu.vercel.app/portfolio`,
          {method: 'POST',
            body: JSON.stringify({
            'a':12
            })
          })
          .then(response=>response.json())
          .then(data=>console.log(data))
      },
      [],
  );

    


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
