<script>
    import LoginForm from '../components/LoginForm.svelte';
    export let content_location;

</script>

{#if content_location === 'Content'}
    <LoginForm on:add />
{:else if content_location === 'LeftSidebar'}
    <p># Login content goes here</p>
{:else if content_location === 'RightSidebar'}
    <p># Login content goes here</p>
{/if }