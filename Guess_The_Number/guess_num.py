import random

#List
list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Int Variables
int_random_num = random.choice(list_nums)
int_player_num = 0
int_score = 10

print("********Guess the Number game********")
int_player_num = int(input("Type one number between 1 and 10: "))

if int_player_num == int_random_num:
    print("Correct! You won!!!")
    print("Perfect Score!!!")
else:
    int_score -= 2
    if int_random_num % 2 == 0:
        print("I'm an even number!")
    else:
        print("I'm an odd number!")

    int_player_num = int(input())

    if int_player_num == int_random_num:
        print("Congratulations! You won!!!")
        print("Your score is: %d" %(int_score))
    else:
        int_score -= 1
        if int_random_num > 5:
            print("I'm greater than or equal to five!")
        else:
            print("I'm less than 5")

        int_player_num = int(input())

        if int_player_num == int_random_num:
            print("Woah! you got it! You won!!!")
            print("Your score is: %d" %(int_score))
        else:
            print("Ups, the number is %d, sorry, you lost :(" %(int_random_num))

print(int_random_num)
