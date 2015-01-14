# Write a program that will ask the user for four integer numbers
# Then add these numbers together before displaying the answer

def main():
    num1 = int(raw_input("Num1 "))
    num2 = int(raw_input("Num2 "))
    num3 = int(raw_input("Num3 "))
    num4 = int(raw_input("Num4 "))

    summary = num1 + num2 + num3 + num4
    print "zbroj svih unesenih brojeva je: ", summary
