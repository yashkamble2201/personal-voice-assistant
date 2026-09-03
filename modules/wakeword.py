import queue
import numpy as np
import sounddevice as sd
from openwakeword.model import Model


# Audio settings
SAMPLE_RATE = 16000
CHANNELS = 1
BLOCK_SIZE = 512

audio_queue = queue.Queue()

# Load wake-word model
wake_model = Model(
    wakeword_models=["hey_jarvis"],
    inference_framework="onnx"
)


def audio_callback(indata, frames, time, status):

    if status:
        print(status)

    audio_queue.put(indata.copy())


def wait_for_wake_word():

    print("💤 Waiting for wake word: Hey Jarvis...")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        blocksize=BLOCK_SIZE,
        callback=audio_callback
    ):

        while True:

            audio = audio_queue.get()

            audio = np.squeeze(audio)

            prediction = wake_model.predict(audio)

            for name, score in prediction.items():

                if score > 0.35:
                    print("🎙️ Wake word detected!")
                    return True

if __name__ == "__main__":
    wait_for_wake_word()