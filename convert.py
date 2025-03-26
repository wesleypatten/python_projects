def temperature_converter():
    print("Welcome to the temperature converter!")
    print("1. Fahrenheit to Celsius")
    print("2. Fahrenheit to Kelvin")
    print("3. Celsius to Fahrenheit")
    print("4. Celsius to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Kelvin to Celsius")

    choice = input("Enter the number of your choice: ")
    if choice == "1":
        fahrenheit = float(input("Enter temparature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}F is {celsius}C")

    elif choice == "2":
        fahrenheit = float(input("Enter temparature in Fahrenheit: "))
        kelvin = ((fahrenheit - 32) * (5/9)) + 273.15
        print(f"{fahrenheit}F is {kelvin}K")

    elif choice == "3":
        celsius = float(input("Enter temparature in Celsius: "))
        fahrenheit = (celsius * (9/5)) + 32
        print(f"{celsius}C is {fahrenheit}F")

    elif choice == "4":
        celsius = float(input("Enter temparature in Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}C is {kelvin}K")

    elif choice == "5":
        kelvin = float(input("Enter temparature in Kelvin: "))
        fahrenheit = ((kelvin - 273.15)*(9/5)) + 32
        print(f"{kelvin}K is {fahrenheit}F")

    elif choice == "6":
        kelvin = float(input("Enter temparature in Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K is {celsius}C")

if __name__ == "__main__":

    temperature_converter()