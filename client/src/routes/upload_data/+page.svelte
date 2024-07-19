<script lang="ts">
    import { ToastContainer, FlatToast }  from "svelte-toasts";
    import UploadedItem from "../../components/upload/UploadedItem.svelte";
    import axios from "../../utils/Axios/axios";
    import toast from "../../utils/Toast/default";

    interface Data {
        filename: string;
        id: string;
        weight: number;
        weightUnitSize: string;
    }

    let datafiles: Data[] = [];
    let file: File | null = null;
    let fileInput: HTMLInputElement | null = null;
    
    function handleFileChange(event: Event) {
        const input = event.target as HTMLInputElement;

        if (input.files && input.files[0]) {
            file = input.files[0];
        }
    }

    async function handleUpload() {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('/datafile/create', formData);
            if (response.status !== 201) throw new Error((await response.data).message);
            toast('Datfile uploaded successfully!', 'success');
            const result = await response.data;

            datafiles = [
                ...datafiles,
                {
                    filename: result.filename,
                    id: result.id,
                    weight: result.weight,
                    weightUnitSize: result.weightUnitSize,
                }
            ];
            
            file = null;
            if (fileInput) fileInput.value = '';
        } catch (error) {
            toast(error.message, 'error');
        }
    }

    async function removeDatafile(id: string) {
        try {
            const response = await axios.delete(`/datafile/${id}/delete`);
            if (response.status !== 204) throw new Error((await response.data).message);
            datafiles = datafiles.filter((datafile) => datafile.id !== id);
        } catch (error) {
            toast(error.message, 'error');
        }
    }
</script>

<svelte:head>
    <title>Upload your datafile - Dalila</title>
    <meta name="description" content="Upload your datafile to our platform now!" />
</svelte:head>

<div class="relative grid items-center max-w-[1400px] min-h-full mx-auto w-full text-sm sm:text-base mt-[76px]">
    {#if typeof window !== 'undefined'}
        <ToastContainer let:data={data}>
            <FlatToast {data} />
        </ToastContainer>
    {/if}
    <div class="flex flex-col items-center justify-self-center w-1/2 bg-[#15223C] rounded-3xl py-[34px]">
        <div class="flex flex-col items-center">
            <h1 class="text-3xl font-medium">Upload your datafile</h1>
            <span class="text-sm text-gray-500 font-bold">only .csv extension is available</span>
        </div>
        <div class="flex font-bold mt-[34px] text-white text-2xl">
            <input
              id="fileInput"
              type="file"
              accept=".csv"
              on:change={handleFileChange}
              class="hidden"
              bind:this={fileInput}
            />
            {#if file}
                <UploadedItem {...{filename: file.name}} on:remove={() => {file = null; fileInput.value = '';}} />
            {:else}
                <label
                    class="bg-blue-500 hover:bg-blue-700 cursor-pointer px-[55px] py-[13px] rounded-2xl"
                    for="fileInput"
                >
                    Drag datafile here!
                </label>
            {/if}
        </div>
        {#if file}
            <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-[55px] py-[13px] rounded-2xl mt-[34px] text-lg"
                on:click={handleUpload}
            >
                Upload
            </button>
        {/if}
        {#if datafiles.length > 0}
            <div class="relative flex flex-col w-3/4 mt-[34px]">
                <h2 class="w-3/4 text-lg font-medium mb-[5px]">Just uploaded datafile(s)</h2>
                <div class="relative flex flex-col gap-3">
                    {#each datafiles as datafile (datafile.id)}
                        <UploadedItem {...datafile} on:remove={() => removeDatafile(datafile.id)} />
                    {/each}
                </div>
            </div>
        {/if}
    </div>
</div>
