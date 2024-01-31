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
    print(" >>Your goal is to navigate through challenges and reach the treasure hidden.")
    time.sleep(1)
    print(" >>May your decisions be wise and your journey adventures!\n")
    
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
    print("1. Cross the Raging river.")
    print("2. Help the stranger.")
    print("3. Enter the Dark forest.")
    print("4. Cross the Rugged road.")
    print("5. Take a nap")
    print("6. Pick the Box.")
    print("7. Climb the Steep mountain.")

    choice = get_user_input(">>Enter the number of your choice\n:-> ",
                            validation_function=validate_number,
                            error_message="ERROR!! Invallid input detected, Try again.")
    return choice
    
def dark_forest():
    print("\n**THE DARK FOREST**\nYou enter a dark forest...")
    time.sleep(1)
    print(" >>>It's full of mysterious creatures and twisted trees.")
    time.sleep(1)
    print(" >>>You see two paths, one to the left and one to the right.")

    fork_choice = get_user_input("Which path do you choose? (left/right)\n:-> ",
                                 validation_function=lambda x: x in ["left", "right"],
                                 error_message="ERROR!! Invalid input? Try again.").lower()

    if fork_choice == "left":
        print(" >>>You encounter a friendly elf who guides you through the forest..\n >>>Proceed to level two")
        return True
    else:
        print(" >>>You stumble upon a group of goblins. They chase you away. Game over\n")
        return False
    
def raging_river():
    print("\n**THE RAGING RIVER**\nYou reach a raging river...")
    time.sleep(1)
    print(" >>>The water is flowing fast and it's dangerous.")
    time.sleep(1)
    print(" >>>You notice a rickety bridge to your left and a sturdy boat to your right.")

    river_choice = get_user_input("Choose one of these ways to take you to the other side of the river (bridge/boat)\n:-> ",
                                  validation_function=lambda x: x in ["boat", "bridge"],
                                  error_message="ERROR!! Invallid input detected. Try again.").lower()

    if river_choice == "boat":
        print(" >>>You successfully navigate the river with the boat to the other side.\n >>>Proceed to level 3")
        return True
    else:
        print(" >>>The bridge collapses under your weight.You drawn and asks for help. Game over")
        return False
    
def steep_mountain():
    print("\n**THE STEEP MOUNTAIN**\nYou start climbing the steep mountain...")
    time.sleep(1)
    print(" >>>The air gets thinner, and then the climb becomes challenging.")
    time.sleep(1)
    print(" >>>You encounter a cave entrance and a narrow ledge.")

    mountain_choice = get_user_input("Do you want to enter the cave or take the narrow ledge route? (cave/ledge)\n:-> ",
                                     validation_function=lambda x: x in ["cave", "ledge"],
                                     error_message="ERROR!! Invallid input detected, Try again.").lower()

    if mountain_choice == "ledge":
        print(" >>>You navigate the narrow ledge and reach the summit.\n >>>Proceed to level 4")
        return True
    else:
        print(" >>>The cave is home to a sleeping dragon. You quietly and stealthily retreat back.")
        return False
    
def rugged_road():
    print("\n**THE RUGGED ROAD**\nYou need to cross the road to the other side...")
    time.sleep(1)
    print(" >>>The road has so many pot-holes and muddy at the same time.")
    time.sleep(1)
    print(" >>>There is no traffic at the moment making the road to be clear.")
    
    road_choice = get_user_input("Do you cross the road or stop your journey? (stop/cross)\n:-> ",
                                 validation_function=lambda x: x in ["stop", "cross"],
                                 error_message="ERROR!! Invallid input detected. Try again.").lower()
    
    if road_choice == "stop":
        print(" >>>You decline crossing the road and a stranger/'help' appears.\n >>>Proceed to level 5")
        return True
    else:
        print(" >>>You try to cross the road and suddenly you got stuck in mud and tanker appears to be coming from the other end, guess what next..")
        return False
    
def help_starnger():
    print("\n**THE STRANGER**\nYou need to interact with the stranger...")
    time.sleep(1)
    print(" >>>You ask the stranger of a shortcut you can use to get to the other side of the road.")
    time.sleep(1)
    print(" >>>The stranger demands you to throw your precious phone away to the muddy road.")
    
    help_choice = get_user_input("Do you accept the stranger's demand? (no/yes)\n:-> ",
                                 validation_function=lambda x: x in ["yes", "no"],
                                 error_message="ERROR!! Invallid input detected. Try again.").lower()
    if help_choice == "yes":
        print(" >>>You throw your phone away and the stranger offers you a way out.\n >>>Proceed to level 6")
        return True
    else:
        print(" >>>You decline the demand and the stranger robs you all your belongings")
        return False
    
def take_nap():
    print("\n**TAKE A NAP**\nYou need to rest for the long journey...")
    time.sleep(1)
    print(" >>>You are tired and need to rest a little bit.")
    time.sleep(1)
    print(" >>>You see a big nice shade of a tree nearby with a cool blowing wind.")
    
    nap_choice = get_user_input("Do you take a rest or not? (yes/no)\n:->",
                                validation_function=lambda i: i in ["yes", "no"],
                                error_message="ERROR!! Invallid input detected. Try again.").lower()
    if nap_choice == "yes":
        print(" >>>You decide to take a nap and regains energy for the rest of the journey.\n >>>Proceed to the final level of the adventure game.")
        return True
    else:
        print(" >>>You continue with the journey and gets tired and literary collapse and faints.")
        return False
    
def misterious_box():
    print("\n**THE MYSTERIOUS BOX**\nYou wake up and finds a box with you...")
    time.sleep(1)
    print(" >>>The box seems to be of a 'savings' box and made of pure bronze alloy.")
    time.sleep(1)
    print(" >>>The box is covered with thin alluminium coating and has a note written 'do not open'.")
    
    box_choice = get_user_input("Do you take the box or leave it? (take/leave)\n:-> ",
                                validation_function=lambda i: i in ["take", "leave"],
                                error_message="ERROR!! Invallid input detected. Try again").lower()
    if box_choice == "leave":
        print(" >>>You leave the box and sees a dark room infront of you and enters it. The final level.")
        return True
    else:
        print(" >>>You try to open the box it exploads damaging your eyesight.")
        return False
    
def treasure_room():
    print("\n**THE TREASURE ROOM**\n >>>Congratulations!! You have at last reached the 'treasure room' which is the final level.")
    time.sleep(2)
    print(" >>>Hurray!! You are rewarded handsomely with untold riches and gifts.")
    time.sleep(2)
    print(" >>>Congrats, You have successfully completed the adventure game!\n")
    time.sleep(2)

def main():
    signUp()
    
    # level 1
    path_choice = choose_path()
    if path_choice == "1":
        if dark_forest():
            
            # level 2
            path_choice = choose_path()
            if path_choice == "2":
                if raging_river():
                    
                    # level 3
                    path_choice = choose_path()
                    if path_choice == "3":
                        if steep_mountain():
                            
                            # level 4
                            path_choice = choose_path()
                            if path_choice == "4":
                                if rugged_road():
                                    
                                    # level 5
                                    path_choice = choose_path()
                                    if path_choice == "5":
                                        if help_starnger():
                                            
                                            # level 6
                                            path_choice = choose_path()
                                            if path_choice == "6":
                                                if take_nap():
                                                    
                                                    # the final level
                                                    path_choice = choose_path()
                                                    if path_choice == "7":
                                                        if misterious_box():
                                                            treasure_room()
                                                            run_again()
                                                    else:
                                                        print("You take the box and it exploades interfering with your eyesight making you to quit from there. Game over.\n")
                                                        run_again()
                                                else:
                                                    print("You take a nap and a lion evades you leaving you with serious wounds. You lost, Game over.\n")
                                                    run_again()
                                            else:
                                                print("You chose the wrong path and got lost. Game over.\n")
                                                run_again()
                                        else:
                                            print("You try to help the stranger and you get robbed. You lost, Game over.\n")
                                            run_again()
                                    else:
                                        print("You chose the wrong path and got lost. Game over.\n")
                                        run_again()
                                else:
                                    print("You try to cross the muddy road and get stuck and a tanker hits you to death. You lost, Game over.\n")
                                    run_again()
                            else:
                                print("You chose the wrong path and got lost. Game over.\n")
                                run_again()
                        else:
                            print("You try to climb the steep mountain and you slip rolling down-wards. You lost, Game over.\n")
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

