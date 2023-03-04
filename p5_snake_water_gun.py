import random

print("Welcome to Snake, Water, Gun Game!")

game_options = ["snake", "water", "gun"]

total_rounds = int(input("Enter the number of rounds you want to play: "))
player_score = 0
computer_score = 0

for round in range(total_rounds):
    print(f"Round {round + 1}:")
    player_choice = input("Enter your choice: ").lower()
    computer_choice = random.choice(game_options)
    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "snake" and computer_choice == "gun":
        print("You lost this round.")
        computer_score += 1
    elif player_choice == "snake" and computer_choice == "water":
        print("You won this round.")
        player_score += 1
    elif player_choice == "water" and computer_choice == "snake":
        print("You lost this round.")
        computer_score += 1
    elif player_choice == "water" and computer_choice == "gun":
        print("You won this round.")
        player_score += 1
    elif player_choice == "gun" and computer_choice == "snake":
        print("You won this round.")
        player_score += 1
    elif player_choice == "gun" and computer_choice == "water":
        print("You lost this round.")
        computer_score += 1
    else:
        print("Invalid choice. Please choose again.")

print("\nFinal Score:")
print(f"Player: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("You won the game!")
elif player_score < computer_score:
    print("You lost the game.")
else:
    print("It's a tie!")
