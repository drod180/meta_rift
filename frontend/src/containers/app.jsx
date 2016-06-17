import React from 'react';
// import { connect } from 'react-redux';
import Champ from '../components/champ';
import Details from '../components/details';

export default function App() {
  return (
    <div>
      <Champ id={id} />
      <Details id={id} />
    </div>
  );
}
