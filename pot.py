#jackpot tools

import random

def main():
    
    print("5 od 50")
    print("tvoja kombinacija glasi:)")
    print(random.sample([
        1,2,3,4,5,6,7,8,9,10,
        11,12,13,14,15,16,17,18,19,20,
        21,22,23,24,25,26,27,28,29,30,
        31,32,33,34,35,36,37,38,39,40,
        41,42,43,44,45,46,47,48,49,50
        ],5))
    print("2 od 10")
    print("dodatni brojevi")
    print(random.sample([
        1,2,3,4,5,6,7,8,9,10],2))
