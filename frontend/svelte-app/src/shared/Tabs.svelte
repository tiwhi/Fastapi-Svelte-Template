<script>
    import { createEventDispatcher } from 'svelte';

    // create custom event dispatcher to use in passing on:click event up to parent component 
    const dispatch = createEventDispatcher();

    export let tabs;
    export let activeTab;
</script>

<div class="tabs"></div>
    <ul>
        {#each tabs as tab}
            <li on:click={() => dispatch('tabChange', tab)}>
                <div class:active={tab === activeTab}>{tab}</div>
            </li>
        {/each}
    </ul>
<style>
    .tabs{
        margin-bottom: 40px; 
    }
    ul{
        display: flex;
        justify-content: center;
        padding:0;
        list-style-type: none;
    }
    li{
        margin: 0 16px;
        font-size: 18px;
        color: #555;
        cursor: pointer;
    }
    .active{
        color: #d91b42;
        border-bottom: 2px solid #d91b42;
        padding-bottom: 8px;
    }
</style>