import requests

from modules.memory import (
    create_database,
    save_message,
    get_recent_messages
)


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3"


# Create the database when the assistant starts
create_database()


def ask_assistant(user_message):

    # Get previous conversation
    conversation_history = get_recent_messages(limit=10)

    messages = [
        {
            "role": "system",
            "content": (
                "You are Yash Assistant, a helpful personal AI voice assistant. "
                "Your name is Yash Assistant. "
                "Keep your answers friendly and concise. "
                "Do not use emojis because your responses will be spoken aloud."
            ),
        }
    ]

    # Add previous messages
    messages.extend(conversation_history)

    # Add current user message
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

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

        assistant_response = result["message"]["content"]

        # Save the conversation
        save_message("user", user_message)
        save_message("assistant", assistant_response)

        return assistant_response

    except requests.exceptions.ConnectionError:
        return (
            "I cannot connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except requests.exceptions.RequestException as error:
        return f"Sorry, something went wrong: {error}"