import React from 'react';
import { Route, IndexRoute } from 'react-router';

/* container components */
import App from './containers/app';


const routes = (
  <Route path="/" component={App}>
    <IndexRoute component={App} />
  </Route>
);

export default routes;
