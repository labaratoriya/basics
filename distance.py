
# Create a program which will ask the user for a distance and whether you will be travelling on Motorway,
# A-road or through town for the duration of travel.
# The program should output the minimum amount of time it will take to reach that distance.
# fizika http://drzavna-matura.com/index.php?topic=73.8

# Napravi program koji ce pitati korisnika za udaljenost koju ce putovati autocestom,
# A-cesta ili kroz grad za vrijeme putovanja.
# Program treba izbaciti minimalno vrijeme koje ce biti potrebno za prijeci tu udaljenost.

import time
from datetime import date
today = date.today()

def main():
    print today
    print ("formula brzina(v), duzina(s), vrijeme(t): v=s*t / s=v*t / t=s/v ")
    print ("1 m/s = 3.6 km/h")
    print ("1 km = 1000 m")

    s = int(raw_input("DUZINA(m): "))
    v = int(raw_input("BRIZINA m/S"))
