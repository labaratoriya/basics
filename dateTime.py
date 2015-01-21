# more info https://docs.python.org/2/library/time.html#module-time

from time import gmtime, strftime

def main():
    print ("------------------------------------------------")
    print strftime("Locale`s full weekday name : %A")
    print strftime("Locale`s abbreviated weekday name %a")
    print strftime("Trenutno vrijeme je: %H:%M:%S")
    print strftime("Week number of the year: %U")
    print strftime("Locale`s full month name: %B")
    print strftime("Month as a decimal number: %m")
    print strftime("Locale`s equivalent of either AM or PM: %p")
    print strftime("Day of the year as a decimal number: %j")
    print strftime("Locales appropriate time representation: %X")
    print strftime("Locales appropriate date representation: %x")
    print ("------------------------------------------------")
