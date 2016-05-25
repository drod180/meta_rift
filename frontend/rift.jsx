import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
// import { Router, browserHistory } from 'react-router';
// import routes from './src/routes';
import { createStore } from 'redux';
import reducers from './src/reducers';

import App from './src/containers/app';
let store = createStore(reducers);

document.addEventListener('DOMContentLoaded', () => {
	render(
	  <Provider store={store}>
	    <App />
	  </Provider>,
	  document.getElementById('root')
	);
});
