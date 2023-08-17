import sklearn
import nltk
import tkinter as tk
from tkinter import scrolledtext
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# Add individual patterns here 
patterns=[
    "hello",
    "how are you",
    "What is your name",
    "bye"
]
#Add more responses here,you can use any dictionary API
responses=[
    "hii",
    "I'm don't not well ,sorry.",
    "I'm not a chatbot.",
    "Goodbye!"
]
#Create a bag of words model
Vectorizer=CountVectorizer()
X=Vectorizer.fit_transform(patterns)


#Function to get the chatbot rewsponse
def get_response():
    user_message = input_text.get("1.0","end-1c")
    user_message_vector=Vectorizer.transform([user_message])
    similarities=cosine_similarity(user_message_vector,X)
    most_similar_index=similarities.argmax()
    if similarities[0][most_similar_index]>0:
        response=responses[most_similar_index]
    else:
        response="I'm sorry, I don't understand,"
    output_text.insert(tk.END,f"chat:{response}\n")
    input_text.delete("1.0",tk.END)
#Create the main window 
root=tk.Tk()
root.title("NLP Basic Chatbot")
#Create and place widgets
input_text=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=5)
input_text.pack(padx=10,pady=10)
send_button=tk.Button(root,text="Send",command=get_response)
send_button.pack()
output_text=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=40,height=10)
output_text.pack(padx=10,pady=10)
root.mainloop()