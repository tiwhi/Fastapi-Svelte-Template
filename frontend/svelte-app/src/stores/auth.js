import { writable, get } from 'svelte/store';

export let auth_token = writable('');

export let logged_in = writable(false);

export let username = writable();

export async function getUserInfo (token) {
    if (!token) {
        // console.log('from getUserInfo fuctnion: you are not logged in')
        // [TODO Tim - 10/2/21]: either make the function only fire when the user is logged in and remove the conditional, or put in a helpful error message 
    }
    else {
        let response = await fetch('http://localhost:8000/api/v1/users/me', {
            method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + token.access_token
                    }
                })
        let data = await response.json();
        // console.log('ABC this is a test of the get user info function', data)
        // console.log('123 --- testing how to access name from data, first name is', data.full_name.split(' ')[0])
        
        // console.log('===== Username is', get(username))
        username.set(data.full_name.split(' ')[0]);
        return data.full_name.split(' ')[0]
    }
    
}

export async function login (fields) {
    let valid = true;
    // console.log('XYZ this is the value of the fields argument', fields)
    if (valid) {
        // console.log('valid credentials')
        const formData = new FormData();
        formData.append('username', fields.username)
        formData.append('password', fields.password)
        let user = {username: fields.username, password: fields.password};
        // console.log(`Form valid. User: ${user}`);
        // console.log('submitHandler was sent:', user)
        fetch('http://localhost:8000/api/v1/token', {
            method: 'POST',
            
            body: formData,
        })
        .then((response) => response.json())
        .then((data) => {
            auth_token.set(data)
            localStorage.setItem('auth', JSON.stringify(get(auth_token)))
            logged_in.set(true);

            // console.log('XYZ current value of logged_in datastore after login function is', get(logged_in))
            // console.log('Success:', get(auth_token));
            // console.log('testing local storage persistence:', localStorage.getItem('auth'))
            $username = getUserInfo(get(auth_token));
            // console.log('========== 123 username is', $username)
        })
        .catch((error) => {
            // console.log('Error:', error);
        })}};

export async function check_login_status () {
    let token = JSON.parse(localStorage.getItem('auth'));
    if (!token) {
        // console.log('ALERT: you need to enter your username and password');
        logged_in.set(false);
        // console.log('123 Logged in status is', get(logged_in))
    }
    else {
        let response = await fetch('http://localhost:8000/api/v1/verify_token', {
            method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': 'Bearer ' + token.access_token
                    }
                })
        // console.log('XYZ response: ', response)
        
        
        if (response.status === 403) {
            // console.log('invalid token!')
            localStorage.removeItem('auth')
            auth_token.set('')
            // console.log('local storage token:', JSON.parse(localStorage.getItem('auth')))
        }
        let data = await response.json()
        // console.log('XYZ data from login() is', data)
        logged_in.set(true);
        auth_token.set(JSON.parse(localStorage.getItem('auth')));
        // console.log('XYZ current value of logged_in datastore after login function is', get(logged_in))
        // console.log('XYZ new test current value of auth_token is', get(auth_token))
	    }
    }


export const logout = () => {
    logged_in.set(false)
    localStorage.removeItem('auth')
    username.set('');
    auth_token.set('')
    // console.log('logged out, value of logged_in is', get(logged_in))
};