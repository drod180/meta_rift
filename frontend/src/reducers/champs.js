export default function champs(state = [], action) {
  switch (action.type) {
    case 'SHOW_MAIN_CHAMP':
      return {
        id: action.id,
      };
    case 'SHOW_TOP_CHAMPIONS':
      return {
        id: action.ids,
      };
    case 'SHOW_COUNTER_CHAMPS':
      return {
        id: action.ids,
      };
    case 'SHOW_COUNTERED_CHAMPS':
      return {
        id: action.ids,
      };
    case 'SHOW_ALL_CHAMPS':
      return {
        id: action.ids,
      };
    default:
      return state;
  }
}
