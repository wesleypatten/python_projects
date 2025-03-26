# This program is a simple calculator that does the four simple operations + - * / and give the answer
""" 
Psuedocode
1. Create a function to get the input of a number.
2. Create a function to get the input of an operator.
3. Create a function to carry out the calculation.
4. Create a variable to store the answer of the operation.
5. Perform the calculation and store the answer.
6. Print out the answer.
"""
def number_input():
    number = input("Enter a number: ")
    number = int(number)
    return number

def operation_choice():
    operation = input("Choose the operation you would like to perform '+' '-' '*' or '/': ")
    return operation

def calculation():
    answer = 0
    num_1 = number_input()
    operator = operation_choice()
    num_2 = number_input()

    if operator == "+":
        answer = num_1 + num_2
        print(f"The answer to {num_1} {operator} {num_2} = {answer}")
    
    elif operator == "-":
        answer = num_1 - num_2
        print(f"The answer to {num_1} {operator} {num_2} = {answer}")

    elif operator == "*":
        answer = num_1 * num_2
        print(f"The answer to {num_1} {operator} {num_2} = {answer}")

    elif operator == "/":
        try:
            answer = num_1 / num_2
            print(f"The answer to {num_1} {operator} {num_2} = {answer}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    
    else:
        print("Invalid operation.")

    
if __name__ == "__main__":
    calculation()    
