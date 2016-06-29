import React from 'react';
import { Route, IndexRoute } from 'react-router';

/* components */
import MainPage from './components/mainPage';


const routes = (
  <Route path="/" component={MainPage} >
    <IndexRoute component={MainPage} />
  </Route>
);

export default routes;
