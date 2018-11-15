import random
from math import *
from operator import itemgetter

game =[]
game.sort(key=itemgetter("item"), reverse=True)

random_number = random.randint(1,10)


def game():
    while True:
             try:
               guess = int(input("Guess any number between 1 - 10:"))
             except ValueError:
                 print("That is not an integer")
             if guess == random_number:
                 print("You have guess is right,your guess was {}".format(guess))
                 break
             else:
                print("Wrong guess!")


game()
# include more guess..
def Mind_game():
    while True:
        try:
         print("Think of a number ")
         print("Double it.Add 10.Halve it,Take away you original number:")

        except ValueError:
         print("Enter integer!")

        else:
         # calc = number*2 + 10
         # calc_two = int(calc/2 - number)

         print("is your number {}".format(5))
        break


Mind_game()



