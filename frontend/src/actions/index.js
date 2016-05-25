export const addChamps = () => {
  return {
    type: 'SHOW_TOP_CHAMPIONS',
  }
}

export const addChamp = (id) => {
  return {
    type: 'SHOW_CHAMP',
    id: id,
  }
}

export const addWeak = (id) => {
  return {
    type: 'SHOW_CHAMPS_WEAK',
    id: id,
  }
}

export const addStrong = (id) => {
  return {
    type: 'SHOW_CHAMPS_STRONG',
    id: id,
  }
}

export const addAllChamps() => {
	return {
		type: 'SHOW_ALL_CHAMPS',
	}
}
