import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock/paper/scissors: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break