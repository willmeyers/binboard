import { userConstants } from "../constants/user.constants";

export function signup(state = {}, action) {
    switch (action.type) {
        case userConstants.SIGNUP_REQUEST:
            return { signingup: true };
        case userConstants.SIGNUP_SUCCESS:
            return {};
        case userConstants.SIGNUP_FAILURE:
            return {};
        default:
            return state;
    }
}