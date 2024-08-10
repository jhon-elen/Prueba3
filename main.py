# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os

# add two numbers
def add_two_numbers(number1, number2):
    return number1 + number2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def another_function():
    print("Hello world")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    result = add_two_numbers(5, 4)
    print(result)
    another_function()
    print(os.getcwd())
    print("hola")
    print("que tal")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
