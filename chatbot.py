import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
}

def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return "I'm sorry, I don't understand that."

print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
