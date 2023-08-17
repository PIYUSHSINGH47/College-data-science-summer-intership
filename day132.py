from textblob import TextBlob
#define input for corresponding ouputs
patterns_responses={
    "hii":"hello! how can I assist you?",
    "how are you":"Hello,I'm here to help you!",
    "bye":"Goodbye! Have a grat day!",
}
def chatbot_response(user_input):
    #create a tectblob object for thee user input
    blob= TextBlob(user_input.lower())
    #Check for patterns in the user input
    for pattern, response in patterns_responses.items():
        if pattern in blob.words:
            return response
        #If no pattern matches , provides a default response
        return "I'm sorry , I don't understand.Can you rephrase?"
#chatbot loop
print("Chatbot: Hello! how can I assist you? (type 'bye' to exit)")
while True:
    user_input=input("You:")
    if user_input.lower()=='bye':
        print("Chatbot:Goodbye! have a grate day!")
        break
    response=chatbot_response(user_input)
    print("Chatbot:",response)
