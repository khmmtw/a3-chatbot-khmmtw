from ChatBot import ChatBot

def main():
    bot = ChatBot("greetings.txt", "responses.txt", "Tell me more.")
    print("Computer:", bot.greet())

    while True:
        user_input = input("Talk to me: ")
        if user_input.lower() == "stop":
            print("Thanks for talking.")
            break
        response = bot.respond(user_input)
        print("Computer:", response)

if __name__ == "__main__":
    main()