<script>
	import ContentDisplay from "./ContentDisplay.svelte";
	export let activeNavItem;
	let content_location = 'LeftSidebar'
</script>

Left Sidebar
<ContentDisplay {activeNavItem} {content_location}/>

<style>
    
</style>