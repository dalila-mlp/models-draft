import { redirect } from '@sveltejs/kit';

/** @type {import('@sveltejs/kit').Handle} */
export const handle = async ({ event, resolve }) => {
    const authToken = event.cookies.get('token');
    
    if (!authToken && event.url.pathname !== '/login') {
        throw redirect(303, '/login');
    }

    if (authToken && event.url.pathname === '/login') {
        throw redirect(303, '/');
    }

    return await resolve(event);
}
