<script>
    export let content_location;
</script>

{#if content_location === 'Content'}
    <p># Search content goes here</p>
    
{:else if content_location === 'LeftSidebar'}
    <p># Search content goes here</p>
    
{:else if content_location === 'RightSidebar'}
    <p># Search content goes here</p>
    
{/if }