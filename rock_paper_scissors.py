import random
# This is a simple rock, paper, scissors game.

def computer_choice():
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    return computer_choice

def user_choice():
    player_choice=input("Enter Rock, Paper, or Scissors: ")
    player_choice=player_choice.capitalize()
    return player_choice

def round(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            return "Computer wins!"
        else:
            return "You win!"
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            return "Computer wins!"
        else:
            return "You win!"
    else:
        return "Invalid input. Try again."


def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0

    while player_score <5 and computer_score < 5:
        computer = computer_choice()
        player = user_choice()
        result = round(player, computer)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(player_score, computer_score)
        print(result)
    if player_score == 5:
        print("You win the game!")
    else:
        print("Computer wins the game, you suck!")
    

if __name__ == "__main__":

    main()



