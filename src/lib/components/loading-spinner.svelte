<div class="flex justify-center items-center">
	<div class="spinner"></div>
</div>

<style>
	.spinner {
		border: 4px solid rgba(255, 255, 255, 0.3); /* Light grey border */
		border-top: 4px solid #3498db; /* Blue border for the top side */
		border-radius: 50%;
		width: 40px;
		height: 40px;
		animation: spin 2s linear infinite;
	}

	@keyframes spin {
		0% {
			transform: rotate(0deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>
