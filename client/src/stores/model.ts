import { writable } from 'svelte/store';

export interface Model {
    id: string;
    filename: string;
    name: string;
    type: string;
    status: string;
    createdAt: string;
    updatedAt: string;
    uploadedBy: string;
    weight: number;
    weightUnitSize: string;
    flops: number;
    lastTrain: string;
    deployed: boolean;
}

export const selectedModel = writable<string | null>(null);
