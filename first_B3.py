# Write a program that will ask the user for three integer numbers
# and then multiply the first two together before dividing the result by the third number.
# The input and output should be user friendly.

def main():
    num1 = int(raw_input('First number: '))
    num2 = int(raw_input('Second number: '))
    num3 = int(raw_input('Third number: '))
    mult = num1*num2
    divide = mult/num3

    print 'Ako pomnozimo prvi i drugi broj dobit cemo: ', mult
    print 'Kad rezultat prva dva broja podijelimo sa trecim: ', divide
