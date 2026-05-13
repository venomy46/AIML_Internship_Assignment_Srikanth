# Simple rule-based chatbot

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()
        
        if user == "hello" or user == "hi":
            print("Chatbot: Hi there! How can I help you?")
        
        elif "name" in user:
            print("Chatbot: I am a simple NLP chatbot.")
        
        elif "how are you" in user:
            print("Chatbot: I am fine! How about you?")
        
        elif "help" in user:
            print("Chatbot: I can answer basic questions. Try asking something simple.")
        
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        
        else:
            print("Chatbot: Sorry, I don't understand.")

# Run chatbot
chatbot()