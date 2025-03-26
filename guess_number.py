import random
def computer_guess():
    return random.randint(1, 100)

def user_guess():
    return int(input("Enter a number between 1 and 100: "))

def main():
    print("Welcome to the guessing game!")
    computer_number = computer_guess()
    user_number = user_guess()
    while user_number != computer_number:
        if user_number > computer_number:
            print("Too high!")
        else:
            print("Too low!")
        user_number = user_guess()
    print("Congratulations! You guessed"
            " the correct number!")
    
if __name__ == "__main__":
    main()