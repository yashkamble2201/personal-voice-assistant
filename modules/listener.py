import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel


# Faster-Whisper model
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)


def listen():
    print("🎤 Listening...")

    sample_rate = 16000
    duration = 5

    try:
        audio = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="float32"
        )

        sd.wait()

        audio = np.squeeze(audio)

        segments, info = model.transcribe(
            audio,
            language="en",
            beam_size=1,
            vad_filter=True
        )

        text = " ".join(
            segment.text for segment in segments
        ).strip()

        if text:
            return text

        print("⚠️ I didn't hear anything.")
        return ""

    except Exception as error:
        print(f"❌ Speech recognition error: {error}")
        return ""