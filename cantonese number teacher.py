# program to teach you how to count from numbers zero to ten in cantonese

import random
import time

# defining functions to use

def cantonese_first():

    round = 1
    counter = 1
    wrong = 0
    revision_list_format = ""
    revision_list = []
    past_random_number = 88

    cantonese_number_list = ["lìhng", "yāt", "yih", "sàam", "sei", "nǵh", "luhk", "chāt", "baat", "gáu", "sahp"]

    print(f"In the 'Canontese First' game mode, you will be presented with a number in Cantonese to which you must respond with the correct digit. This will last for 10 rounds.\n \nLet's begin {user_name}!\n ")

    while counter <= 10:

        get_random_number = random.randint(1, 10)

        while True:
            if int(get_random_number) == int(past_random_number):
                get_random_number = random.randint(1, 10)
            else:
                break

        current_cantonese_number = cantonese_number_list[get_random_number]
        time.sleep(0.5)
        cantonese_first_answer = input(f"ROUND {round}: {current_cantonese_number}\nENTER ANSWER: ")
        while True:
            if int(cantonese_first_answer) == int(get_random_number): 
                print("CORRECT!")
                past_random_number = cantonese_first_answer
                counter += 1
                round += 1

                break
            else:
                # cantonese_first_answer = input("That's not the right, try again: ")
                print(f"INCORRECT! The digit that corresponds with {current_cantonese_number} is {get_random_number}.")
                counter += 1
                round += 1
                wrong += 1
                revision_list_format = str(current_cantonese_number) + " (" + str(get_random_number) + ")"
                revision_list.append(revision_list_format)
                break
    
    total = 10 - wrong

    def revise():
        for x in revision_list:
            print(x)

    if total >= 5:
        print(f"Well done {user_name}, you got {total} out of 10 rounds correct!\nYou shoud look to revise the following numbers: ")
        revise()
    else:
        print(f"Good try {user_name}, you got {total} out of 10 rounds correct.\nYou shoud look to revise the following numbers: ")
        revise()

def numbers_to_canontese():
    # work in progress
    pass

def game_configuration():
    game_modes = ["(1) Cantonese First // Match the outputted Cantonese number with a digit!", "(2) Numbers To Cantonese // Choose the correct Canontese pīnyīn to mirror the displayed digit! "]
    print(f"{user_name}, please view our current list of game modes and select which ever one you want to play today:\n")
    
    for x in game_modes:
        print(x)

    game_mode_selection = input("\nSELECT GAME MODE VIA THEIR CORRESPONDING NUMBER (1, 2, 3, etc): ")

    while True:
        if game_mode_selection == "1":
            print("Game mode 'Canontese First' has been selected!")
            cantonese_first()
            break
        elif game_mode_selection == "2":
            print("Game mode 'Numbers To Cantonese' has been selected!")
            numbers_to_canontese()
            break
        else:
            game_mode_selection = input("You must select using a valid number!\nSELECT GAME MODE VIA THEIR CORRESPONDING NUMBER (1, 2, 3, etc): ")

def game_intro():
    global user_name
    user_name = input("Hi there new user, what is your name?\nENTER NAME: ")
    confirm = input(f"Nice to have you here, {user_name}. Would you like to begin learning numbers in Cantonese?\nSTART GAME (Y/N): ")
    option_1 = "y"
    option_2 = "n"
    while True:
        if confirm.upper() == option_1.upper():
            game_configuration()
            break
        elif confirm.upper() == option_2.upper():
            print(f"Very well, we shall not start right now. We hope to see you soon when you're ready to learn numbers in cantonese {user_name}, take care!")
            break
        else:
            confirm = input(f"You must decide whether or not to start learning using characters 'Y' or 'N'!\nSTART GAME (Y/N): ")

# call on functions to build program below

game_intro()

