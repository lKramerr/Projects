import random

#Decision Variable
str_input = ""

#List
list_dice = [1, 2, 3, 4, 5, 6]

#Boolean Variables
bool_loop = True

def main(bool_loop):
    print("")
    print("**********************")
    print("Dice Rolling Simulator")
    print("**********************")
    
    while bool_loop:
        print("\nDo you want to roll the dice?")
        str_input = str(input("(y/n) ")).lower()
        
        if str_input == 'y' or str_input == 'yes' or str_input == 'yeah':
            print("")
            print("::: " + str(random.choice(list_dice)) + " :::")
            
        elif str_input == 'n' or str_input == 'no' or str_input == 'nop':
            bool_loop = False

main(bool_loop)