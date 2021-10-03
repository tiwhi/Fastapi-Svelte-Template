<script>
    // imports
    import { onMount } from "svelte";
    import { createEventDispatcher } from 'svelte';
    import { auth_token, logout, logged_in, username } from '../stores/auth.js';

    // create custom event dispatcher to use in passing on:click event up to parent component 
    const dispatch = createEventDispatcher();
    
    export let activeNavItem;
  
    // Show mobile icon and display menu
    let showMobileMenu = false;
    
  $: if ($logged_in) {
    // console.log('=============== XYZ 123 Username is', $username)
    // console.log('=============== logged in!', $username)
    loggedInNavItems = [ 
      { id: 1, label: "logo", href: "#" },
      { id: 2, label: "Home", href: "#" },
      { id: 3, label: "Product", href: "#" },
      { id: 4, label: "Pricing", href: "#" },
      { id: 5, label: "Frequently Asked Questions", href: "#" },
      { id: 6, label: "Search", href: "#" },
      { id: 7, label: $username, href: "#" },
      { id: 8, label: "Logout", href: "#" },
    ]; 
  } else {
    // console.log('=============== NOT logged in!')
  }

    // List of navigation items
    let loggedInNavItems = [ 
      { id: 1, label: "logo", href: "#" },
      { id: 2, label: "Home", href: "#" },
      { id: 3, label: "Product", href: "#" },
      { id: 4, label: "Pricing", href: "#" },
      { id: 5, label: "Frequently Asked Questions", href: "#" },
      { id: 6, label: "Search", href: "#" },
      { id: 7, label: $username, href: "#" },
      { id: 8, label: "Logout", href: "#" },
    ];  

    // logged out items 
    let loggedOutNavItems = [ 
      { id: 1, label: "logo", href: "#" },
      { id: 2, label: "Home", href: "#" },
      { id: 3, label: "Product", href: "#" },
      { id: 4, label: "Pricing", href: "#" },
      { id: 5, label: "Frequently Asked Questions", href: "#" },
      { id: 6, label: "Search", href: "#" },
      { id: 7, label: "Login", href: "#" },
      { id: 8, label: "Register", href: "#" }
    ];

    // Mobile menu click event handler
    const handleMobileIconClick = () => (showMobileMenu = !showMobileMenu);

  
  
    // Media match query handler
    const mediaQueryHandler = e => {
      // Reset mobile state
      if (!e.matches) {
        showMobileMenu = false;
      }
    };
  
    // Attach media query listener on mount hook
    onMount(() => {
      const mediaListener = window.matchMedia("(max-width: 767px)");
      // console.log('This is a test of the logged_in store, its value is:', $logged_in)
      // console.log('GHJ This is a test of the username store, its value is:', $username)
      mediaListener.addListener(mediaQueryHandler);
    });

    function handleLogout () {
		  logout()
      dispatch('navChange', { label: "Home", href: "#" })
		  
      // console.log('active nav item:', activeNavItem)
	  };
  </script>
  
  <nav>
    <div class="inner">
      <div on:click={handleMobileIconClick} class={`mobile-icon${showMobileMenu ? ' active' : ''}`}>
        <div class="middle-line"></div>
      </div>
      <ul class={`navbar-list ${showMobileMenu ? ' mobile' : ''}`}>
        {#if $logged_in}
          {#each loggedInNavItems as item (item.id)}
            {#if item.label === 'Logout'}
              <li>
                <a
                class='nav-element'
                on:click={handleLogout}
                href={item.href}>
                    <div class:active={item.label === activeNavItem}>
                        {item.label}
                    </div>
                </a>
              </li>
            {:else }
              <li>
                <a
                class='nav-element'
                on:click={() => dispatch('navChange', item)}
                href={item.href}>
                    <div class:active={item.label === activeNavItem}>
                        {item.label}
                    </div>
                </a>
              </li>
            {/if }
          {/each}
        {:else }
          {#each loggedOutNavItems as item (item.id)}
            <li>
              <a
              class='nav-element'
              on:click={() => dispatch('navChange', item)}
              href={item.href}>
                  <div class:active={item.label === activeNavItem}>
                      {item.label}
                  </div>
              </a>
            </li>
          {/each}
        {/if }
             
      </ul>
    </div>
  </nav>
  
  <style>
    nav {
        background-color: rgba(0, 0, 0, 0.8);
        font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
        height: 45px;
        position: fixed;
        top: 5px;
        width: 100%;
        border-radius: 3px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    }

    .active{
        color: #fff;
        border-bottom: 2px solid #fff;
        padding-bottom: 8px;
    }
    
    .inner {
        max-width: 980px;
        padding-left: 20px;
        padding-right: 20px;
        margin: auto;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        height: 100%;
    }
  
    .mobile-icon {
        width: 25px;
        height: 14px;
        position: relative;
        cursor: pointer;
    }
  
    .mobile-icon:after,
    .mobile-icon:before,
    .middle-line {
        content: "";
        position: absolute;
        width: 100%;
        height: 2px;
        background-color: #fff;
        transition: all 0.4s;
        transform-origin: center;
    }
  
    .mobile-icon:before,
    .middle-line {
        top: 0;
    }
  
    .mobile-icon:after,
    .middle-line {
        bottom: 0;
    }
  
    .mobile-icon:before {
        width: 66%;
    }
  
    .mobile-icon:after {
        width: 33%;
    }
  
    .middle-line {
        margin: auto;
    }
  
    .mobile-icon:hover:before,
    .mobile-icon:hover:after,
    .mobile-icon.active:before,
    .mobile-icon.active:after,
    .mobile-icon.active .middle-line {
        width: 100%;
    }
  
    .mobile-icon.active:before,
    .mobile-icon.active:after {
        top: 50%;
        transform: rotate(-45deg);
    }
  
    .mobile-icon.active .middle-line {
        transform: rotate(45deg);
    }
  
    .navbar-list {
        display: none;
        width: 100%;
        justify-content: space-between;
        margin: 0;
        padding: 0 40px;
    }
  
    .navbar-list.mobile {
        background-color: rgba(0, 0, 0, 0.8);
        position: fixed;
        display: block;
        height: calc(100% - 45px);
        bottom: 0;
        left: 0;
    }
  
    .navbar-list li {
        list-style-type: none;
        position: relative;
    }

    .navbar-list li:hover {
        opacity: 0.6;
    }

    .navbar-list li:before {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 1px;
        background-color: #424245;
    }
  
    .navbar-list a {
        color: #fff;
        text-decoration: none;
        display: flex;
        height: 45px;
        align-items: center;
        padding: 0 10px;
        font-size: 13px;
    }
  
    @media only screen and (min-width: 767px) {
      .mobile-icon {
        display: none;
      }
  
      .navbar-list {
        display: flex;
        padding: 0;
      }
  
      .navbar-list a {
        display: inline-flex;
      }
    }
  </style>