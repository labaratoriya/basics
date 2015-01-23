# Ask the user to enter the current month
# the program should output whether the month is in
# Winter, Spring, Summer or Autumn

def main():
    print ("--------------------")
    print ("Seasons")
    print ("This program will asks for month a number and than displays the season")
    print ("--------------------")

    month = int(raw_input("Please enter the month number: "))
    print ("--------------------")

    if month == 1 or month == 2 or month == 12:
        print ("This month is in winter")
    elif month == 3 or month == 4 or month == 5:
        print ("This month is in Spring")
    elif month == 6 or month == 7 or month == 8:
        print ("This month is in Summer")
    elif month == 9 or month == 10 or month == 11:
        print ("This month is in Autumn")
    else:
        print ("You have entered an invalid month number")
