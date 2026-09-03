from modules.brain import ask_assistant
from modules.speech import speak
from modules.listener import listen
from modules.wakeword import wait_for_wake_word
from modules.actions import execute_action


def main():
    print("Yash Assistant 🤖")
    print("Say 'Hey Jarvis' to wake me.")
    print("Say 'exit' to stop.\n")

    while True:

        # ==============================
        # 1. WAIT FOR WAKE WORD
        # ==============================
        print("💤 Waiting for wake word...")

        if not wait_for_wake_word():
            continue

        print("🎙️ I'm listening...\n")

        # ==============================
        # 2. LISTEN TO USER
        # ==============================
        user_message = listen()

        # Ignore empty/invalid speech
        if not user_message:
            print("⚠️ I didn't hear anything.\n")
            continue

        print(f"You: {user_message}")

        # ==============================
        # 3. EXIT COMMAND
        # ==============================
        if user_message.lower().strip() in ["exit", "quit", "stop"]:
            response = "Goodbye! 👋"
            print(f"Yash Assistant: {response}")
            speak(response)
            break

        # ==============================
        # 4. CHECK FOR ACTIONS
        # ==============================
        action_response = execute_action(user_message)

        if action_response:
            response = action_response
        else:
            # ==============================
            # 5. ASK LOCAL AI
            # ==============================
            response = ask_assistant(user_message)

        # ==============================
        # 6. DISPLAY RESPONSE ONCE
        # ==============================
        print(f"Yash Assistant: {response}")

        # ==============================
        # 7. SPEAK RESPONSE
        # ==============================
        speak(response)

        print()


if __name__ == "__main__":
    main()