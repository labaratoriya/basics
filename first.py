# this program will say hello to you
# this program was written on January 8th

def main():
    print("What is your name?")
    yourName = raw_input()
    print("Hello {0}!".format(yourName))
    
    # now ask for user`s age
    yourAge = int(raw_input("What is your age?"))
    print("Hello {0}. You are a young {1}".format(yourName,yourAge))
