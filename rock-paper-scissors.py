####################################################################################################################################################################################################################
# Rock Paper Scissors (Python 3.7)
####################################################################################################################################################################################################################

from random import randint

def main():
 choice  = ["rock", "paper", "scissors"]
 computer = choice[randint(0,2)]

 print("Lets play Rock, Paper, Scissors!\n")
 user = input("Enter your choice (Rock, Paper or Scissors): ").lower()
 print(" ")
 print(f"The Computer Chose: {computer}")

 if user == computer:
    print("Draw")
 elif user == "rock" and computer == "paper":
    print("Computer Wins")
 elif user == "rock" and computer == "scissors":
    print("User Wins")
 elif user == "paper" and computer == "rock":
    print("User Wins")
 elif user == "paper" and computer == "scissors":
    print("Computer Wins")
 elif user == "scissors" and computer == "rock":
    print("Computer Wins")
 elif user == "scissors" and computer == "paper":
    print("User Wins")
 print(" ")
 main()

main()
