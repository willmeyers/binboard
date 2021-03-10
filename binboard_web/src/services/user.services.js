import { config } from "../config";

export const userServices = {
    login,
    logout,
    signup
}

function login(username, password) {
    const reqOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(username, password)
    }

    console.log(reqOptions.body)

    return fetch(`${config.BASE_URL}token/`, reqOptions)
        .then(response => {
            const token = response.json()
                .then(token => {
                    const access = token.access;
                    const refresh = token.refresh;
                    localStorage.setItem('access', access);
                    localStorage.setItem('refresh', refresh);
                    
                    return access;
                });
        })
}

function logout() {
    localStorage.removeItem('token');
}

function signup(user) {
    const reqOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(user)
    }

    return fetch(`${config.BASE_URL}users/`, reqOptions)
        .then(response => {
            return response.json()        
        });
}