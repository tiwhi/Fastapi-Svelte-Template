<script>
    export let type = 'primary';
    export let flat = false;
    export let inverse = false;
</script>

<button class={type} class:flat={flat} class:inverse={inverse} on:click>
    <slot>

    </slot>
</button>

<style>
    button{
        border: 0;
        cursor: pointer;
        border-radius: 3px;
        padding: 0px, 20px;
        font-weight: 225;
        box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    }
    .primary{
        background: #ff3e00;
        padding: 3px 15px 5px 15px;
        color: white;
    }
    .secondary{
        background: #00a9ff;
        padding: 3px 15px 5px 15px;
        color: white;
    }
    .tertiary{
        background: rgba(0, 0, 0, 0.8);;
        color: white;
        outline: none;
        
        border: none;
        padding: 3px 15px 5px 15px;
        margin: 0;
        font-family: inherit;
        font-size: 24px;
        font-weight: 500;
        
    }
    .flat{
        box-shadow: none;
    }
    .primary.inverse{
        background: white;
        color: #d91b42;
        border: 2px solid #d91b42;
    }
    .secondary.inverse{
        background: white;
        color: #45c496;
        border: 2px solid #45c496;
    }
</style>