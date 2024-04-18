<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	let transcript = '';
	const dispatch = createEventDispatcher();
	const handleTranscriptChange = (event: Event) => {
		transcript = (event.target as HTMLTextAreaElement).value;
		dispatch('transcriptChange', { transcript });
	};
</script>

<textarea
	class="rounded-md w-[600px] h-40 resize-none p-3"
	placeholder="Enter your text here..."
	bind:value={transcript}
	on:input={handleTranscriptChange}
/>
