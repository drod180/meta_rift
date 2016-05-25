import React from 'react';
import { connect } from 'react-redux';
import Champ from '../components/champ';
import Details from '../components/details';

export default function Single() {
  return (
    <div>
			<section className="top-champ">
	      <Champ />
				<Details />
			</section>

			<section className="weak-champs">
	      <Champ />
				<Details />

				<Champ />
				<Details />

				<Champ />
				<Details />
			</section>

			<section className="strong-champs">
	      <Champ />
				<Details />

				<Champ />
				<Details />

				<Champ />
				<Details />
			</section>
		</div>
	)
};
