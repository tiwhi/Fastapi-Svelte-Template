<script>
    import { getContext, onDestroy } from "svelte";
    export let id;
    
    let selectedTab = getContext('selectedTab');
    const tabTitles = getContext('tabTitles');

</script>

<div>
    {#if $selectedTab === id}
        <slot />
    {/if }
</div>