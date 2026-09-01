import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer


MODEL_PATH = "models/vosk-model-small-en-in-0.4"

model = Model(MODEL_PATH)


def listen():

    q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status)

        q.put(bytes(indata))

    device_info = sd.query_devices(kind="input")

    sample_rate = int(device_info["default_samplerate"])

    recognizer = KaldiRecognizer(model, sample_rate)

    print("🎤 Listening...")

    with sd.RawInputStream(
        samplerate=sample_rate,
        blocksize=8000,
        device=device_info["name"],
        dtype="int16",
        channels=1,
        callback=callback,
    ):

        while True:

            data = q.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "").strip()

                if text:
                    return text