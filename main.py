from modules.brain import ask_assistant
from modules.speech import speak
from modules.listener import listen
from modules.actions import execute_action
import time


def main():
    print("Yash Assistant 🤖")
    print("Say 'exit' to stop.\n")

    while True:

        user_message = listen()

        # Ignore empty or invalid recognition
        if not user_message:
            continue

        print(f"You: {user_message}")

        if user_message.lower() in ["exit", "quit", "stop"]:
            response = "Goodbye!"
            print(f"Yash Assistant: {response}")
            speak(response)
            break

        action_response = execute_action(user_message)

        if action_response:
            response = action_response
        else:
            response = ask_assistant(user_message)

        print(f"Yash Assistant: {response}")

        print("Speaking...")
        speak(response)

        time.sleep(0.5)


if __name__ == "__main__":
    main()