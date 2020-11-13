# Rock, Paper, Scissors game
import random

options = ["rock", "paper", "scissors"]
computersChoice = random.choice(options)
print("Welcome to Rock, Paper, Scissors")
print("What do you choose?")
print(" ")
print("-----------------------------------")


playAgain = input("Ready to play? yes or no?")
while playAgain == "yes":
    myChoice = input("What did you pick? ")
    if(myChoice == computersChoice):
        print("Its a tie!")
    elif(myChoice == "rock" and computersChoice == "scissors"):
        print("You Won!")
    elif(myChoice == "paper" and computersChoice == "rock"):
        print("You Won!")
    elif (myChoice == "scissors" and computersChoice == "pyaper"):
        print("You Won!")
    elif(myChoice == "paper" and computersChoice == "scissors"):
        print("You Lost")
    elif(myChoice == "scissors" and computersChoice == "rock"):
        print("You Lost")
    elif(myChoice == "rock" and computersChoice == "paper"):
        print("You Lost")
    else:
        print("no one won")
    print(" ")
    playAgain = input("Ready to play? yes or no?")
    if playAgain == "no":
        break


