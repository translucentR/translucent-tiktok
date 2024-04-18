<script lang="ts">
	import { createEventDispatcher, onMount } from 'svelte';
	import '$lib/css/theme-colors.css';
	import LoadingSpinner from '../../../lib/components/loading-spinner.svelte';
	let cudaDetails = {
		cudaAvailable: undefined,
		cudaVersion: undefined,
		cuDNNVersion: undefined,
		numberOfGPUs: undefined,
		gpus: undefined
	};

	const dispatch = createEventDispatcher();
	onMount(async () => {
		try {
			const response = await fetch('http://localhost:5000/local/cuda');
			if (!response.ok) {
				cudaDetails.cudaAvailable = false;
				throw new Error('Failed to fetch CUDA details');
			}
			const data = await response.json();
			dispatch('useCudaChange', { cudaAvailalble: data.cudaAvailable });
			cudaDetails = {
				cudaAvailable: data.cudaAvailable,
				cudaVersion: data.cudaVersion,
				cuDNNVersion: data.cuDNNVersion,
				numberOfGPUs: data.numberOfGPUs,
				gpus: data.gpus
			};
		} catch (error) {
			console.error('Error fetching CUDA details:', error);
			cudaDetails.cudaAvailable = false;
			dispatch('useCudaChange', { cudaAvailalble: false });
		}
	});
</script>

{#if cudaDetails.cudaAvailable === undefined}
	<LoadingSpinner />
{/if}
{#if cudaDetails.cudaAvailable === false}
	<p class="text-red-500">
		You do not have CUDA enabled. Your video will take a while to process. Please see <a
			class="underline"
			href="/CudaInstructions">here</a
		> for a guide to install.
	</p>
{/if}

{#if cudaDetails.cudaAvailable !== undefined}
	<div>
		<h2 class="text-lg font-bold">CUDA Details:</h2>
		<ul>
			<li>CUDA Available: {cudaDetails.cudaAvailable ? 'Yes' : 'No'}</li>
			{#if cudaDetails.cudaVersion}
				<li>CUDA Version: {cudaDetails.cudaVersion}</li>
			{/if}
			{#if cudaDetails.cuDNNVersion}
				<li>cuDNN Version: {cudaDetails.cuDNNVersion}</li>
			{/if}
			{#if cudaDetails.numberOfGPUs}
				<li>Number of GPUs: {cudaDetails.numberOfGPUs}</li>
			{/if}
			{#if cudaDetails.gpus}
				<li>GPU Names: {cudaDetails.gpus.join(', ')}</li>
			{/if}
		</ul>
	</div>
{/if}
