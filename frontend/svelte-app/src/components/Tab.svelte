<script>
    import { getContext, onDestroy } from "svelte";
    export let title;
    export let id;
    
    let selectedTab = getContext('selectedTab');
    const tabTitles = getContext('tabTitles');

    $: tabTitles.updateTitle(id, title);

    tabTitles.registerTab(id, title);

    onDestroy(() => {
        tabTitles.unregisterTab(id);
    });
</script>

<div>
    {#if $selectedTab === id}
        <slot />
    {/if }
</div>