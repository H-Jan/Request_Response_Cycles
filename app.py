
from flask import Flask 
from random import randint

app = Flask(__name__)

@app.route('/')
def homepage():
    """ Shows a greeting to the user. """
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """ Display a message tot he user that changes based on their input """
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def choiced_dessert(users_dessert):
    """ Displays a message showing that I like desserts too"""
    return f'How did you know I liked {users_dessert}?'


#Mad Libs Challenge
@app.route('/madlibs/<adjective>/<noun>')
def madlibs_adjective_noun(adjective, noun):
    """ Displays a work appropriate adlibs response"""
    return f'The {adjective} {noun} is angry!'

#Multiply 2 Numbers Challenge
@app.route('/multiply/<number1>/<number2>')
def multiplication_program(number1, number2):
    if number1.isdigit() and number2.isdigit():
        result = int(number1) * int(number2)
        """ Demonstrates a multiplication function with route variables as inputs """
        return f' {number1} times {number2} is {result}'
    else: 
        return f'Try Again! This time, input two numnbers!'


#Say N Times
@app.route('/sayntimes/<word>/<n>')
def sayItNTimes(word, n):
    if n.isdigit():
        word_format = (word + ' ')
        formula = word_format * int(n)
        return f'{formula}'
    else:
        return f'Invalid input, Please try again by entering a word and a number'

#Dice Game Yay!
@app.route('/dicegame')
def playingGame():
    """ Imported randint from Random to choose a random integer """
    random_number = randint(1,6)
    if random_number == 6:
        return f'You rolled a 6, you won!'
    else:
        return f'You rolled a {random_number}, you lost!'



if __name__ == '__main__':
    app.run(debug=True)

