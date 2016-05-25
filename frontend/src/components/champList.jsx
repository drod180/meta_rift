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
)

export default ChampList;
