__author__ = 'drake'

#import random module for randomly generated things throughout program
import random
from termcolor import *


#create class that will hold defined game function
class Game():
    def __init__(self):
        #starting with a score of zero for each of the following attributes to increment and display at the end of game
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        def playable():
            cprint("Rock\n"
                   "Spock\n"
                   "Paper\n"
                   "Lizard\n"
                   "Scissors", 'blue')
            """this function prints out a list of available "playable" options for the user to pick
            in order to play against the computer, with each option beating 2 other options in the list."""
            #create list of possible answers to pull from

        def match():
            playable()
            possible = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']

            """this function is the main part of the game itself, creating a list
             of the possible options from the function playable() that can then be turned
             into the offset, which will be accessed through a matrix along with the offset of the
             option chosen by the computer randomly to determine which of the two beats the other."""

            #create dictionary to correspond with what element from "possible" list
            # corresponds with what the action does by indices

            d = {'01': 'Cuts', '12': 'Covers', '23': 'Crushes',
                 '34': 'Poisons', '40': 'Smashes', '03': 'Decapitate', '31': 'Eats',
                 '14': 'Disproves', '42': 'Vaporizes', '20': 'Crushes'}

            #get input from player on which choice they want to go with

            player_choice = raw_input(colored("Pick which one you want to play! "
                                              "Try to beat the computer! : ", 'yellow')).capitalize()

            #create option to prompt user for input if they choose something that is not an available option

            while player_choice not in possible:
                print("Invalid choice. Choose again. ")
                match()

            #create variable of index of what player chooses
            index = possible.index(player_choice)

            #create variable for randomly generated choice to be used by computer
            random_choice = random.randint(0, len(possible)-1)

            #declare the computer's choice to be the result of the random_choice variable
            computer_choice = possible[random_choice]

            print 'Player Picks: '+colored(player_choice, 'green')
            print 'Computer Picks: '+colored(possible[random_choice], 'red') + '\n'

            """todo add scoring options to the game. give number of computer wins,
            player wins, and ties after the player has decided to quit the game.(done)"""
            """todo add doc strings to functions"""

            #determining if the choices of both the user and computer are the same, resulting in a "tie"
            if random_choice == index:
                cprint("It's a tie! ", 'red', 'on_grey')

                #prompting user if they want to continue playing or exit the game
                play_again = raw_input(colored("Would you like to play again? ", 'yellow')).lower()
                self.ties += 1
                if play_again in ['y', 'yes']:
                    match()
                else:
                    cprint("Thank you for playing! ", 'yellow')
                    cprint("Your score was " + str(self.player_score) + ", and the computer's score was "
                           + str(self.computer_score),  'blue')
                    if self.ties == 1:
                        cprint("There was just " + str(self.ties) + " tie!", 'red')
                    else:
                        cprint("There were " + str(self.ties) + " ties! ", 'yellow')

            else:
                try:
                    #looking in indices of dictionary above to see if the computer's choice is the first
                    # of an index of the dictionary.
                    #if the computer's choice is first, the computer would win and the following code executed.

                    result = d[str(random_choice) + str(index)]
                    print computer_choice + ' ' + result + ' ' + player_choice + '.' + \
                        colored(' Computer wins!', 'red', 'on_grey')
                    self.computer_score += 1
                    play_again = raw_input(colored("Would you like to play again? ", 'yellow')).lower()
                    if play_again in ['y', 'yes']:
                        match()
                    else:
                        cprint("Thank you for playing! ", 'yellow')
                        cprint("Your score was " + str(self.player_score) + ", and the computer's score was "
                               + str(self.computer_score),  'blue')
                        if self.ties == 1:
                            cprint("There was just " + str(self.ties) + " tie!", 'red')
                        else:
                            cprint("There were " + str(self.ties) + " ties! ", 'yellow')

                except:
                    #if the user's choice is the first of the index of the dictionary above,
                    # the following code would be executed.

                    result = d[str(index) + str(random_choice)]
                    print player_choice + ' ' + result + ' ' + computer_choice + '.' + \
                          colored(' Player Wins!', 'green')
                    self.player_score += 1
                    play_again = raw_input(colored("Would you like to play again? ", 'yellow')).lower()
                    if play_again in ['y', 'yes']:
                        match()
                    else:
                        cprint("Thank you for playing! ", 'yellow')
                        cprint("Your score was " + str(self.player_score) + ", and the computer's score was "
                               + str(self.computer_score),  'blue')
                        if self.ties == 1:
                            cprint("There was just " + str(self.ties) + " tie!", 'red')
                        else:
                            cprint("There were " + str(self.ties) + " ties! ", 'yellow')

        match()

Game()
