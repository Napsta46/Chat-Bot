from QA import responses

responses()
def related(x_text):
    name = "I.T.K"
    weather = "Rainy"
    mood = "Happy!"

    responses()
    
    if "name" in x_text:
        y_text = "What's your name?"
    elif "weather" in x_text:
        y_text = "what's today's weather?"
    elif "robot" in x_text:
        y_text = "are you a robot?"
    elif "how are" in x_text:
        y_text = "how are you?"
    elif "stop" in x_text:
        y_text = "exit"
    elif "end" in x_text:
        y_text = "exit"
    elif "bye" in x_text:
        y_text = "exit"
    elif "exit" in x_text:
        y_text = "exit"
    else:
        y_text = ""
    return y_text
# A function helps to match words that can be related to the question
