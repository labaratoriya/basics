# Write a function that asks the user to input a number between 1 and 20.
# Give a response which indicates if the number is either within the range, too high or too low.

def main():
    number = int(raw_input("Input a number"))
    if number >20:
        print("Number is too high")
    elif number <1:
        print("Number is too low")
    elif number >1:
        print("Number is in the range")
    else:
        print("Number is still in the range")
