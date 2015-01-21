# Ask the user to enter the current month, the program should output whether the month is
# in Winter, Spring, Summer or Autumn.

def main():
    print ("Enter the current month")
    curMonth = raw_input()
    print curMonth

    if curMonth == "1":
        print ("Zima je - Sijecanj")
    elif curMonth == "2":
        print ("Sredina zime je - Veljaca")
    elif curMonth == "3":
        print ("Zima je skoro gotova - Ozujak")
    elif curMonth == "4":
        print ("Proljece je - Travanj")
    elif curMonth == "5":
        print ("Sredina proljeca je - mjesec Svibanj")
    elif curMonth == "6":
        print ("Kraj proljecea je - mjesec Lipanj")
    elif curMonth == "7":
        print ("Ljeto je - summer time mjesec Srpanj")
    else:
        print ("Neko drugo godisnje doba")

