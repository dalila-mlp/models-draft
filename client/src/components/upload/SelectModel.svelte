<script lang="ts">
    import { onMount } from 'svelte';
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    interface Option {
        id: string;
        filename: string;
    }

    export let options: Option[] = [];
    export let typeOption: string = "";
    export let value: string;
    export let specificValue: string | null = null;

    let showDropdown = false;
    let currentFilename: string = "Choose " + typeOption;

    function toggleDropdown() {
        showDropdown = !showDropdown;
    }

    function selectOption(option: Option) {
        currentFilename = option.filename;
        value = option.id;
        showDropdown = false;
        dispatch('select', option.id);
        dispatch('change', option.id);
    }

    onMount(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (!(event.target as HTMLElement).closest('.dropdown-container')) {
                showDropdown = false;
            }
        };

        document.addEventListener('click', handleClickOutside);

        return () => document.removeEventListener('click', handleClickOutside);
    });
</script>

<div class="dropdown-container relative inline-block text-left w-3/4">
    <button
        class="
            inline-flex
            w-full
            justify-center
            items-center
            rounded-lg
            shadow-sm
            py-[13px]
            bg-slate-700
            text-lg
            font-medium
            text-white
            hover:bg-gray-600
            focus:outline-none
        "
        type="button"
        on:click={toggleDropdown}
    >
        {specificValue ?? currentFilename}
        <svg class="absolute right-[21px] fill-current h-8 w-8 transform" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
    </button>
    {#if showDropdown}
        <div class="absolute right-0 mt-2 w-full rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-10">
            <ul class="text-gray-700" aria-labelledby="dropdownDefault">
                {#each options as option}
                    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
                    <!-- svelte-ignore a11y-click-events-have-key-events -->
                    <li
                        class="cursor-pointer px-4 py-2 hover:bg-gray-100 hover:rounded-md text-md"
                        on:click={() => selectOption(option)}
                    >
                        {option.filename}
                    </li>
                {/each}
            </ul>
        </div>
    {/if}
</div>

<style>
    .dropdown-container {
        position: relative;
    }
</style>
