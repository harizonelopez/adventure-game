# Dev_@ladinh production
# an adventure game

import time

my_size = 2
my_list = []

def validate_word(word):
    return word.isalpha() and len(word) >= 1

def validate_number(number):
    return number.isdigit() and int(number) >= 1

def validate_name(name):
    forbidden_names = ["kevo", "brayo", "franko", 
                   "bravo", "stivo", "shee"]
    return name not in forbidden_names

def run_again():
    print("**PLAY AGAIN**")
    response = get_user_input("Do you wannah play again (yes/no)\n:-> ",
                              validation_function=lambda x: x in ["yes", "no"],
                              error_message="ERROR!! Invalid input? Try again.",).lower()
    if response == "yes":
        main()
        
    else:
        print(" >>>Cool, welcome next time to the game.\n")
        quit()
    
def get_user_input(prompt, validation_function=None, 
                   error_message="ERROR!! The name is forbidden as an input. Try again."):
    while True:
        user_input = input(prompt).strip().lower()
        if not user_input:
            print("ERROR!! Please enter a valid response.")
            continue
        if validation_function and not validation_function(user_input):
            print(error_message)
            continue
        return user_input

def introduction():
    print(" >>Welcome to the adventure game!")
    time.sleep(1)
    print(" >>You find yourself in a mysterious land.")
    time.sleep(1)
    print(" >>Your goal is to navigate through challenges and reach the treasure kept at a specific place.")
    time.sleep(1)
    print(" >>Let the adventure begin!")
    
def signUp():
    print("\n***ADVENTURE GAME***\nWelcome to the adventure game, you need to sign-up & login to play the game\nEnjoy pall")
    print("\n**Sign Up**")
    for i in range(my_size):
        name = get_user_input("Enter your name\n:-> ",
                                validation_function=validate_name,
                                error_message="ERROR!! The name is forbidden as an input. Try again.")
        my_list.append(name)
    
    user_name = None    
    print("\n**Log In**")
    while user_name not in my_list:
        user_name = get_user_input("Enter your user name\n:-> ",
                                   validation_function=validate_word,
                                   error_message="ERRROR!! Strange input detected. Try again.")
        
        if user_name in my_list:
            print(f"\nHey {user_name}, you have succesfully logged in to the adventure game.")
            introduction()
            
        else:
            print("ERROR!! Incorrect username entered? Try again.")
        
def choose_path():
    print("\n**PATH SELECTION**\nChoose your path:")
    print("1. Enter the dark forest.")
    print("2. Cross the raging river.")
    print("3. Climb the steep mountain.")

    choice = get_user_input(">>Enter the number of your choice\n:-> ",
                            validation_function=validate_number,
                            error_message="ERROR!! Incorrect entry? Try again.")
    return choice
    
def dark_forest():
    print("\n**THE DARK FOREST**\nYou enter the dark forest...")
    time.sleep(1)
    print(" >>>It's full of mysterious creatures and twisted trees.")
    time.sleep(1)
    print(" >>>You see a fork in the path ahead of you.")

    fork_choice = get_user_input("Which path do you choose? (left/right)\n:-> ",
                                 validation_function=lambda x: x in ["left", "right"],
                                 error_message="ERROR!! Invalid input? Try again.").lower()

    if fork_choice == "left":
        print(" >>>You encounter a friendly elf who guides you through the forest..\n >>>Proceed to level two")
        return True
    else:
        print(" >>>You stumble upon a group of goblins. They chase you away.\n")
        return False
    
def raging_river():
    print("\n**THE RAGING RIVER**\nYou reach the raging river...")
    time.sleep(1)
    print(" >>>The water is fast and dangerous.")
    time.sleep(1)
    print(" >>>You notice a rickety bridge to your left and a sturdy boat to your right.")

    river_choice = get_user_input("Choose one of these ways to take you to the other side (bridge/boat)\n:-> ",
                                  validation_function=lambda x: x in ["boat", "bridge"],
                                  error_message="ERROR!! Invallid input detected. Try again.").lower()

    if river_choice == "boat":
        print("You successfully navigate the river with the boat.\n >>>Proceed to level 3")
        return True
    else:
        print("The bridge collapses under your weight.You drawn and asks for help.")
        return False
    
def steep_mountain():
    print("\n**THE STEEP MOUNTAIN**\nYou start climbing the steep mountain...")
    time.sleep(1)
    print(" >>>The air gets thinner, and then the climb becomes challenging.")
    time.sleep(1)
    print(" >>>You encounter a cave entrance and a narrow ledge.")

    mountain_choice = get_user_input("Do you want to enter the cave or take the narrow ledge? (cave/ledge)\n:-> ",
                                     validation_function=lambda x: x in ["cave", "ledge"],
                                     error_message="ERROR!! Invallid input detected, Try again.").lower()

    if mountain_choice == "ledge":
        print(" >>>You navigate the narrow ledge and reach the summit.\n >>>Proceed to the final level of the game")
        return True
    else:
        print("The cave is home to a sleeping dragon. You quietly retreat back.")
        return False
    
def treasure_room():
    print("\n**THE TREASURE ROOM**\n >>>Congratulations! You have reached the treasure room at last which is the final level.")
    time.sleep(1)
    print(" >>>Hurray!! You are rewarded handsomely with untold riches.")
    time.sleep(1)
    print(" >>>Congrats, You have successfully completed the adventure game having completed all the levels.!\n")
    
def main():
    signUp()
    
    #stage 1
    path_choice = choose_path()
    if path_choice == "1":
        if dark_forest():
            
            #stage 2
            path_choice = choose_path()
            if path_choice == "2":
                if raging_river():
                    
                    #stage 3
                    path_choice = choose_path()
                    if path_choice == "3":
                        if steep_mountain():
                            treasure_room()
                            run_again()
                    else:
                        print("You chose the wrong path and got lost. Game over.\n")
                        run_again()
                else:
                    print("You failed to cross the river. Game over.\n")
                    run_again()
            else:
                print("You chose the wrong path and got lost. Game over.\n")
                run_again()
        else:
            print("You were not able to navigate the dark forest. Game over.\n")
            run_again()
    else:
        print("You chose the wrong path and got lost. Game over.\n")
        run_again()
        
if __name__ == "__main__":
    main()
                            
