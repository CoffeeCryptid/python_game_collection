# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#initialize global variable range
rng = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global rng
    global secret_number
    global rem_guess
    secret_number = random.randrange(0, rng)
    rem_guess = math.ceil(math.log(rng, 2))
    print("Started new game! The range is [0,{}). Remaining guesses: {}.".format(rng, rem_guess))


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global rng
    rng = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global rng
    rng = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global rem_guess
    n = int(guess)
    print("Guess was {}.".format(n))
    rem_guess -= 1
    if rem_guess <= 0 and n != secret_number:
        print("Wrong. You lost!\n")
        new_game()
    elif n > secret_number:
        print("Lower! Remaining guesses: {}.".format(rem_guess))
    elif n < secret_number:
        print("Higher! Remaining guesses: {}.".format(rem_guess))
    else:
        print("Correct! You won!\n")
        new_game()

    
# create frame
f = simplegui.create_frame("Guess the number!", 300, 300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Number", input_guess, 190)
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
