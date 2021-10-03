<script>
    export let content_location;
</script>

{#if content_location === 'Content'}
    <p># Product content goes here</p>
    
{:else if content_location === 'LeftSidebar'}
    <p># Product content goes here</p>
    
{:else if content_location === 'RightSidebar'}
    <p># Product content goes here</p>
    
{/if }