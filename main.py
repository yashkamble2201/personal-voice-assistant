from modules.brain import ask_assistant


def main():
    print("Yash Assistant 🤖")
    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Yash Assistant: Goodbye! 👋")
            break

        response = ask_assistant(user_message)

        print(f"Yash Assistant: {response}\n")


if __name__ == "__main__":
    main()