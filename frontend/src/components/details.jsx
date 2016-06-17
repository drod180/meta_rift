import React, { PropTypes } from 'react';

const Details = ({ onClick, score, name }) => (
  <div
    onClick={onClick}
  >
    <p>{name}</p>
    <p>{score}</p>
  </div>
);

Details.propTypes = {
  onClick: PropTypes.func.isRequired,
  score: PropTypes.number.isRequired,
  name: PropTypes.string.isRequired,
};

export default Details;
