import math
# function for addition
def addition(a,b):
    return a + b

# function for subtraction
def subtraction(a,b):
    return a - b

# function for multiplication
def multiplication(a,b):
    return a * b

# function for division
def division(a,b):
    if b == 0:
        return "Error: Division by Zero"

# calculation function
def calculation(op,num1,num2):
    if op == "+":
        return addition(num1,num2)
    
    elif op == "-":
        return subtraction(num1,num2)
    
    elif op == "*":
        return multiplication(num1,num2)
    
    elif op == "/":
        return division(num1,num2)
    
    else:
        return "Error: Invalid Operation"

# getting user input    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
op = input("Enter an operation to perform, '+','-','*','/'")


if __name__ == "__main__":
    # assigning result to the called function, printing the result.
    result = calculation(op,num1,num2)
    print(result)