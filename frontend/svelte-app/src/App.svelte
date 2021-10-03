<script>
	import Navbar from './components/Navbar.svelte';
	import RegisterForm from './components/RegisterForm.svelte';
	import LoginForm from './components/LoginForm.svelte';
	import Button from './shared/Button.svelte';
	import { auth_token, check_login_status, login, logout, logged_in, getUserInfo, username } from './stores/auth.js';
	import { onMount } from 'svelte';
	// Navigation Imports
	import Tabs from './components/Tabs.svelte';
	import Tab from './components/Tab.svelte';
	import ContentContainer from './layout/ContentContainer.svelte';
	import Content from './layout/Content.svelte';
	import LeftSidebar from './layout/LeftSidebar.svelte';
	import RightSidebar from './layout/Right_Sidebar.svelte';
	import { get } from 'svelte/store';


	// navigation 
	
	let selectedTab = '2';
	// $: console.log('selected tab id:', selectedTab)
	
	let activeNavItem = 'Home';
	
	const navItemChange = (e) => {
		activeNavItem = e.detail['label'];
		// console.log('e.detail:', e.detail)
		// console.log('activeNavItem', activeNavItem)
	};

	const handleRegister = (e) => {
		
		activeNavItem = 'Home';
	};

	const handleLogin = (e) => {
		
		activeNavItem = 'Home';
	};

	function testEndpointButtonHandler() {
		fetch('http://localhost:8000/api/v1/users/?skip=0&limit=100', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
					'Authorization': 'Bearer ' + $auth_token.access_token
                }
            })
		.then((response) => response.json())
		.then((data) => {
			// console.log('Success:', data);
		})
		.catch((error) => {
			// console.log('Error:', error);
		})
	}

	function testLocalStorageJWTHandler() {
		$auth_token = JSON.parse(localStorage.getItem('auth'))
		// console.log('test auth token from local storage:', $auth_token)
	}

	onMount(() => {
		$auth_token = JSON.parse(localStorage.getItem('auth'))
		check_login_status();
		// console.log('========== 123 auth_token is', $auth_token)
		if ($auth_token) {
			$username = getUserInfo($auth_token);
			// console.log('========== 123 username is', $username)
		}
	})
	
</script>

<div class="all">
	<Navbar {activeNavItem} on:navChange={navItemChange}/>
	<header></header>		
	<main>
		<div class="flex-parent">
			<div class="left-sidebar">
				<LeftSidebar {activeNavItem}/>
			</div>
			<div class="content">
				<Content {activeNavItem}
					on:add={handleLogin}
					on:register={handleRegister}
					on:logout={logout}
					on:testEndpointButton={testEndpointButtonHandler}
					on:testLocalStorage={testLocalStorageJWTHandler}
				/>
			</div>
			<!-- <button on:click={() => getUserInfo($auth_token)}>Test Get User Info</button> -->
			<div class="right-sidebar">
				<RightSidebar {activeNavItem}/>
			</div>
		</div>
	</main>
	
	<footer>Footer Content: {$username}</footer>
</div>
<style>
	:global(body) {
		/* this will apply to <body> */
		margin: 0;
		padding: 3px;
	}
	
	.all {
		display: grid;
		height: 100vh;
		grid-template-rows: auto 1fr auto;
		z-index: 5;
	}
	
	.flex-parent {
		display: flex;
		flex-wrap: wrap;
		height: 100%;
	}

	.left-sidebar {
		flex: 1 1 250px;
		/* border: 1px solid #ddd; */
		/* background: lightblue; */
		font-size: 2rem;
		border-right: 1px solid lightgrey;
		text-align: center;
	}

	.content {
		flex: 1 1 740px;
		/* border: 1px solid red; */
		/* background: coral; */
		font-size: 2rem;
		text-align: center;
		padding: 0.5em;
	}

	.right-sidebar {
		flex: 1 1 250px;
		/* border: 1px solid #ddd; */
		/* background: yellow; */
		border-left: 1px solid lightgrey;
		font-size: 2rem;
		text-align: center;
	}

	header {
		/* background: lightpink; */
		padding: 2rem;
		text-align: center;
		width: 100%;
	}

	footer {
		/* background: wheat; */
		padding: 2rem;
		text-align: center;
		border-top: 1px solid #ddd;
	}

	h1 {
		/* color: rgba(0, 0, 0, 0.8); */
		/* color: #2196f3; */
		/* color: #007BA3; */
		/* color: #00C1FF; */
		/* background: -webkit-linear-gradient(#eee, #333);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent; */ 
		background-image:linear-gradient(to right, #ff3e00, #009485); /* alt color: #00a9ff or fastapi green for blened color: #009485*/
		color:rgba(0, 0, 0, 0); -webkit-background-clip:text;
		background-clip:text;
		position:relative;
		z-index: -1;
		
		/* color: #ff3e00; */
		text-transform: uppercase;
		font-size: 3.5em;
		font-weight: 100;
	}
</style>