<script>
    import RegisterForm from '../components/RegisterForm.svelte';
    export let content_location;
</script>

{#if content_location === 'Content'}
    <RegisterForm on:register/>
{:else if content_location === 'LeftSidebar'}
    <p># Register content goes here</p>
{:else if content_location === 'RightSidebar'}
    <p># Register content goes here</p>
{/if }