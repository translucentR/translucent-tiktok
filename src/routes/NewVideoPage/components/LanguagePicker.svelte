<script lang="ts">
	import { onMount, createEventDispatcher } from 'svelte';
	let languages = [];
	let selectedLanguage = '';
	const dispatch = createEventDispatcher();

	export let model = '';

	// Fetch languages whenever the model changes
	onMount(() => {
		fetchLanguages();
	});

	$: model, fetchLanguages();

	async function fetchLanguages() {
		if (model) {
			const response = await fetch(
				`http://localhost:5000/model/languages?model=${encodeURIComponent(model)}`
			);
			if (response.ok) {
				const data = await response.json();
				languages = data.languages;
			} else {
				languages = [];
				console.error('Failed to fetch languages');
			}
		}
	}

	function handleLanguageChange(event: Event) {
		selectedLanguage = (event.target as HTMLSelectElement).value;
		dispatch('languageChange', { language: selectedLanguage });
	}
</script>

{#if languages.length > 0}
	<div class="language-selector">
		<label for="language-select">Choose a language:</label>
		<select id="language-select" bind:value={selectedLanguage} on:change={handleLanguageChange}>
			{#each languages as language}
				<option value={language}>{language}</option>
			{/each}
		</select>
	</div>
{:else}
	<p>No additional languages available.</p>
{/if}
