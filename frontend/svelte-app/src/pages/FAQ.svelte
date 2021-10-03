<script>
    export let content_location;
</script>

{#if content_location === 'Content'}
    <p># Frequently Asked Questions content goes here</p>
    
{:else if content_location === 'LeftSidebar'}
    <p># Frequently Asked Questions content goes here</p>

{:else if content_location === 'RightSidebar'}
    <p># Frequently Asked Questions content goes here</p>

{/if }