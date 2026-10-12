"""A small multi-turn terminal chatbot powered by a local Ollama model."""


from ollama import chat

MODEL = "qwen3:4b"
EXIT_COMMANDS = {"exit", "quit"}

def main():
    messages: list[dict[str,str]] = []
    print(f"Ollama {MODEL} is ready! \n")

    while True:
        try:
            user_message = input("You: ").strip()
        except( EOFError, KeyboardInterrupt):
            print("Chat has ended")
            break

        if not user_message:
            continue

        if user_message.lower() in EXIT_COMMANDS:
            print("Chat has ended")
            break

        messages.append({"role": "user", "content": user_message})

        try:
            response =  chat(model=MODEL, messages=messages)
        except Exception as error:
            messages.pop()
            print( "Could not reach Ollama. Confirm that Ollama is running "
                f"and {MODEL} is installed. Details: {error}\n"
            )
            continue

        assistant_message = response.message.content
        if assistant_message is None:
            messages.pop()
            print("Ollama returned an empty message. Try again \n")
            continue
        messages.append({"role": "assistant", "content": assistant_message})
        print(f"Ollama response: {assistant_message}\n")


if __name__ == "__main__":
    main()
