import random



print("ChatBot: What is your name?")
user_input = input()
print("Hello " + user_input + ', Nice to meet You, What do you want to know')

name = "I.T.K"
weather = "Rainy"
mood = "Sad"

chatbot_template = name + " : {0}" 
user_template  = user_input + " : {0}"
#{0} is gotten from format function, this substitute the variable given. replaces the placeholders that are passed as parameters  

responses = {
    "What's your name?": [
    "They call me {0}".format(name),
    "I usually go by {0}".format(name),
    "Je mapple {0}".format(name),
    "You can call me {0}".format(name),
    "Where is my manners, You call me danny{0}".format(name)],
    #suggested response for the question "Whats is your name?"
    #the value(answers) are grouped in a list
    
    
    "what's today's weather?": [
    "The weather is {0}".format(weather), 
    "It's {0} today".format(weather), 
    "Let me check, it looks {0} today".format(weather) ],
    
    "Are you a robot?": [ 
    "What do you think?", 
    "Maybe yes, maybe no!", 
    "Yes, I am a robot with human feelings.", ],
    
    "how are you?": [ 
    "I am feeling {0}".format(mood), 
    "{0}! How about you?".format(mood), 
    "I am {0}! How about yourself?".format(mood), ],
    
    "": [ 
    "Hey! Are you there?", 
    "What do you mean by saying nothing?", 
    "Sometimes saying nothing tells a lot :)", ],
    "default": [
    "this is a default message"]
    #response is written in a key and value format where the key is the question and value is the answer
}
        
        
def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message
# A function that calls in the random function to select random answers to the same question

def related(x_text):
    if "name" in x_text:
        y_text = "What's your name?"
    elif "weather" in x_text:
        y_text = "what's today's weather?"
    elif "robot" in x_text:
        y_text = "are you a robot?"
    elif "how are" in x_text:
        y_text = "how are you?"
    else:
        y_text = ""
    return y_text
# A function helps to match words that can be related to the question

def send_message(message): 
    print(user_template.format(message)) 
    response = respond(message) 
    print(chatbot_template.format(response))
  
while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop" or my_input == "end": 
        print ("Code ends here")
        break