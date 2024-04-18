<script lang="ts">
	import { onMount, createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	const toolkitList = ['Coqui.ai'];
	let selectedToolkit = toolkitList[0];

	onMount(() => {
		// Dispatch the initial state right after the component has been mounted
		dispatch('toolkitChange', { toolkit: toolkitList[0] });
	});
	function handleModelChange(event: Event) {
		selectedToolkit = (event.target as HTMLSelectElement).value;
		dispatch('toolkitChange', { toolkit: selectedToolkit });
	}
</script>

<select class="rounded-md p-2" bind:value={selectedToolkit} on:change={handleModelChange}>
	{#each toolkitList as listItem}
		<option value={listItem}>{listItem}</option>
	{/each}
</select>
