import { get, set } from 'js-cookie';

export { Payments } from './payments';
export { Api } from './api';
export { Modals } from './web/modals';


// pass-through for Cookies API
export const Cookies = {
  get: get,
  set: set,
};
