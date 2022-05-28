import random
from QA import responses
from prediction import related



print("ChatBot: What is your name?")
user_input = input()
print("Hello " + user_input + ', Nice to meet You, What do you want to know')

name = "I.T.K"
weather = "Rainy"
mood = "Happy!"

chatbot_template = name + " : {0}" 
user_template  = user_input + " : {0}"
#{0} is gotten from format function, this substitute the variable given. replaces the placeholders that are passed as parameters  

responses()      
        
def respond(message):
    if message in responses(): 
        bot_message = random.choice(responses()[message])
    else: 
        bot_message = random.choice(responses()["default"])
    return bot_message
# A function that calls in the random function to select random answers to the same question



def send_message(message): 
    print(user_template.format(message)) 
    response = respond(message) 
    print(chatbot_template.format(response))


while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop" or my_input == "end" or my_input == "bye": 
        print ("Code ends here")
        break