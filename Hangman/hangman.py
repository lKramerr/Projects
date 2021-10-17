import gamemode

str_menu = ""
bool_menu = True

def play():
    print("")
    print("Select difficulty")
    print("[E]asy")
    print("[M]edium")
    print("[H]ard")
    print("\nLetter: ")

    while bool_menu:

        str_menu = input().lower()

        if str_menu == 'e' or str_menu == 'easy':
            print("Coming soon!")
        elif str_menu == 'm' or str_menu == 'medium':
            print("Coming soon!")
        elif str_menu == 'h' or str_menu == 'hard':
            gamemode.hardmode()
            break

def menu():
    print(
    """     _______
     I    l
     I    l
     I HANGMAN
     I
     I
     I
 ---------"""
    )

    print("  [P]lay")
    print("  [E]xit")
    print("\n  Letter: ", end = "")

    while bool_menu:
        str_menu = input().lower()

        if str_menu == "p" or str_menu == "play":
            play()
            break
        elif str_menu == "e" or str_menu == "exit":
            print("Bye, bye!")
            break

menu()
