import pyttsx3
import re


def speak(text):

    if not text:
        return

    text = str(text)

    # Remove emojis and special characters for speech
    clean_text = re.sub(
        r'[^\x00-\x7F]+',
        '',
        text
    )

    print("Speaking...")

    engine = pyttsx3.init()

    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    engine.say(clean_text)
    engine.runAndWait()

    engine.stop()