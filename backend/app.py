from flask import Flask, request, jsonify, send_from_directory, abort
from flask_cors import CORS
import torch
from os import path, getenv
from CoquiTTSAdapter import CoquiTTSAdapter

# declare flas app
app = Flask(__name__)

# allow communications on local ports
CORS(app, resources={r"*": {"origins": ["http://localhost:3000", "https://localhost:443"]}})

# selects the tts adapter to use. Will grow as more toolkits are added
def get_tts_adapter(toolkit):
    if toolkit == "Coqui.ai":
        return CoquiTTSAdapter(device=torch.device("cuda" if torch.cuda.is_available() else "cpu"))
    # Add other toolkit adapters as elif branches
    return None


@app.route('/models', methods=['GET'])
def list_models():
    toolkit = request.args.get('toolkit')
    adapter = get_tts_adapter(toolkit)
    if adapter:
        models = adapter.list_models()
        return jsonify({'models': models})
    return jsonify(error="Invalid toolkit"), 400

@app.route('/model/languages', methods=['GET'])
def get_model_languages():
    toolkit = request.args.get('toolkit')
    tts_model = request.args.get('model')
    if not tts_model:
        return jsonify({"error": "Model identifier not provided"}), 400
    
    adapter = get_tts_adapter(toolkit)
    if adapter:
        languages = adapter.get_model_languages(tts_model)
        return jsonify({"languages": languages})
    return jsonify({"error": "Invalid toolkit"}), 400

@app.route('/local/cuda', methods=['GET'])
def check_cuda():
    """Check if CUDA is available and return detailed CUDA-related information."""
    details = {
        "cudaAvailable": torch.cuda.is_available()
    }

    try:
        details["cudaVersion"] = torch.version.cuda if torch.cuda.is_available() else "None"
    except Exception as e:
        details["cudaVersion"] = "None"

    try:
        details["cuDNNVersion"] = str(torch.backends.cudnn.version()) if torch.cuda.is_available() else "None"
    except Exception as e:
        details["cuDNNVersion"] = "None"

    try:
        details["numberOfGPUs"] = str(torch.cuda.device_count()) if torch.cuda.is_available() else "None"
    except Exception as e:
        details["numberOfGPUs"] = "None"

    try:
        if torch.cuda.is_available() and torch.cuda.device_count() > 0:
            details["gpus"] = [torch.cuda.get_device_name(i) for i in range(torch.cuda.device_count())]
        else:
            details["gpus"] = ["No GPU found"]
    except Exception as e:
        details["gpus"] = ["None"]

    return jsonify(details)


# TODO: finish implementation, currently generates an audio track
@app.route('/video/generate', methods=['POST'])
def generate_video():
    try:
        data = request.json
        toolkit = data.get('toolkit')
        adapter = get_tts_adapter(toolkit)
        
        if not adapter:
            return jsonify({"error": "Invalid toolkit"}), 400
        
        transcript = data.get('transcript')
        voiceModel = data.get('voiceModel')
        filePath = data.get('filePath')
        outputFile = path.join(filePath, 'output.wav')

        # Assuming generate_audio is a synchronous function that waits for completion
        result = adapter.generate_audio(transcript, voiceModel, outputFile)
        if result:
            return jsonify({"message": "Video generation completed successfully.", "outputPath": outputFile})
        else:
            return jsonify({"error": "Audio generation failed"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# TODO: finish implementation, currently returns an audio track   
@app.route('/video', methods=['GET'])
def serve_video():
    # Retrieve the full path from the query parameter and decode URL encoding
    full_path = request.args.get('path')
    if not full_path:
        abort(400, description="No file path provided")
    
    # Decode URL and normalize path
    full_path = path.normpath(request.args.get('path', ''))
    
    # Separate the directory path and the filename
    directory_path, filename = path.split(full_path)

    if not path.isfile(full_path):
        abort(404, description="File not found")
    
    # Send file from its directory
    return send_from_directory(directory_path, filename, as_attachment=True)

@app.route('/', methods=['GET'])
def root_path():
    return(jsonify("true"))
if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
