import logo from './logo.svg';
import './App.css';
import {React, useEffect} from 'react'
import { saveAs } from 'file-saver';

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

  const test = async () => {

        await fetch(`https://test-fawn-mu.vercel.app/get_file`)
        //await fetch(`http://localhost:8080/api/v1/get_file`,
        .then(response =>
            response.blob())
        .then(myBlob =>
            saveAs(myBlob,'test.py'))
        .catch(error => {
            console.log(error)
        });

};

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>

        <button onClick={test}>TEST</button>

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
