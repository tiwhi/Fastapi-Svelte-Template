<script>
    import { setContext } from 'svelte';
    import { writable } from 'svelte/store';
    import { onMount } from "svelte";

    // Tab formatting 
    export let selectedTab = '1';
    let selectedTabStore = writable(selectedTab);

    $: $selectedTabStore = selectedTab;
    $: updateProps($selectedTabStore);

    function updateProps(value) {
        selectedTab = value
    };

    setContext('selectedTab', selectedTabStore);

    let titles = [];
    setContext('tabTitles', {
        registerTab(id, title) {
            titles.push({ id, title });
            titles = titles;
        },
        updateTitle(id, title) {
            const tabIndex = titles.findIndex(title => title.id === id);
            titles[tabIndex].title = title; 
        },
        unregisterTab(id) {
            const tabIndex = titles.findIndex(title => title.id === id);
            if (tabIndex > -1) {
                titles.splice(tabIndex, 1);
                titles = titles; 
            }
        }
    })

    // Managing Mobile:
    // Show mobile icon and display menu
    let showMobileMenu = false;

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
      mediaListener.addListener(mediaQueryHandler);
    });
</script>

<nav>
    <div class="inner">
        <div on:click={handleMobileIconClick} class={`mobile-icon${showMobileMenu ? ' active' : ''}`}>
            <div class="middle-line"></div>
        </div>
        <div class={`navbar-list ${showMobileMenu ? ' mobile' : ''}`}>
            {#each titles as { id, title }}
                <li class:selected={$selectedTabStore === id}>
                    <button
                    on:click={() => { $selectedTabStore = id }}>
                        {title}
                    </button>
                </li>
            {/each }
        </div>      
    </div>
</nav>

<slot {selectedTab} />

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

    /* .selected {
        color: #fff;
        border-bottom: 2px solid #fff;
        padding-bottom: 8px;
    } */
    
    .inner {
        max-width: 980px;
        padding-left: 20px;
        padding-right: 20px;
        padding-top: 10px;
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
        padding: 0px 40px;
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

    .navbar-list li.selected {
        color: #fff;
		border-bottom: 2px solid #fff;
    }

    .navbar-list li:hover {
        opacity: 0.6;
    }
  
    .navbar-list button {
        background-color: rgba(0, 0, 0, 0.0);
        color: #fff;
        border: none;
        text-decoration: none;
        display: flex;
        height: 20px;
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
  
      .navbar-list button {
        display: inline-flex;
      }
    }
</style>