import re

def get_response(user_input):
    user_input_lower = user_input.lower()
    if re.search(r'\b(hi|hello)\b', user_input_lower):
        return "Hi there! How can I assist you today?"
    elif re.search(r'\b(how are you|how are you doing)\b', user_input_lower):
        return "I'm just a computer program, but I'm doing well. Thanks for asking!"
    elif re.search(r'\b(your name|who are you)\b', user_input_lower):
        return "I'm a chatbot named Shree's ChatBot! What can I do for you?"
    elif re.search(r'\b(what is your purpose|why are you here)\b', user_input_lower):
        return "I'm here to help and provide information. Ask me anything!"
    # Add more rules here
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask another question?"


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
