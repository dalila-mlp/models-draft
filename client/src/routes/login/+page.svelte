<script lang="ts">
    import { createEventDispatcher } from 'svelte';
    import { ToastContainer, FlatToast } from "svelte-toasts";
    import { login } from '../../middleware/auth';
    import axios from "../../utils/Axios/axios";
    import toast from "../../utils/Toast/default";

    let username: string = '';
    let password: string = '';
    const dispatch = createEventDispatcher();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post(
                "authentication_token",
                {username, password},
                {headers: {"Content-Type": "application/json"}},
            );

            if (response.status !== 200) throw new Error('Login failed! Please check your credentials and try again.');

            const data = await response.data;
            dispatch('login', { token: data.token });
            login(data.token);
        } catch (error) {
            toast(error.message, 'error');
        }
    };
</script>

<svelte:head>
    <title>Login - Dalila</title>
    <meta name="description" content="Log on to the platform to access all our features!" />
</svelte:head>

<div class="relative flex items-center justify-center h-screen bg-[#15223C] text-white -mt-[76px]">
    {#if typeof window !== 'undefined'}
        <ToastContainer let:data={data}>
            <FlatToast {data} />
        </ToastContainer>
    {/if}
    <form class="bg-[#1e293b] rounded-lg p-8 w-full max-w-md space-y-6" on:submit={handleSubmit}>
        <h2 class="text-3xl font-semibold">Login</h2>
        <div>
            <label for="username" class="block text-sm font-medium text-gray-300">Email</label>
            <input 
                type="username" 
                id="username" 
                bind:value={username} 
                required 
                class="mt-1 block w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
        </div>
        <div>
            <label for="password" class="block text-sm font-medium text-gray-300">Password</label>
            <input 
                type="password" 
                id="password" 
                bind:value={password} 
                required 
                class="mt-1 block w-full px-3 py-2 bg-gray-700 border border-gray-600 rounded-md text-white focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
        </div>
        <button 
            type="submit" 
            class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
            Login
        </button>
    </form>
</div>

<style>
    ::-webkit-scrollbar {
        width: 12px;
    }

    ::-webkit-scrollbar-track {
        background: #1e293b;
    }

    ::-webkit-scrollbar-thumb {
        background-color: #64748b;
        border-radius: 20px;
        border: 3px solid #1e293b;
    }
</style>
