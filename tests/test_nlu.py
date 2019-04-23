from rasa_nlu.model import Interpreter

interpreter = Interpreter.load('../models/current/nlu')

# define function to ask question
def ask_question(text):
    print(interpreter.parse(text))
    
# asking question
ask_question("i want to buy a laptop")
ask_question("hello")    