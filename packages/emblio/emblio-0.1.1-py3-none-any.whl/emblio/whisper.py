import torch
import whisper
from whisper.audio import (
    N_FRAMES,
    N_SAMPLES,
    log_mel_spectrogram,
    pad_or_trim,
)
from .embedding_new import AudioEmbedding


class WhisperModel:
    def __init__(self, model_type="base") -> None:
        self.model_type = model_type
        self.model = whisper.load_model(self.model_type)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)


class WhisperEmbedding(AudioEmbedding):
    def __init__(self):
        super(WhisperEmbedding, self).__init__()

        self.embedding = None

    def get_embedding(
        self,
        audio_file_path: str,
        model: WhisperModel,
        **decode_options,
    ):
        dtype = torch.float16 if decode_options.get("fp16", True) else torch.float32
        mel = log_mel_spectrogram(audio_file_path, padding=N_SAMPLES)
        mel_segment = pad_or_trim(mel, N_FRAMES).to(self.model.device).to(dtype)
        self.embedding = model.encoder(mel_segment.unsqueeze(0)).squeeze(0)
        return self.embedding

    def get_shape(self):
        return self.embedding.shape
