<script>
    import Button from '../shared/Button.svelte';
    import { createEventDispatcher } from 'svelte';
    
    export let content_location;
    
    let dispatch = createEventDispatcher();

    const submitLoginHandler = () => {

        dispatch('login');
    }
    const submitLogoutHandler = () => {

        dispatch('logout');
    }
    const submitTestEndpointHandler = () => {

        dispatch('testEndpointButton');
    }
    const submitTestLocalStorageHandler = () => {

        dispatch('testLocalStorage');
    }
</script>

{#if content_location === 'Content'}
    <h1>Svelte / Fastapi</h1>
    <p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
    <p>Visit the <a href="https://fastapi.tiangolo.com/tutorial/first-steps/">FastAPI tutorial</a> to learn how to build FastAPI apps.</p>
    <!-- <Button on:click={submitTestEndpointHandler} type="primary" flat={false}>Test Endpoints</Button>
    <Button on:click={submitTestLocalStorageHandler} type="secondary" flat={false}>Test JWT Local Storage</Button>
    <Button on:click={submitLoginHandler} type="secondary" flat={true}>Test Login Function</Button>
    <Button on:click={submitLogoutHandler} type="primary" flat={true}>Test Logout Function</Button> -->
{:else if content_location === 'LeftSidebar'}
    <p># Home content goes here</p>
{:else if content_location === 'RightSidebar'}
    <p># Home content goes here</p>
{/if }

<style>
    h1 {
            /* color: rgba(0, 0, 0, 0.8); */
            /* color: #2196f3; */
            /* color: #007BA3; */
            /* color: #00C1FF; */
            /* background: -webkit-linear-gradient(#eee, #333);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent; */ 
            background-image:linear-gradient(to right, #ff3e00, #009485); /* alt color: #00a9ff or fastapi green for blened color: #009485*/
            color:rgba(0, 0, 0, 0); -webkit-background-clip:text;
            background-clip:text;
            position:relative;
            z-index: -1;
            
            /* color: #ff3e00; */
            text-transform: uppercase;
            font-size: 3.5em;
            font-weight: 100;
        }
</style>