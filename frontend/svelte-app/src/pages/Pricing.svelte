<script>
    export let content_location;
</script>

{#if content_location === 'Content'}
    <p># Pricing content goes here</p>
    
{:else if content_location === 'LeftSidebar'}
    <p># Pricing content goes here</p>

{:else if content_location === 'RightSidebar'}
    <p># Pricing content goes here</p>
    
{/if }