# cool site python http://www.tutorialspoint.com/python/python_numbers.htm
# Create a program which will troubleshoot printing problems.
# The program should ask questions like 'is the printer turned on?'
# and 'is there paper in the printer'.

def main():
    print("----------------------------")
    print("PRINTER TROUBLESHOOT PROBLEM")
    print("----------------------------")
    str = raw_input("cappitalize input text: ")
    print str.upper()
    print str.capitalize()
    response = raw_input("Is your printer on network (Y or N)?: ")
    print("-----------------------------------------------")
    response = response.upper()
    if response == 'N':
        print ("Check the newtwork cable is plugged in...")
        print("-----------------------------------------------")
        response = raw_input ("Did you solve this problem? (Y or N): ")
        print("-----------------------------------------------")
        if response == 'Y':
            solved = True
        else:
            solved = False
    elif response == 'Y':
        solved = False
    else:
        solved = False
        print("You need to enter either Y or N as your answer.")
        print("-----------------------------------------------")

    # question 2

    if not solved:
        response = raw_input("Is the paper inside?: ")
        print("-----------------------------------------------")
        response = response.upper()
        if response == 'N':
            print("-----------------------------------------------")
            print("Please, check the paper tray in the printer...")
            print("-----------------------------------------------")
            response = raw_input("Did you solve the problem (Y or N)?: ")
            print("-----------------------------------------------")
            if response == 'Y':
                solved = True
            else:
                solved = False
        elif response == 'Y':
            solved = False

     # question 3 to question x, reapeat above

     # final section

    if not solved:
         print("-----------------------------------------------")
         print("Sorry, this tool cant fix your printer problems")
         print("Call your technical support or administrator!")
         print("-----------------------------------------------")
