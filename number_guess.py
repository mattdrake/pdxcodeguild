__author__ = 'drake'

#import random module for computer generated number
import random
myName = raw_input("Hi there! What's your name? ").capitalize()

#function to call the game. starts with a variable guesses at 1 so as to have correct number of tries displayed.
def play():
    points = 10
    guesses = 1
    number = random.randrange(1, 51)
#prints line from computer to let the user know how many tries, and to get input.
    print("\033[1;32mWell " + myName + ", I'm thinking of a number between 1 and 50. Try to guess! You only get 7 tries.\033[1;m ")
    choice = input("Please choose a number between 1 and 50 . ")
    #while choice > 0:
    while choice != number and guesses < 7:
#if the user input is lower than the generated number, prints following lines.
        if choice < number:
            print("\033[1;34mPlease guess higher. \033[1;m")
            print("\033[1;31mYou have " + str(7 - guesses) + " guesses left.\033[1;m ")

#if the user input is higher than generated number, prints following lines
        else:
            print("\033[1;34mPlease guess lower. \033[1;m ")
            print("\033[1;31mYou have " + str(7 - guesses) + " guesses left.\033[1;m ")
        choice = input("Please choose a number between 1 and 50. ")
        guesses += 1

#todo add bonus points for getting within 5 of the randomly generated number on the first guess
#reachd end of maximum allowed guesses. prints what number was, then prompts for new game.
    if guesses == 7 and choice != number:
        points = points + (7 - guesses)
        print("\033[1;34mSorry. You have reached the maximum guesses allowed.\033[1;m ")
        print("\033[1;31mThe number was\033[1;m " + str(number))
        print("You scored " + str(points) + " points. ")
        play_again = raw_input("\033[1;34mWould you like to play again? Yes or No \033[1;m ").lower()
        if play_again == 'yes':
            play()
        elif play_again == 'y':
            play()
        else:
            print("\033[1;31mThank you for playing!\033[1;m ")
#prints how many guesses it took user to get correct number. prompts for new game
    else:
        points = points + (7 - guesses)
        print("\033[1;34mYou guessed it in " + str(guesses) + " tries! You scored " + str(points) + " points! \033[1;m ")
        play_again = raw_input("Would you like to play again? Yes or No ").lower()
        if play_again == 'yes':
            play()
        elif play_again == 'y':
            play()
        else:
            print("\033[1;31mThank you for playing!\033[1;m ")

play()







