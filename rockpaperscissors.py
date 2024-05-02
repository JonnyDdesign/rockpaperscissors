import random

player_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if player_input == "q":
        break

    if player_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2