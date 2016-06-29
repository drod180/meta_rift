import React from 'react';
import MainChamp from '../containers/mainChamp';
import TriChamps from '../containers/triChamps';

export default function MainPage() {
  return (
    <div>
      <MainChamp />
      <TriChamps />
      <TriChamps />
      <TriChamps />
    </div>
  );
}
