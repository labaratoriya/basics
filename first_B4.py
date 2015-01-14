# Write a program that will ask the user for two numbers a then divide one by the other.
# The number of times one goes into another and the remainder should be displayed.
# For example, If 3 and 2 were entered: 3/2 = 1 remainder 1.
# The input and output should be user friendly.

def main():
    num1 = int(input("number 1:"))
    num2 = int(input("number 2: "))

    remainder = num1 % num2

    print remainder
