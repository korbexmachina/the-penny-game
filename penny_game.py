# Short python script to act as the predictor for the penny game
# Author: Korben Tompkin
# Date: 2023-12-08

import random
import time

def main() -> None:
    # Variables
    player_score = 0
    computer_score = 0
    try:
        rounds = int(input("How many rounds would you like to play?\nRounds: "))
        print("\n---------------------------------------\n")
    except ValueError:
        print("Invalid number of rounds. Please try again.")
        rounds = int(input("How many rounds would you like to play?\nRounds: "))
        print("\n---------------------------------------\n")

    if rounds <= 0:
        print("Rounds must be greater than 0. Please try again.")
        exit(0)

    # Game Loop
    for i in range(rounds):
        random.seed(time.time()) # Seed the random number generation

        if random.randint(0, 1) == 1:
            prediction = "H"
        else:
            prediction = "T"

        player_choice = input("What is your choice for this round? (H/T)\nYour choice: ")

        while player_choice != "H" and player_choice != "T":
            print("Invalid choice. Please try again.")
            player_choice = input("What is your choice for this round? (H/T)\nYour choice: ")

        print(f"I predicted {prediction}")

        if player_choice == prediction:
            print("I win this round!")
            computer_score += 1
        else:
            print("You win this round!")
            player_score += 1

        print(f"Current Scores:\nPlayer: {player_score}\nComputer: {computer_score}\n")
        print("---------------------------------------\n")

    # Print Results
    print(f"Final Scores:\nPlayer: {player_score}\nComputer: {computer_score}\n")

    if player_score == computer_score:
        print("It's a draw!")
    elif player_score < computer_score:
        print("I won the game!")
    elif player_score > computer_score:
        print("You won the game!")
    print("\n---------------------------------------")

main()
