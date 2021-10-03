<script>
    import Button from '../shared/Button.svelte';
    // import BasicDataStore from '../stores/BasicDataStore.js';
    import { auth_token, login } from '../stores/auth.js';
    import { createEventDispatcher } from 'svelte';

    let fields = { username: '', password: ''};
    let errors = { username: '', password: ''}; 
    let valid = false; 

    let dispatch = createEventDispatcher();

    
    function submitHandler () {
        login(fields);
        dispatch('add');
    }
</script>

<form on:submit|preventDefault={submitHandler}>
    <h4>Login</h4>
    <div class="form-field">
        <label for="email">Email:</label>
        <input type="email" id="email" bind:value={fields.username} placeholder="Email">
        <div class="errors">{ errors.email }</div>
    </div>
    <div class="form-field">
        <label for="password">Password:</label>
        <input type="password" id="password" bind:value={fields.password} placeholder="Password">
        <div class="errors">{ errors.password }</div>
    </div>
    <Button type="secondary" flat={false}>Login</Button>
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
        color: #ff3e00;
		text-transform: uppercase;
		font-size: 1.5em;
		font-weight: 100;
        margin-top: 0;
        margin-bottom: 0;
	}
</style>