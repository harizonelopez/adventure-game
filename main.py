# Dev_@ladinh production
# an adventure game

import time

my_size = 2
my_list = []

def validate_name(name):
    forbidden_names = ["kevo", "brayo", "franko", 
                   "bravo", "stivo", "shee"]
    return name not in forbidden_names

def validate_number(number):
    return number.isdigit() and int(number) >= 1

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
    print(" Welcome to the adventure game!")
    time.sleep(1)
    print(" You find yourself in a mysterious land.")
    time.sleep(1)
    print(" Your goal is to navigate through challenges and reach the treasure kept at a specific place.")
    time.sleep(1)
    print(" Let the adventure begin!\n")
    
    
def signUp():
    print("\n**ADVENTURE GAME**\n")
    for i in range(my_size):
        name = get_user_input("**Sign Up**\nEnter your name\n:-> ",
                                validation_function=validate_name,
                                error_message="ERROR!! The name is forbidden as an input. Try again.")
        my_list.append(name)
    
    user_name = None    
    print("\n**Log In**\n")
    while user_name not in my_list:
        user_name = get_user_input("Enter your user name\n:-> ",
                                   validation_function=validate_name,
                                   error_message="ERRROR!! The name is forbidden as an input. Try again.")
        
        if user_name in my_list:
            print(f"Hey {user_name}, you have succesfully logged in to the adventure game.")
            introduction()
            
        else:
            print("ERROR!! Incorrect username entered? Try again.")
        
def choose_path():
    print("**PATH SELECTION**\nChoose your path:")
    print("1. Enter the dark forest.")
    print("2. Cross the raging river.")
    print("3. Climb the steep mountain.")

    choice = get_user_input("Enter the number of your choice:-> ",
                            validation_function=validate_number,
                            error_message="ERROR!! Incorrect entry? Try again.")
    return choice
    
def dark_forest():
    print("**THE DARK FOREST**\nYou enter the dark forest...")
    time.sleep(1)
    print("It's full of mysterious creatures and twisted trees.")
    time.sleep(1)
    print("You see a fork in the path ahead of you.")

    fork_choice = get_user_input("Which path do you choose? (left/right):-> ",
                                 validation_function=lambda x: x in ["yes", "no"],
                                 error_message="ERROR!! Invalid input? Try again.").lower()

    if fork_choice == "left":
        print("You encounter a friendly elf who guides you through the forest.")
        return True
    else:
        print("You stumble upon a group of goblins. They chase you away.")
        return False
    
def raging_river():
    print("**THE RAGING RIVER**\nYou reach the raging river...")
    time.sleep(1)
    print("The water is fast and dangerous.")
    time.sleep(1)
    print("You notice a rickety bridge to your left and a sturdy boat to your right.")

    river_choice = input("Do you want to take the bridge or the boat? (bridge/boat):-> ").lower()

    if river_choice == "boat":
        print("You successfully navigate the river with the boat.")
        return True
    else:
        print("The bridge collapses under your weight. You swim to safety side.")
        return False
    
def steep_mountain():
    print("**THE STEEP MOUNTAIN**\nYou start climbing the steep mountain...")
    time.sleep(1)
    print("The air gets thinner, and then the climb becomes challenging.")
    time.sleep(1)
    print("You encounter a cave entrance and a narrow ledge.")

    mountain_choice = input("Do you want to enter the cave or take the narrow ledge? (cave/ledge): ").lower()

    if mountain_choice == "ledge":
        print("You navigate the narrow ledge and reach the summit.")
        return True
    else:
        print("The cave is home to a sleeping dragon. You quietly retreat back.")
        return False
    
def treasure_room():
    print("**THE TREASURE ROOM**\nCongratulations! You reach the treasure room at last.")
    time.sleep(1)
    print("Hurray!! You are rewarded handsomely with untold riches.")
    time.sleep(1)
    print("Congrats, You have successfully completed the adventure game!")
    
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
                    else:
                        print("You chose the wrong path and got lost. Game over.")
                else:
                    print("You failed to cross the river. Game over.")
            else:
                print("You chose the wrong path and got lost. Game over.")
        else:
            print("You were not able to navigate the dark forest. Game over.")
    else:
        print("You chose the wrong path and got lost. Game over.")
        
if __name__ == "__main__":
    main()
                            
