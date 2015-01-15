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

def main():
    print("------------------------------------------------")
    print("-------------------VOYAGER----------------------")
    print("------------------------------------------------")
    print("Nalazis se u svemirskom brodu, negdje u svemiru ")
    print("------------------------------------------------")
    print("Trazis put kuci")
    print("------------------------------------------------")
    print("Pokusavas pronaci pravi put do zemlje")
    print("------------------------------------------------")
    print("Pokrecem igru ...")
    time.sleep(2)
    print("------------------------------------------------")
    print("Pokrecem navigaciju...")
    time.sleep(2)
    print("------------------------------------------------")
    time.sleep(3) 
    print("Pokrecem warp pogon i pripremam se za putovanje")
    print("------------------------------------------------")
    time.sleep(2)
    print("Mozes upaliti warp(1) warp (2)")
    answer = int(raw_input("---> Odaberi warp pogon ... "))
    print("Odabrao si ",answer," Sto ce se dogoditi?")
    print("------------------------------------------------")
    time.sleep(2)
    print("Ulazim u warp ...")
    time.sleep(2)
    print("Prosli smo nekoli suncevih sistema ...")
    time.sleep(3)
    if answer == 2:
        print("...odjednom se pojavila crna rupa povukla brod u svoju jezgru, nitko te vise nije vidio....")
    else:
        print("...tvoj brod je zaustivio su zaustavili Romulanci")
        time.sleep(2)
        print("......................................")
        print("Romulanci te zovu na ekran")
        

    # end of program
