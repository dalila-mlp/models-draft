import { writable } from 'svelte/store';
import { goto } from '$app/navigation';

export const getCookie = (name: string) => {
    if (typeof document === 'undefined') return null;
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
}

export const authToken = writable<string | null>(getCookie('token'));

export function checkAuth() {
    let token: string | null = null;
    authToken.subscribe((value: string) => token = value);

    return !!token;
}

export function login(token: string) {
    document.cookie = `token=${token}; path=/; max-age=${60 * 60 * 24}`;
    authToken.set(token);
    goto('/');
}

export function logout() {
    document.cookie = 'token=; path=/; max-age=0';
    authToken.set(null);
    goto('/login');
}
