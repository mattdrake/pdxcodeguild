__author__ = 'drake'

import random


class Game():
    def __init__(self):
        def rules():
            print("0 - Rock\n"
                  "1 - Spock\n"
                  "2 - Paper\n"
                  "3 - Lizard\n"
                  "4 - Scissors")

        def number_to_name():
            number = input("Pick a number to correspond with your choice of what to play! ")
            if number == 0:
                return "Rock"
            elif number == 1:
                return "Spock"
            elif number == 2:
                return "Paper"
            elif number == 3:
                return "Lizard"
            elif number == 4:
                return "Scissors"
            else:
                print("Invalid selection! Try again")

        def name_to_number():
            if number_to_name() == "Rock":
                return 0
            elif number_to_name() == "Spock":
                return 1
            elif number_to_name() == "Paper":
                return 2
            elif number_to_name() == "Lizard":
                return 3
            else:
                return 4
        def rpsls():
            computer_number = random.randint(0, 5)
            player_number = name_to_number()
            computer_name = computer_number(number_to_name())
            name = number_to_name()
            difference = (player_number - computer_number) % 5

            if difference == 0:
                result = "You tied with the computer! "
            elif difference == 1 or difference == 2:
                result = "You won! "
            else:
                result = "Aaah! The computer beat you! "

            print "Player chooses", name
            print "Computer chooses", computer_name
            print result
            if name != "Scissors":
                print


        rules()
        rpsls()

Game()






