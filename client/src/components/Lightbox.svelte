<script>
    export let imageUrl;
    export let show = false;
    export let onClose = () => {};

    const handleBackgroundClick = (event) => {
        if (event.target.classList.contains('lightbox-background')) {
            onClose();
        }
    }
</script>

{#if show}
    <div class="lightbox-background fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50" on:click={handleBackgroundClick}>
        <img src={imageUrl} alt="Lightbox Image" class="max-w-full max-h-full" />
        <button on:click={onClose} class="absolute top-4 right-4 text-white text-2xl">&times;</button>
    </div>
{/if}

<style>
    .lightbox-background {
        backdrop-filter: blur(5px);
    }
</style>
