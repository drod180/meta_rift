import React from 'react';
// import { connect } from 'react-redux';
import Champ from '../components/champ';
import Details from '../components/details';

export default function App() {
  return (
    <div>
      <section className="main-champ">
        <Champ />
        <Details />
      </section>

      <section className="top-champs">
        <Champ />
        <Details />

        <Champ />
        <Details />

        <Champ />
        <Details />
      </section>

      <section className="counter-champs">
        <Champ />
        <Details />

        <Champ />
        <Details />

        <Champ />
        <Details />
      </section>

      <section className="countered-champs">
        <Champ />
        <Details />

        <Champ />
        <Details />

        <Champ />
        <Details />
      </section>
    </div>
  );
}
