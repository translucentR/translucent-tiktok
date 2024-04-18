<script>
	import { createEventDispatcher, onMount } from 'svelte';

	export let filePath = ''; // This will store the selected directory path

	// Function to open the directory picker
	const dispatch = createEventDispatcher();
	async function selectDirectory() {
		const path = await window.electronAPI.selectDirectory();
		filePath = path;
		if (path) {
			dispatch('filePathChange', { path: path });
		}
	}
</script>

<div class="flex items-center gap-2">
	<input
		type="text"
		readonly
		class="flex-grow w-[400px] p-2 rounded-md"
		value={filePath}
		placeholder="Select a directory to save videos..."
	/>
	<button on:click={selectDirectory} class="p-2 rounded-md cursor-pointer link-btn !max-w-[100px]"
		>Browse...</button
	>
</div>
