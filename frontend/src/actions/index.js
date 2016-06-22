export const Show-MainChamp = (id) => ({
  type: 'SHOW_MAIN_CHAMP',
  mainChampId: id,
});

export const Add-TopChamps = (ids) => ({
  type: 'SHOW_TOP_CHAMPIONS',
  topChampIds: ids,
});

export const Show-CounterChamps = (ids) => ({
  type: 'SHOW_COUNTER_CHAMPS',
  counterChampIds: ids,
});

export const Show-CounteredChamps = (ids) => ({
  type: 'SHOW_COUNTERED_CHAMPS',
  counteredChampIds: ids,
});

export const Show-AllChamps = (ids) => ({
  type: 'SHOW_ALL_CHAMPS',
  allChamps: ids,
});
