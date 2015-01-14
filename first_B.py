# Exercise 2 Basics
# Input two whole numbers, add them together and print the result to the screen.

def main():
    number1 = int(raw_input("Enter your first number"))
    number2 = int(raw_input("Enter your second number"))

    sumOfnumbers = number1 + number2
    print("{0} + {1} = {2}".format(number1,number2,sumOfnumbers))
