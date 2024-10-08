import axios from 'axios';
import { getCookie } from '../../middleware/auth';

const instance = axios.create({baseURL: import.meta.env.VITE_DOMAIN_URL});

instance.interceptors.request.use(
    (config) => {
        const token = getCookie('token');
        if (token) config.headers['Authorization'] = `Bearer ${token}`;

        return config;
    },
    (error) => Promise.reject(error),
);

export default instance;
