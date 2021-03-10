import { useState } from "react";
import { connect } from "react-redux";

import { userActions } from "../actions/user.actions";

function LoginForm(props) {
    const [form, setForm] = useState({
        username: '',
        password: ''
    });

    function handleSubmit(e) {
        e.preventDefault();
        console.log(form)
        props.login(form.username, form.password);
    }

    function handleChange(e) {
        setForm(prev => ({
            ...prev,
            [e.target.name]: e.target.value
        }))
    }

    return (
        <form onSubmit={handleSubmit}>
            <label>username</label>
            <input type="text" name="username" onChange={handleChange} />
            <label>password</label>
            <input type="password" name="password" onChange={handleChange} />
            <button type="submit">Login</button>
        </form>
    );
}

function mapState(state) {
    const { loggingIn } = state.authentication;
    return { loggingIn };
}

const actionCreators = {
    login: userActions.login
}

const ConnectedLoginForm = connect(mapState, actionCreators)(LoginForm);

export default ConnectedLoginForm;