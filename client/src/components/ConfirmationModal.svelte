<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    export let message: string = "Are you sure?";
    export let onConfirm: () => void;
    export let onCancel: () => void;

    const dispatch = createEventDispatcher();

    function confirm() {
        onConfirm();
        dispatch("close");
    }

    function cancel() {
        onCancel();
        dispatch("close");
    }
</script>

<div class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-gray-900 bg-opacity-50 z-50">
    <div class="bg-slate-700 rounded-lg p-8">
        <p class="text-lg font-medium mb-4">{message}</p>
        <div class="flex justify-end">
            <button class="bg-red-500 hover:bg-red-700 text-white px-4 py-2 rounded mr-2" on:click={confirm}>Confirm</button>
            <button class="bg-gray-300 hover:bg-gray-400 text-slate-700 px-4 py-2 rounded" on:click={cancel}>Cancel</button>
        </div>
    </div>
</div>
