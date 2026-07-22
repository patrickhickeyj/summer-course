#Lesson 5 practice stuff

import random
import math

userwin = 0
compwin = 0

def getnumbergames():
    usernum = int(input("Best of how many games? "))
    while ((usernum % 2 == 0) or (not usernum < 10) or (not usernum > 0)):
        usernum = int(input("Give a valid input (odd int, 1-9) "))
    return usernum

gamenum = getnumbergames()

#Constant
valid = ["paper", "rock", "scissors"]

def getuserguess():
    userguess = input("Pick rock, paper, or scissors: ")
    while userguess not in valid:
        userguess = input("Pick rock, paper, or scissors: ")
    return userguess

def getcompguess():
    return random.choice(valid)

def decidewinner(user, comp):
    global userwin
    global compwin
    print(f'Your pick is {user}, my pick is {comp}')
    if user == comp:
        print(f"Tie!")
    elif user == "rock":
        if comp == "paper":
            print("You lose!")
            compwin = compwin + 1
        else:
            print("You win")
            userwin = userwin + 1
    elif user == "paper":
        if comp == "scissors":
            print("You lose!")
            compwin = compwin + 1
        else:
            print("You win")
            userwin = userwin + 1
    elif user == "scissors":
        if comp == "rock":
            print("You lose!")
            compwin = compwin + 1
        else:
            print("You win")
            userwin = userwin + 1

while (userwin < math.ceil(gamenum /2) and compwin < math.ceil(gamenum / 2)):
    decidewinner(getuserguess(), getcompguess())
    



