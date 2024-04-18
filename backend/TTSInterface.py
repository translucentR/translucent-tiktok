from abc import ABC, abstractmethod

class TTSInterface(ABC):
    @abstractmethod
    def list_models(self):
        """Method to list available TTS models."""
        pass

    @abstractmethod
    def generate_audio(self, text, model, output_path):
        """Method to generate audio from text using a specified model."""
        pass

    @abstractmethod
    def get_model_languages(self, model):
        """Method to get available languages for a specified model."""
        pass
