# Translucent TikTok Application

This project is a desktop application built with Electron, SvelteKit, and Flask, designed to convert text to speech and manage TTS (text-to-speech) functionalities. It provides an interface for selecting TTS models, languages, and outputting audio files based on the given text. The goal is to expand the capabilities to generate fully functional story-time videos autonomously.

## Prerequisites

- **Python 3.11**: Ensure Python 3.11 is installed and aliased to `python`. You can verify your Python version by running `python --version` in your terminal.
- **Node.js**: A recent version of Node.js must be installed. Verify by running `node --version`.
- **npm**: npm must also be installed as it comes with Node.js. Verify with `npm --version`.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/translucentR/translucenttechnology
   cd translucent-tiktok
   ```

2. **Install Node Dependencies**:
   ```bash
   npm install
   ```
   This will install dependencies for node and python

## Running the Application

- **Development Mode**:
  Run the application in development mode by executing:

  ```bash
  npm run dev
  ```

  This will concurrently start the backend Flask server on port 5000 and the Electron frontend on port 3000.

- **Production Mode**:
  Building the application for production has not been tested yet. Instructions will be added when available.

## Updating Python Dependencies

If new Python packages are installed during development, make sure to update the `requirements.txt` file. Here are the steps to ensure consistency:

1. Activate your Python virtual environment.
2. Install any new packages as required.
3. Update `requirements.txt` by running:
   ```bash
   pip freeze > backend/requirements.txt
   ```

## Notes

- The Flask API runs on `http://localhost:5000`.
- The Electron app runs on `http://localhost:3000`.
- Ensure all Python development is done within the virtual environment to avoid conflicts with global packages.

## Troubleshooting

- If you encounter issues related to Python versions or dependencies, make sure the virtual environment is set up correctly and activated.
- Ensure Node.js and npm are updated to their latest versions if you encounter any issues with npm packages or scripts.
- For NVIDIA GPU support please make sure to have CUDA v12.1.0 and cuDNN v9.0.0 installed

## Contributing

Contributions to the project are welcome. Ensure any open issues are discussed in the issue tracker before opening a pull request.
