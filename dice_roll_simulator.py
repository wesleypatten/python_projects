import random

def dice_roll():
    roll = random.randint(1,6)
    return roll



def dice_game():
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        player_roll = dice_roll()
        computer_roll = dice_roll()
        if player_roll == computer_roll:
            print("It's a tie")
        elif player_roll > computer_roll:
            print("Player wins!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"{player_score} - {computer_score}")
    if player_score == 5:
        print("You have won the game")
    else:
        print("The computer has won the game")


if __name__ == "__main__":
    dice_game()