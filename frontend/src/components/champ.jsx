import React, { PropTypes } from 'react';

const Champ = ({ onClick, imgURI, thumb }) => (
  <div onClick={onClick} className={thumb ? 'thumb' : 'full'}>
    <img src={imgURI} alt="" />
  </div>
);

Champ.propTypes = {
  onClick: PropTypes.func.isRequired,
  imgURI: PropTypes.string.isRequired,
  thumb: PropTypes.bool.isRequired,
};

export default Champ;
