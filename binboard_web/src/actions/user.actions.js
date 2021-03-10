import { userConstants } from "../constants/user.constants";
import { userServices } from "../services/user.services";

export const userActions = {
    login
}

function login(username, password) {
    return dispatch => {
        dispatch(request({ username }));

        userServices.login({ username, password })
            .then(
                user => {
                    dispatch(success(user));
                },
                error => {
                    dispatch(failure(error.toString()));
                }
            );
    };

    function request(user) { return { type: userConstants.LOGIN_REQUEST, user } }
    function success(user) { return { type: userConstants.LOGIN_SUCCESS, user } }
    function failure(user) { return { type: userConstants.LOGIN_FAILURE, user } }
}