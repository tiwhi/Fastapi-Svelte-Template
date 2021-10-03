<script>
    import BasicDataStore from '../stores/BasicDataStore.js';
    import ListElement from './ListElement.svelte';  
    import { fade, slide, scale } from 'svelte/transition';
    import { flip } from 'svelte/animate';
</script>

<div class="user-list">
    {#each $BasicDataStore as user (user.id)}
        <div in:fade out:scale|local animate:flip={{duration: 500}}>
            <ListElement {user} />
        </div>
    {/each}
</div>

<style>
    .user-list{
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 20px;
    }
</style>