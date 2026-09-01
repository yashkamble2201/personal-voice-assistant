import webbrowser
import subprocess
from datetime import datetime


def execute_action(command):
    """
    Execute safe, predefined assistant actions.
    Returns a response if an action was handled.
    Returns None if the command is not an action.
    """

    command = command.lower().strip()

    # Open Google Chrome
    if "open chrome" in command or "open google chrome" in command:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Opening Chrome."

    # Open VS Code
    if "open vs code" in command or "open visual studio code" in command:
        subprocess.Popen("code")
        return "Opening Visual Studio Code."

    # Open YouTube
    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # Open Google
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    # Tell time
    if "what time" in command or "current time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    return None