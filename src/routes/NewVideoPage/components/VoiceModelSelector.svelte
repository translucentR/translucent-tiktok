<script lang="ts">
	import { onMount } from 'svelte';
	import { createEventDispatcher } from 'svelte';
	import Spinner from '../../../lib/components/loading-spinner.svelte';

	export let toolkit: string;

	$: if (toolkit) {
		fetchModels(toolkit);
	}

	let models = [];
	let selectedModel = '';
	let isReady = false;
	// Dispatch function to communicate with the parent component
	const dispatch = createEventDispatcher();

	const fetchModels = async (toolkit) => {
		try {
			const url = `http://localhost:5000/models?toolkit=${toolkit}`;
			const response = await fetch(url);
			if (!response.ok) {
				throw new Error('Failed to fetch');
			}
			const data = await response.json();
			models = data.models;
			isReady = true;
			selectedModel = models[0]; // default to the first model
			dispatch('voiceModelChange', { model: selectedModel });
		} catch (error) {
			console.error('Error fetching models based on toolkit:', error);
			isReady = true;
		}
	};

	// Function to handle selection changes
	const handleModelChange = (event: Event) => {
		selectedModel = (event.target as HTMLSelectElement).value;
		dispatch('voiceModelChange', { model: selectedModel });
	};
</script>

<div class="flex items-center">
	{#if isReady}
		<select class="rounded-md p-2" bind:value={selectedModel} on:change={handleModelChange}>
			{#each models as model}
				<option value={model}>{model}</option>
			{/each}
		</select>
	{:else}
		<Spinner />
	{/if}
</div>
