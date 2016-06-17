import React, { PropTypes } from 'react';
import Champ from './champ';

const ChampList = ({ champs, onChampClick }) => (
  <ul>
    {champs.map(champ =>
      <Champ
        key={champ.id}
        {...champ}
        onClick={() => onChampClick(champ.id)}
      />
    )}
  </ul>
);

ChampList.propTypes = {
  champs: PropTypes.number.isRequired,
  onChampClick: PropTypes.func.isRequired,
};

export default ChampList;
