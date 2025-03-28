import random
import string

def password_generator(*password_data):
    return password_data

length =input("How many characters do you want in your password?")
while int(length) < 8 or int(length) >32:
    print("Password length must be between 8 and 32 characters")
    length = input("Enter a valid length: ")

numbers = input("Do you want want to include numbers, Yes/No:").strip().lower()
while numbers not in ["yes", "no"]:
    print("Please enter Yes or No:")
    numbers = input("Do you want want to include numbers, Yes/No:").strip().lower()

if numbers == "yes":
    numbers = string.digits
elif numbers == "no":
    numbers = None

upper = input("Do you want want to include uppercase letters, Yes/No:").strip().lower()
while upper not in ["yes", "no"]:
    print("Please enter Yes or No:")
    upper = input("Do you want want to include numbers, Yes/No:").strip().lower()

if upper == "yes":
    upper = string.ascii_letters
elif upper == "no":
    upper = string.ascii_lowercase

symbols = input("Do you want want to include symbols, Yes/No:").strip().lower()
while symbols not in ["yes", "no"]:
    print("Please enter Yes or No:")
    symbols = input("Do you want want to include numbers, Yes/No:").strip().lower()

if symbols == "yes":
    symbols = string.punctuation
elif symbols == "no":
    symbols = None

if __name__ == "__main__":
    check = list(password_generator(length, numbers, upper, symbols))
    print(check)
    password_length = int(check[0])
    data = []
    for i in check[1:]:
        if i != None:
            data.append(i)
    data = ''.join(data).strip()
    password = ''
    for i in range(0,(password_length+1)):
        password = password+random.choice(data)
    print(data)
    print(len(data))
    print(password_length)
    print(password)