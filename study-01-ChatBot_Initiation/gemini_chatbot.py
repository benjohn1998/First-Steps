"""A small multi-turn terminal chatbot powered by Gemini."""

import os
from google import genai

MODEL = "gemini-3.5-flash"
EXIT_COMMANDS = {"/exit", "exit", "quit"}

def main() -> None:
    """An interactive Gemini chat session"""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit ( "Gemini api key has not been set. ")

    client = genai.Client(api_key=api_key)
    chat = client.chats.create(model=MODEL)

    print("Gemini chatbot is ready!")

    while True:
        try:
            user_message = input("You: ").strip()
        except(EOFError, KeyboardInterrupt):
            print("chat ended. ")
            break

        if user_message.lower() in EXIT_COMMANDS:
            print("Chat ended")
            break

        if not user_message:
            continue

        try:
            response = chat.send_message(user_message)
            print (f"Gemini: {response.text}\n")
        except Exception as error:
            print(f"Gemini request has failed- {error}.\n")

if __name__ == "__main__":
    main()