import math

def add(n1,n2):
    return n1 + n2

def multiply(n1,n2):
    return n1 * n2

def subtract(n1,n2):
    return n1 - n2

def divide(n1,n2):
    return n1 / n2

def square_root(n):
    return math.sqrt(n)

def square(n):
    return math.pow(n,2)

def sine(n):
    # answer is in radians
    return math.sin(n)

def cosine(n):
    # answer is in radians
    return math.cos(n)

def tangent(n):
    # answer is in radians
    return math.tan(n)

complex_operations = {
    "1" : square_root,
    "2" : square,
    "3" : sine,
    "4" : cosine,
    "5" : tangent,}

simple_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,}

def simple_calculator():
    num1 = float(input("First number: "))
    should_continue_simple = True
    while should_continue_simple:
        for symbol in simple_operations:
            print(symbol)
        simple_operation_symbol = input("Pick an operation: ")
        simple_calculation = simple_operations[simple_operation_symbol]
        num2 = float(input("Next number: "))
        simple_answer = simple_calculation(num1,num2)
        print(f"{num1} {simple_operation_symbol} {num2} = {simple_answer}")

        continue_simple_calc = input(f"Type 'y' to continue with {simple_answer} or 'n' to start a new calculation: ")
        if continue_simple_calc == 'y':
            num1 = simple_answer
        else:
            should_continue_simple = False

def complex_calculator():
    num = int(input("Enter the number: "))
    should_continue_complex = True
    while should_continue_complex:
        print("1.Square root\n2.Square\n3.Sine\n4.Cosine\n5.Tangent")
        complex_operation_symbol = input("Pick an operation (using numbers): ")
        complex_calculation = complex_operations[complex_operation_symbol]
        complex_answer = complex_calculation(num)
        print(f"'{num}' under operation {complex_operation_symbol} = {complex_answer}")
        continue_complex_calc = input(f"\nType 'y' to continue with {complex_answer}, 'n' to start a new calculation or 'q' to quit: ")
        if continue_complex_calc == 'y':
            num = complex_answer
        elif continue_complex_calc =='n':
            complex_calculator()
        else:
            quit()

always_on = True
while always_on:
    choice = int(input("how many numbers are you working with? "))
    if choice > 1:
        simple_calculator()
    else:
        complex_calculator()
    
input()


