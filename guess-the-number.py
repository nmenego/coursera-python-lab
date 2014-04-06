#Week 2 Lab
#Week 2 lab
#Guess the number
#by nmenego

import math
import simplegui
import random

# initialize global variables used in your code
number_to_guess = -1
guess_range = -1
rem_guess = -1

def new_game():
    """ Helper function to start and restart the game. """
    # new game, set default range
    restart_game(100)
    show_rem_guess()
    return

def restart_game(new_range):
    """ Reusable method to restart the guess range """
    """  and print some messages """
    global guess_range
    global number_to_guess
    global rem_guess

    # set new range
    guess_range = new_range

    # create number to guess
    number_to_guess = random.randrange(0, guess_range)
    print
    print "NEW GAME: Range is from 0 to ", guess_range

    # minimum number of guesses in binary search
    rem_guess = int(math.ceil(math.log(new_range, 2)))

    return

def show_rem_guess():
    """ Print the number of guesses left. """
    if(rem_guess != 0):
        print "Remaining guesses: ", rem_guess
    else:
        print "You ran out of guesses. :("
        restart_game(guess_range) #restart game using prev range
        show_rem_guess()
    return

# define event handlers for control panel
def range100():
    """ Button that changes range to range [0,100) and restarts """
    restart_game(100)
    show_rem_guess()
    return

def range1000():
    """ Button that changes range to range [0,1000) and restarts """
    restart_game(1000)
    show_rem_guess()
    return

def input_guess(guess):
    """ Handles guess input """
    global rem_guess

    # validate input
    try:
        guess_int = int(guess)
        print "You guessed: ", guess_int
    except ValueError:
        print "Please enter a valid number. "
        return

    # take 1 from guess
    rem_guess -= 1

    # evaluate
    if(guess_int == number_to_guess):
        print "Correct!"
        restart_game(guess_range)
        show_rem_guess()
        return
    elif(guess_int > number_to_guess):
        print "Lower!"
    elif(guess_int < number_to_guess):
        print "Higher!"
    else:
        print "ERROR! WHOA! That was unexpected!"
    print 
    show_rem_guess()

    return

    
# create frame
f = simplegui.create_frame("Guess the number", 300, 300)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess:", input_guess, 200)

# call new_game and start frame
new_game()
f.start()
