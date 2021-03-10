import { userConstants } from '../constants/user.constants';

let token = localStorage.getItem('token');
if (token) {
    token = JSON.parse(token);
}
const initialState = token ? { loggedIn: true, token } : {};

export function authentication(state = initialState, action) {
    switch (action.type) {
        case userConstants.LOGIN_REQUEST:
            return {
                loggedIn: true,
                token: action.token
            };
        case userConstants.LOGIN_SUCCESS:
            return {
                loggedIn: true,
                token: action.token
            };
        case userConstants.LOGIN_FAILURE:
            return {
                loggedIn: false
            };
        default:
            return state;
    }
}