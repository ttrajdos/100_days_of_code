import art
from os import system

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multipication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Can't divide by 0"
    return a / b

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multipication,
    "/" : division
}


def calculator():
    print(art.calculator)
    first_number = float(input("What's the first number?: "))

    while True:
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))
        
        result = operations[operation](first_number, second_number)

        print(f"{first_number} {operation} {second_number} = {result}")

        decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new calculation: ")

        if decision == 'n':
            system('clear')
            calculator()

        first_number = result

calculator()





