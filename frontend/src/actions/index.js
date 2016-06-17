export const showMainChamp = (id) => ({
  type: 'SHOW_MAIN_CHAMP',
  mainChampId: id,
});

export const addTopChamps = (ids) => ({
  type: 'SHOW_TOP_CHAMPIONS',
  topChampIds: ids,
});

export const showCounterChamps = (ids) => ({
  type: 'SHOW_COUNTER_CHAMPS',
  counterChampIds: ids,
});

export const showCounteredChamps = (ids) => ({
  type: 'SHOW_COUNTERED_CHAMPS',
  counteredChampIds: ids,
});

export const showAllChamps = (ids) => ({
  type: 'SHOW_ALL_CHAMPS',
  allChamps: ids,
});
