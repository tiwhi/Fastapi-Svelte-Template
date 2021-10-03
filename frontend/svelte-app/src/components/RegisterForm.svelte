<script>
    import Button from '../shared/Button.svelte';
    import { createEventDispatcher } from 'svelte';
    import { login } from '../stores/auth';

    let fields = { full_name: '', username: '', password: ''};
    let errors = { full_name: '', username: '', password: ''}; 
    let valid = false; 

    let dispatch = createEventDispatcher();

    const submitHandler = () => {
        valid = true;
        
        // validate full name -> if the field is empty, generates an error
        if (fields.full_name.trim().length < 1) {
            valid = false;
            errors.full_name = 'Full Name cannot be empty'
        } else {
            errors.full_name = '';
        };

        // [TODO - Tim 10/2/21]: update validation to something more meaningful. Also, change 'username' to email?
        // validate email -> if the email is less than 3 characters it generates an error
        if (fields.username.trim().length < 3) {
            valid = false;
            errors.username = 'Must be a valid email address, e.g. myname@example.com'
        } else {
            errors.username = '';
        };

        // validate password -> if the field is empty, generates an error
        if (fields.password.trim().length < 1) {
            valid = false;
            errors.password = 'Password cannot be empty'
        } else {
            errors.password = '';
        };

        // add new user
        if (valid) {
            let user = {password: fields.password, email: fields.username, full_name: fields.full_name};
            // console.log(`Form valid. User: ${user}`);
            fetch('http://localhost:8000/api/v1/users/open', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(user),
            })
            .then((response) => response.json())
            .then((data) => {
                // console.log('Register Success:', data);
                login(fields)
            })
            .catch((error) => {
                // console.log('Error:', error);
            })
            dispatch('register');
        }

    }

</script>

<form on:submit|preventDefault={submitHandler}>
    <h4>Create Account</h4>
    <div class="form-field">
        <label for="full_name">Full Name:</label>
        <input type="text" id="full_name" bind:value={fields.full_name} placeholder="Full Name">
        <div class="errors">{ errors.username }</div>
    </div>
    <div class="form-field">
        <label for="email">Your Email:</label>
        <input type="email" id="email" bind:value={fields.username} placeholder="Email">
        <div class="errors">{ errors.username }</div>
    </div>
    <div class="form-field">
        <label for="password">Your Password:</label>
        <input type="password" id="password" bind:value={fields.password} placeholder="Password">
        <div class="errors">{ errors.password }</div>
    </div>
    <Button type="primary" flat={false}>Register</Button>
</form>

<style>
    .form {
        background-color: #ffffff;
        width: 500px;
        margin: 50px auto 10px auto;
        padding: 30px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 10px -3px #333;
        text-align: center;
    }
    form {
        background-color: #ffffff;
        width: 400px;
        /* margin: 0 auto; */
        margin: 50px auto 10px auto;
        padding: 30px;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 10px -3px #333;
        text-align: center;
    }
    .form-field{
        margin: 18px auto;
    }
    input {
        width: 100%;
        border-radius: 6px;
        border: 1px solid #D9D9D9;
        outline: none;
        display: block;
        margin: 20px auto 20px auto;
    }
    label {
        margin: 10px auto;
        text-align: left;
    }
    .errors {
        color: red;
        font-weight: bold;
        font-size: 16px;
    }
    h4 {
		/* color: rgba(0, 0, 0, 0.8); */
		/* color: #2196f3; */
		/* color: #007BA3; */
		/* color: #00C1FF; */
        color: #00a9ff;
		text-transform: uppercase;
		font-size: 1.5em;
		font-weight: 100;
        margin-top: 0;
        margin-bottom: 0;
	}
</style>