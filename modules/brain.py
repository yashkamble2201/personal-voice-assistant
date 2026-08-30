import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3"


def ask_assistant(user_message):
    messages = [
        {
            "role": "system",
            "content": (
                "You are Yash Assistant, a helpful personal AI voice assistant. "
                "Your name is Yash Assistant. "
                "Keep your answers friendly and concise."
            ),
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=data,
            timeout=120,
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.exceptions.ConnectionError:
        return (
            "I cannot connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except requests.exceptions.RequestException as error:
        return f"Sorry, something went wrong: {error}"