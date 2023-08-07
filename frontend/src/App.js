import React from 'react';
import Modal from 'react-modal';
import QuoteList from './QuoteList';
import './styles.css';

// Set the main application element (e.g., the root div with id="root")
Modal.setAppElement('#root');

const App = () => {
  return (
    <div className="App">
      <h1>QuoteMaster</h1>
      <QuoteList />
    </div>
  );
};

export default App;
