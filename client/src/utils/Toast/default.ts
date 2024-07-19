import { toasts } from 'svelte-toasts';

type ToastType = 'info' | 'success' | 'error' | 'warning' | 'default';

interface ToastOptions {
  duration?: number;
  dismissible?: boolean;
  pausable?: boolean;
  theme?: 'light' | 'dark';
  placement?: 'top-right' | 'top-left' | 'bottom-right' | 'bottom-left' | 'top-center' | 'bottom-center';
}

const options: ToastOptions = {
  duration: 5000,
  dismissible: true,
  pausable: true,
  theme: 'dark',
  placement: 'top-right',
};

export const toast = (
  content: string,
  type: ToastType = 'default'
) => {
  switch (type) {
    case 'info':
      return toasts.info(content, options);
    case 'success':
      return toasts.success(content, options);
    case 'error':
      return toasts.error(content, options);
    case 'warning':
      return toasts.warning(content, options);
    default:
      return toasts.add({ description: content, ...options });
  }
};

export default toast;
