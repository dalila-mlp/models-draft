// src/svelte-carousel.d.ts
declare module 'svelte-carousel' {
    import { SvelteComponent } from 'svelte';
    export interface CarouselProps {
        autoplay?: boolean;
        autoplayTimeout?: number;
        [key: string]: any;
    }
    export default class Carousel extends SvelteComponent {
        $$prop_def: CarouselProps;
    }
}
