import React from 'react';
import { connect } from 'react-redux';

function App() {
  return (
    <div>
      <p>
        Hello World
      </p>
    </div>
  );
}

module.exports = connect(
  null
)(App);
