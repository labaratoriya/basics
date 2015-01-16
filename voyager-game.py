# Program maze game VOYAGER
# Your task is to extend this program to include more challenge.
# More twists and turns! Perhaps you could add three directions to choose from, or more choices to make.
# After you have made some extensions you might like to use the random function.
# This will make your program more fun as the computer will randomly decide whether the option chosen by the user
# ---------------------------------------------------
# To do this the following information will be useful.

# import randomneeds to be added at the top of the program
# random.randint(1,5) will generate a random number between 1 and 5
# random.choice(["a","b","c"]) will generate a random choice of either a, b or c
# ---------------------------------------------------

import time
import random

def main():

    print(random.choice(["put Mjeseca","put Marsa","put Jupitera"]))
    print(random.randint(1,15))
    
    print("------------------------------------------------")
    print("-------------------VOYAGER----------------------")
    print("------------------------------------------------")
    print("Pokrecem igru ...")
    time.sleep(2)
    print("Nalazis se u svemirskom brodu, negdje u svemiru ")
    print("------------------------------------------------")
    print("Trazis put kuci")
    time.sleep(1)
    print("------------------------------------------------")
    print("Pokusavas pronaci pravi put do zemlje")
    time.sleep(1)
    print("------------------------------------------------")
    print("Pokrecem navigaciju...")
    time.sleep(2)
    print("------------------------------------------------")
    print("Pokrecem warp pogon i pripremam se za putovanje")
    time.sleep(2)
    print("------------------------------------------------")
    print("Mozes upaliti warp(1) warp (2)")
    answer = int(raw_input("---> Odaberi warp pogon ... "))
    print("Odabrao si ",answer," Sto ce se dogoditi?")
    time.sleep(2)
    print("------------------------------------------------")
    print("Ulazim u warp ...")
    time.sleep(2)
    
    if answer == 2:
        print("------------------------------------------------")
        print("Iz strojarnice javljaju nestabilnost u warp jezgri ...")
        time.sleep(1)
        print("------------------------------------------------")
        print("...dogodio se nepredvidjeni zboj u warp jezgri, Voyager se zaustavio....")
        time.sleep(1)
        print("------------------------------------------------")
    else:
        print("Prosao si nekoliko svjetlosnih godina")
        print("------------------------------------------------")
        time.sleep(2)
        print("... i odjenom su tvoj brod zaustavili Izvanzemaljci")
        time.sleep(2)
        print("------------------------------------------------")
        print("... zovu kapetana na ekran")
    print(random.choice(["a","b","c"]))
        

    # end of program
