# Dev_@ladinh production
# sign-up and login program entailing the user to enter his/her name and then logiin's in

print("\n>>>WELCOME TO THE ADVENTURES GAME<<<")
my_size = 2
my_list = []
number_list = ["1","2","3","4","5"]

def validate_name(name):
    forbidden_names = ["kevo", "brayo", "franko", 
                   "bravo", "stivo", "shee"]
    return name not in forbidden_names

def validate_number(number):
    return number.isdigit() and int(number) >= 1

def run_again(identity):
    response = get_user_input(f"\n{identity}, do wannah play again [yes or no]:-> ", 
                              validation_function=lambda x: x in ["yes", "no"],
                              error_message="ERROR!! Invalid input, respond only with 'yes' or 'no', Try again.").lower()
    if response == "yes":
        sign_up()   
    elif response == "no":
        print("^^^Cool, Welcome next time to the game^^^\n")
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
    
def sign_up():
    print("\n**Sign Up**")
    for i in range(my_size):
        name = get_user_input("Enter your name :-> ", 
                              validation_function = validate_name) 
        my_list.append(name)
        
    identity = None
    print("\n**Log In**\nLog in now")
    while identity not in my_list:
        identity = get_user_input("Enter your user name\n:-> ", 
                                validation_function = validate_name)
        if identity in my_list:
            print(f"Hey {identity}, You have succesfully logged in to the game.")
            game_logic(identity)            
        else:
            print("ERROR!! Incorrect username? Try again.")    

def game_logic(identity):
    print(f"\n**GAME LOGIC**\n{identity}, welcome to the game, you need to guess a number.")
    number_guess = get_user_input("Enter number:-> ",
                           validation_function=validate_number,
                           error_message="ERROR!! Please enter a valid number")    
    if number_guess in number_list:
        print("All is cool")   
        
sign_up()


        
        
             
        
    
        
      
    
