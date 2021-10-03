<script>
	import ContentDisplay from "./ContentDisplay.svelte";
	export let activeNavItem;
	let content_location = 'RightSidebar'
</script>

Right Sidebar
<ContentDisplay {activeNavItem} {content_location}/>

<style>
    
</style>
