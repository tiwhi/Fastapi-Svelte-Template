<script>
    export let content_location;
</script>

{#if content_location === 'Content'}
<p># Landing page content goes here</p>
{:else if content_location === 'LeftSidebar'}
    <p># Landing page content goes here</p>
{:else if content_location === 'RightSidebar'}
    <p># Landing page content goes here</p>
{/if }