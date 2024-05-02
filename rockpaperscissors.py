import random

player_wins = 0
computer_wins = 0

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in ["rock", "paper", "scissors"]:
        continue