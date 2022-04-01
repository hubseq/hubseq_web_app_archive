'use strict';
import React from "react";
import ReactDOM from "react-dom";
import {getApiClient} from "../api";
import TeamApplication from "./App";

const domContainer = document.querySelector('#team-content');
const apiUrls = JSON.parse(document.getElementById('api-urls').textContent);
const user = JSON.parse(document.getElementById('user-details').textContent);

domContainer ? ReactDOM.render(
  <TeamApplication
    client={getApiClient()}
    urlBase={urlBase}
    apiUrls={apiUrls}
    user={user}
  />,
  domContainer) : null;
