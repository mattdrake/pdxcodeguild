__author__ = 'drake'

#import random module for computer generated number
import random


#function to call the game. starts with a variable guesses at 1 so as to have correct number of tries displayed.
def play():
    guesses = 1
    number = random.randrange(1, 51)
#prints line from computer to let the user know how many tries, and to get input.
    print("I'm thinking of a number between 1 and 50. Try to guess! You only get 7 tries. ")
    choice = input("Please choose a number between 1 and 50 . ")
    while choice != number and guesses < 7:
#if the user input is lower than the generated number, prints following lines.
        if choice < number:
            print("\033[1;34mPlease guess higher\033[1;m .")
            print("You have " + str(7 - guesses) + " guesses left. ")
#if the user input is higher than generated number, prints following lines
        else:
            print("\033[1;34mPlease guess lower\033[1;m. ")
            print("You have " + str(7 - guesses) + " guesses left. ")
        choice = input("Please choose a number between 1 and 50. ")
        guesses += 1

#reachd end of maximum allowed guesses. prints what number was, then prompts for new game.
    if guesses == 7:
        print("Sorry. You have reached the maximum guesses allowed. ")
        print("The number was " + str(number))
        play_again = raw_input("Would you like to play again? Yes or No ").lower()
        if play_again == 'yes':
            play()
        else:
            print("Thank you for playing! ")
#prints how many guesses it took user to get correct number. prompts for new game
    else:
        print("You guessed it in " + str(guesses) + " tries!")
        play_again = raw_input("Would you like to play again? Yes or No ").lower()
        if play_again == 'yes':
            play()
        else:
            print("Thank you for playing! ")

play()







