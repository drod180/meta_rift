export default function champs(state = [], action) {
  switch (action.type) {
		case 'SHOW_CHAMP':
      return {
        id: action.id,
      }
			break;
    case 'SHOW_TOP_CHAMPIONS':
      return {
        id: 1,
      }
			break;
    case 'SHOW_ALL_CHAMPS':
			return {
				id: 2,
			}
			break;
		case 'SHOW_CHAMPS_WEAK':
			return {
				id: action.id,
			}
			break;
		case 'SHOW_CHAMPS_STRONG':
			return {
				id: action.id,
			}
			break;
    default:
      return state
  }
}
