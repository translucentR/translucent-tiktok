<script>
	import { onMount } from 'svelte';
	import { fly } from 'svelte/transition';
	import { backOut } from 'svelte/easing';

	let themeModes = ['light', 'dark', 'system'];
	let cond = true;
	let currentTheme = 'light'; // Default theme
	let i = themeModes.indexOf(currentTheme);

	const prev = () => {
		cond = false;
		setTimeout(() => {
			i = i !== 0 ? i - 1 : themeModes.length - 1;
		}, 10);
	};

	const next = () => {
		cond = true;
		setTimeout(() => {
			i = (i + 1) % themeModes.length;
		}, 10);
	};

	// Run this code only on the client-side
	let isClient = false;
	onMount(() => {
		isClient = typeof window !== 'undefined' && window.theme;
		if (isClient) {
			currentTheme = window.theme.get();
			i = themeModes.indexOf(currentTheme);
		}
	});

	// Reactive statements must be top-level
	// This will now check if it's running in a client and then execute
	$: if (isClient) {
		window.theme.set(themeModes[i]);
	}
</script>

<div id="sidebar">
	<div class="sidebar-content">
		<header>
			<span class="text-xl">Page Routing</span>
		</header>
		<a class="my-1 link-btn" href="/NewVideoPage">New 🎥</a>
		<a class="my-1 link-btn" href="/CudaInstructions">Cuda Instructions</a>
		<!-- <a class="my-1 link-btn" href="/page3">Page 3</a> -->
	</div>
	<div class="my-4 sidebar-content">
		<header>
			<span class="text-xl">Theme</span>
		</header>
		<div class="carousel">
			<button on:click={prev} class="fa-solid fa-chevron-left" />
			<div class="carousel-item">
				{#each [themeModes[i]] as themeMode (i)}
					<span
						in:fly={{ x: cond ? -80 : 80, duration: 500, easing: backOut }}
						out:fly={{ x: cond ? 80 : -80, duration: 500, easing: backOut }}
						class="capitalize">{themeMode}</span
					>
				{/each}
			</div>
			<button on:click={next} class="fa-solid fa-chevron-right" />
		</div>
	</div>
</div>
