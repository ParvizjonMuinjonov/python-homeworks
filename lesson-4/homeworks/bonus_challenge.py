from random import choice

options = ["rock", "scissors", "paper"]


i = 0
player = 0

while i < 5 or player < 5:
    a = choice(options)
    players_choice = input("Choose one(rock, paper, scissors): ")

    if players_choice.lower() == "rock" and a == "paper":
        print("Computer won")
        i += 1
    elif players_choice.lower() == "rock" and a == "scissors":
        print("You won")
        player += 1

    elif players_choice.lower() == "scissors" and a == "rock":
        print("Computer won")
        i += 1
    elif players_choice.lower() == "scissors" and a == "paper": 
        print("You won")
        player += 1
    elif players_choice.lower() == "paper" and a == "scissors":
        print("Computer won")
        i += 1
    elif players_choice.lower() == "paper" and a == "rock":
        print("You won")
        player += 1

    else:
        print("Draw")
        continue
    if player == 5:
        print("Congrats, you won!")
        print(f"Your score: {player} and Computer's score: {i}")
        break
    elif i == 5:
        print("You lost")
        print(f"Your score: {player} and Computer's score: {i}")
        break

    
        