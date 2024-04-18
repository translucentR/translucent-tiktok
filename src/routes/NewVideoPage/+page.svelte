<script lang="ts">
	import TranscriptPrompt from './components/TranscriptPrompt.svelte';
	import VoiceModelSelector from './components/VoiceModelSelector.svelte';
	import CudaDetails from './components/CudaDetails.svelte';
	import VideoStoragePathPicker from './components/VideoStoragePathPicker.svelte';
	import LanguagePicker from './components/LanguagePicker.svelte';
	import ToolkitSelector from './components/ToolkitSelector.svelte';
	import LoadingSpinner from '../../lib/components/loading-spinner.svelte';
	import AudioPlayer from './components/AudioPlayer.svelte';

	let transcript = '';
	const handleTranscriptChange = (e: CustomEvent) => {
		transcript = e.detail.transcript;
	};

	let voiceModel = '';
	const handleVoiceModelChange = (e: CustomEvent) => {
		voiceModel = e.detail.model;
		console.log(voiceModel);
	};

	let useCuda: boolean | undefined = undefined;
	const handleCudaChange = (e: CustomEvent) => {
		useCuda = e.detail.cudaAvailalble;
	};

	let filePath: string | undefined = undefined;
	const handleFilePickerChange = (e: CustomEvent) => {
		filePath = e.detail.path;
	};

	// let selectedLanguage = '';
	// const handleLanguageChange = (e: CustomEvent) => {
	// 	selectedLanguage = e.detail.language;
	// };

	let selectedToolkit = '';
	const handleToolkitChange = (e: CustomEvent) => {
		selectedToolkit = e.detail.toolkit;
	};

	let outputPath = '';
	let isSubmitting = false;
	const handleSubmit = async () => {
		outputPath = '';
		const data = {
			transcript: transcript,
			cuda: useCuda,
			voiceModel: voiceModel,
			filePath: filePath,
			toolkit: selectedToolkit
		};

		isSubmitting = true;
		const response = await fetch('http://localhost:5000/video/generate', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		});

		isSubmitting = false;
		const result = await response.json();
		if (response.ok) {
			console.log('Success:', result);
			outputPath = result.outputPath;
		} else {
			console.error('Failed:', result.error);
		}
	};
</script>

<div class="flex flex-col justify-center items-center [&>*]:m-4">
	<h1 class="text-6xl font-semibold uppercase pb-8">Create a new TTS Video</h1>
	<TranscriptPrompt on:transcriptChange={handleTranscriptChange} />
	<div class="flex space-x-8 items-center">
		<ToolkitSelector on:toolkitChange={handleToolkitChange} />
		<VoiceModelSelector on:voiceModelChange={handleVoiceModelChange} toolkit={selectedToolkit} />
	</div>
	<VideoStoragePathPicker on:filePathChange={handleFilePickerChange} />
	<!-- <LanguagePicker on:languageChange={handleLanguageChange} /> -->
	<button on:click={handleSubmit} class="my-1 link-btn">
		{#if isSubmitting}
			<LoadingSpinner />
		{:else}
			Submit
		{/if}
	</button>
	{#if outputPath}
		<p>video available at {outputPath}</p>
		<AudioPlayer src={`http://localhost:5000/video?path=${encodeURIComponent(outputPath)}`} />
	{/if}
	<CudaDetails on:useCudaChange={handleCudaChange} />
	<p>toolkit: {selectedToolkit}</p>
</div>
