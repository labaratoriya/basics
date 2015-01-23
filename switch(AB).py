# Create a program which will allow the user to enter the state of two switches
# (either 1 (on) or 0 (off)).
# The program should work out if both switches are on and then output the message
# 'the light is on'.
# Otherwise, the program should output the message 'the light is off'.

def main():
    print ("Program asks for the state of two switches and than displays wheter the ligh is")
    print ("on or not")
    print ("_______________________")

    switchA = int(raw_input("Please enter state of switch A (1 or 0): "))
    switchB = int(raw_input("Please enter state of switch B (1 or 0): "))

    if switchA == 1 and switchB == 1:
        print ("the light is ON")
    else:
        print ("the light is OFF")
