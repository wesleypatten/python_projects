def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Error: Division by Zero"
    return a / b

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
    
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
op = input("Enter an operation to perform, '+','-','*','/'")


if __name__ == "__main__":
    result = calculation(op,num1,num2)
    print(result)