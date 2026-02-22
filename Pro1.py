#Rock,Paper and Scissors (Human Vs Computer)

import random

choose_options = ["rock", "paper", "scissors"]

print(".....Welcome to Rock, Paper, Scissors")

user_choice = input("\n Enter rock, paper, or scissors : ")
computer_choice =  random.choice(choose_options)

print("Computer Chose: " + computer_choice)

if user_choice == computer_choice :
    print("It's a tie!")

elif user_choice == "rock" :
    if computer_choice == "scissors" :
        print("You win! Rock smashes Scissors")
    else :
        print("You lose! Paper cover Rock")

elif user_choice == "paper" :
    if computer_choice == "rock" :
        print("You win! Paper covers Rock")
    else :
        print("You lose! Scissors cuts Paper")

elif user_choice == "scissors" : 
    if computer_choice == "paper" :
        print("You win! Scissors cuts Paper")
    else :
        print("You lose! Rocks smashes Scissors")

else : 
    print ("Invalid input. Please check your spelling!")
