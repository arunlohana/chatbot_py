
def get_reply(message):
    """Return a reply based on the user's message."""
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message in ("how are you", "how are you?"):
        return "I am fine, thanks!"
    elif message in ("bye", "goodbye", "see you"):
        return "Goodbye!"
    else:
        return "I don't know how to answer that yet. Try hello, how are you, or bye."


def chat():
    """Keep chatting until the user says goodbye."""
    print("Chatbot: Hello! Type 'bye' whenever you want to leave.")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print(f"Chatbot: {reply}")

        if user_message.strip().lower() in ("bye", "goodbye", "see you"):
            break


if __name__ == "__main__":
    chat()
