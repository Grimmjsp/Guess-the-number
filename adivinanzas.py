import random

win = random.randint(0, 10) # Winner random number
print("Adivina el número del 0 al 10 que estoy pensando:")

while True:           # Begin of the infinite loop
    num = int(input())  # User input

    if num == win:   # Check user input
        print("\nEnhorabuena, el número correcto es {}".format(num)) # If true
        break

    else:                               # If false
        print("[!] WRONG \n")
    
        print("Inténtalo de nuevo \n")