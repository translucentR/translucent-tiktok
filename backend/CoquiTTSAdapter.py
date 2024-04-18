import torch
from TTS.api import TTS as CoquiTTS
from TTSInterface import TTSInterface 

class CoquiTTSAdapter(TTSInterface):
    def __init__(self, device=None):
        self.device = device or torch.device("cpu")

    def list_models(self):
        try:
            return CoquiTTS().list_models().list_models()
        except Exception as e:
            print(e)
            return []

    def generate_audio(self, text, model, output_path):
        try:
            tts = CoquiTTS(model_name=model, progress_bar=True).to(self.device)
            return tts.tts_to_file(text, file_path=output_path)
        except Exception as e:
            print(e)
            return None

    def get_model_languages(self, model):
        try:
            tts = CoquiTTS(model_name=model)
            return tts.languages if tts.is_multilingual else []
        except Exception as e:
            print(e)
            return []
