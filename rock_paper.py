__author__ = 'drake'

#import random module for randomly generated things throughout program
import random
from termcolor import *


#create class that will hold defined game function
class Game():
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        def playables():
            cprint("Rock\n"
                   "Spock\n"
                   "Paper\n"
                   "Lizard\n"
                   "Scissors", 'blue')
            #create list of possible answers to pull from

        def match():
            playables()
            possible = ['Scissors', 'Paper', 'Rock', 'Lizard', 'Spock']

            #create dictionary to correspond with what element from "possible" list corresponds with what the action does by indices

            d = {'01': 'Cuts', '12': 'Covers', '23': 'Crushes',
                 '34': 'Poisons', '40': 'Smashes', '03': 'Decapitate', '31': 'Eats',
                 '14': 'Disproves', '42': 'Vaporizes', '20': 'Crushes'}

            #get input from player on which choice they want to go with

            player_choice = raw_input(colored("Pick which one you want to play! Try to beat the computer! : ", 'yellow')).capitalize()

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

            print 'Player Picks: '+player_choice
            print 'Computer Picks: '+possible[random_choice] + '\n'

            """todo add scoing options to the game. give number of computer wins,
            player wins, and ties after the player has decided to quit the game."""
            """todo add doc strings to functions"""

            #determining if the choices of both the user and computer are the same, resulting in a "tie"
            if random_choice == index:
                print ("It's a tie! ")

                #prompting user if they want to continue playing or exit the game
                play_again = raw_input("Would you like to play again? ").lower()
                self.ties += 1
                if play_again in ['y', 'yes']:
                    match()
                else:
                    cprint("Thank you for playing! ", 'yellow')

            else:
                try:
                    #looking in indices of dictionary above to see if the computer's choice is the first
                    # of an index of the dictionary.
                    #if the computer's choice is first, the computer would win and the following code executed.

                    result = d[str(random_choice) + str(index)]
                    print(computer_choice + ' ' + result + ' ' + player_choice + '. Computer wins! ')
                    self.computer_score += 1
                    play_again = raw_input(colored("Would you like to play again? ", 'yellow')).lower()
                    if play_again in ['y', 'yes']:
                        match()
                    else:
                        cprint("Thank you for playing! ", 'yellow')
                        print("your score was {0}, and the computer score was {1}".format(self.player_score,
                                                                                          self.computer_score))

                except:
                    #if the user's choice is the first of the index of the dictionary above,
                    # the following code would be executed.

                    result = d[str(index) + str(random_choice)]
                    print player_choice + ' ' + result + ' ' + computer_choice + '. Player Wins! '
                    self.player_score += 1
                    play_again = raw_input("Would you like to play again? ").lower()
                    if play_again in ['y', 'yes']:
                        match()
                    else:
                        cprint("Thank you for playing! ", 'yellow')
                        print("your score was {0}, and the computer score was {1}".format(self.player_score, self.computer_score))
                        print("there were " + str(self.ties) + " ties! ")

        match()

Game()