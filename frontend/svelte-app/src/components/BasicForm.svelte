<script>
    import Button from '../shared/Button.svelte';
    import BasicDataStore from '../stores/BasicDataStore.js';
    import { createEventDispatcher } from 'svelte';

    let fields = { username: '', password: '', password2: ''};
    let errors = { username: '', password: '', password2: ''}; 
    let valid = false; 

    let dispatch = createEventDispatcher();

    const submitHandler = () => {
        valid = true;
        
        // validate username -> if the username is less than 3 characters it generates an error
        if (fields.username.trim().length < 3) {
            valid = false;
            errors.username = 'Username must be at least 3 characters long'
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

        // validate password 2-> if the field does not match password, then throw an error
        if (fields.password2.trim() != fields.password.trim()) {
            valid = false;
            errors.password2 = 'Does not match Password 1'
        } else {
            errors.password2 = '';
        };

        // add new user
        if (valid) {
            let user = {username: fields.username, password: fields.password, id: Math.random()};
            // console.log(`Form valid. User: ${user}`);
            BasicDataStore.update((users) => {
                // console.log(`Datastore updated. User: ${user}`)
                return [user, ...users];
            })
            dispatch('add');
        }

    }

</script>

<form on:submit|preventDefault={submitHandler}>
    <div class="form-field">
        <label for="username">Username:</label>
        <input type="text" id="username" bind:value={fields.username}>
        <div class="errors">{ errors.username }</div>
    </div>
    <div class="form-field">
        <label for="password">Password 1:</label>
        <input type="password" id="password" bind:value={fields.password}>
        <div class="errors">{ errors.password }</div>
    </div>
    <div class="form-field">
        <label for="password2">Password 2:</label>
        <input type="password" id="password2" bind:value={fields.password2}>
        <div class="errors">{ errors.password2 }</div>
    </div>
    <Button type="secondary" flat={true}>Add User</Button>
</form>


<style>
    form{
        width: 400px;
        margin: 0 auto;
        text-align: center;
    }
    .form-field{
        margin: 18px auto;
    }
    input{
        width: 100%;
        border-radius: 6px;
    }
    label{
        margin: 10px auto;
        text-align: left;
    }
    .errors{
        color: red;
        font-weight: bold;
        font-size: 16px;
    }
</style>