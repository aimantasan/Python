import random

while True:
    choices = ["rock","paper","scissors"]   # Choice of Rock,Paper,Scissors
    computer = random.choice(choices)       # Create computer AI for random choice
    player = None                           # Initialize value with None

    while player not in choices:
        player = input("Rock, Paper or Scissors? :").lower() # Set input to always be in lower form

    if player == computer:                      # Conditional Statement if Tie
        print("Computer: ", computer)
        print("Player: " ,player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":                 # Conditiuonal Statement if Lose (Rock)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Lose!")
        if computer == "scissors":              # Conditional Statement if Win (Rock)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Win!")

    elif player == "paper":
        if computer == "scissors":                 # Conditional Statement if Lose (Paper)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Lose!")
        if computer == "rock":              # Conditional Statement if Win (Paper)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Win!")

    elif player == "scissors":
        if computer == "rock":                 # Conditional Statement if Lose (Scissors)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Lose!")
        if computer == "paper":              # Conditional Statement if Win (Scissors)
            print("Computer: ", computer)
            print("Player: " ,player)
            print("You Win!")

    play_again = input("Play Again? (yes/no):").lower()
    if play_again != "yes":
        break

print("bye")
        




