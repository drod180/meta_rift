
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { Router, browserHistory } from 'react-router';

import { configureStore } from './src/store';
import routes from './src/routes';

let state = window.__initialState__ || undefined;
const store = configureStore(browserHistory, state);

render(
  <Provider store={store}>
    <Router routes={routes} />
  </Provider>,
  document.getElementById('root')
);
