<script>
    import Home from '../pages/Home.svelte';
	import Product from '../pages/Product.svelte';
	import Pricing from '../pages/Pricing.svelte';
	import FAQ from '../pages/FAQ.svelte';
	import Search from '../pages/Search.svelte';
	import Login from '../pages/Login.svelte';
	import Register from '../pages/Register.svelte';
	
	export let activeNavItem;
    export let content_location;
</script>

{#if activeNavItem === 'Home'}
	<Home {content_location}
        on:add
        on:logout
        on:testEndpointButton
        on:testLocalStorage/>
{:else if activeNavItem === 'Product'}
	<Product {content_location}/>
{:else if activeNavItem === 'Pricing'}
	<Pricing {content_location}/>
{:else if activeNavItem === 'Frequently Asked Questions'}
	<FAQ {content_location}/>
{:else if activeNavItem === 'Search'}
	<Search {content_location}/>
{:else if activeNavItem === 'Login'}
	<Login {content_location} on:add/>
{:else if activeNavItem === 'Register'}
	<Register {content_location} on:register/>
{/if }