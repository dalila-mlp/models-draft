<script lang="ts">
    import { onMount } from "svelte";
    import { ToastContainer, FlatToast }  from "svelte-toasts";
    import SelectModel from "../../components/upload/SelectModel.svelte";
    import UploadedItem from "../../components/upload/UploadedItem.svelte";
    import axios from "../../utils/Axios/axios";
    import toast from "../../utils/Toast/default";

    let modelNames: Array<string> = [];
    let modelTypes: Array<string> = [];

    onMount(async () => {
        const namesResponse = await axios.get("/model/names");
        modelNames = await namesResponse.data;

        const typesResponse = await axios.get("/model/types");
        modelTypes = await typesResponse.data;
    });

    interface Model {
        filename: string;
        id: string;
        name: string;
        type: string;
        weight: number;
        weightUnitSize: string;
    };

    let models: Model[] = [];
    let selectedModel: string = "Choose model name";
    let selectedType: string = "Choose model type";
    let file: File | null = null;
    let fileInput: HTMLInputElement | null = null;
    let llm_operation: boolean = false;

    async function handleFileChange(event: Event) {
        llm_operation = true;
        const input = event.target as HTMLInputElement;

        if (input.files && input.files[0]) {
            file = input.files[0];
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('/model/info', formData);
            if (response.status !== 200) throw new Error((await response.data).message);
            toast('Paremeters retrieved successfully!', 'success');
            const result = await response.data;
            selectedModel = result.model_name;
            selectedType = result.model_type;
        } catch (error) {
            toast(error.message, 'error');
        } finally {
            llm_operation = false;
        }
    }

    async function handleUpload() {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('name', selectedModel);
        formData.append('type', selectedType);

        try {
            const response = await axios.post('/model/create', formData);
            if (response.status !== 201) throw new Error((await response.data).message);
            toast('Model uploaded successfully!', 'success');
            const result = await response.data;

            models = [
                ...models,
                {
                    filename: result.filename,
                    id: result.id,
                    name: result.name,
                    type: result.type,
                    weight: result.weight,
                    weightUnitSize: result.weightUnitSize,
                }
            ];
            
            file = null;
            selectedModel = modelNames[0];
            selectedType = modelTypes[0];
            if (fileInput) fileInput.value = '';
        } catch (error) {
            toast(error.message, 'error');
        }
    }

    async function removeModel(id: string) {
        try {
            const response = await axios.delete(`/model/${id}/delete`);
            if (response.status !== 204) throw new Error((await response.data).message);
            models = models.filter((model) => model.id !== id);
            selectedModel = "Choose model name";
            selectedType = "Choose model type";
        } catch (error) {
            toast(error.message, 'error');
        }
    }
</script>

<svelte:head>
    <title>Upload your model - Dalila</title>
    <meta name="description" content="Upload your artificial intelligence model to our platform now!" />
</svelte:head>

<div class="relative grid items-center max-w-[1400px] mx-auto w-full text-sm sm:text-base mt-[76px]">
    {#if typeof window !== 'undefined'}
        <ToastContainer let:data={data}>
            <FlatToast {data} />
        </ToastContainer>
    {/if}
    <div class="flex flex-col items-center justify-self-center w-1/2 bg-[#15223C] rounded-3xl py-[34px]">
        <div class="flex flex-col items-center">
            <h1 class="text-3xl font-medium">Upload your model</h1>
            <span class="text-sm text-gray-500 font-bold">only .py extension is available</span>
        </div>
        {#if llm_operation}
            <div class="w-full bg-yellow-300 text-black text-center py-2 my-[13px]">
                Parameters being determined by llm, please wait...
            </div>
        {/if}
        <div class="flex flex-col items-center w-full mt-[21px]">
            <div class="flex flex-col items-center w-full">
                <h2 class="w-3/4 text-lg font-medium mb-[5px]">Model</h2>
                <SelectModel
                    bind:value={selectedModel}
                    bind:specificValue={selectedModel}
                    options={modelNames.map(modelName => ({ id: modelName, filename: modelName }))}
                    typeOption="model"
                />
            </div>
            <div class="flex flex-col items-center w-full mt-[13px]">
                <h2 class="w-3/4 text-lg font-medium mb-[5px]">Type</h2>
                <SelectModel
                    bind:value={selectedType}
                    bind:specificValue={selectedType}
                    options={modelTypes.map(modelType => ({ id: modelType, filename: modelType }))}
                    typeOption="type"
                />
            </div>
        </div>
        <div class="flex font-bold mt-[34px] text-white text-2xl">
            <input
              id="fileInput"
              type="file"
              accept=".py"
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
                    Drag model here!
                </label>
            {/if}
        </div>
        {#if file}
            <button
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold px-[55px] py-[13px] rounded-2xl mt-[34px] text-2xl"
                on:click={handleUpload}
                disabled={llm_operation || !selectedModel || !selectedType}
                class:opacity-50={llm_operation || !selectedModel || !selectedType}
                class:cursor-not-allowed={llm_operation || !selectedModel || !selectedType}
            >
                Upload
            </button>
        {/if}
        {#if models.length > 0}
            <div class="relative flex flex-col w-3/4 mt-[34px]">
                <h2 class="w-3/4 text-lg font-medium mb-[5px]">Just uploaded model(s)</h2>
                <div class="relative flex flex-col gap-3">
                    {#each models as model (model.id)}
                        <UploadedItem {...model} on:remove={() => removeModel(model.id)} />
                    {/each}
                </div>
            </div>
        {/if}
    </div>
</div>
