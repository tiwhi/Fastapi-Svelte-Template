<script>
	import ContentDisplay from "./ContentDisplay.svelte";
	export let activeNavItem;
	let content_location = 'Content'
</script>

<ContentDisplay {activeNavItem} {content_location}
    on:add
    on:register
    on:logout
    on:testEndpointButton
    on:testLocalStorage
/>