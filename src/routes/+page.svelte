<script>
	// SvelteKit Imports
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';

	const carouselImages = [
		{
			src: '/images/svelte.svg',
			description: 'Built using SvelteKit 👌'
		},
		{
			src: '/images/tailwind.svg',
			description: 'Easy styling with Tailwind 😍'
		},
		{
			src: '/images/electron.svg',
			description: 'Wrapped in Electron 🤖'
		}
	];

	let i = 0;

	onMount(() => {
		setInterval(() => {
			i = (i + 1) % carouselImages.length;
		}, 5000);
	});
</script>

<h1 class="text-6xl font-semibold uppercase">Introducing</h1>
<h2 class="my-6 text-4xl uppercase">Translucent TTS</h2>
