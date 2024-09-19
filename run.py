import random
import american_countries
import asian_countries
import european_countries
import hangman_game
import os
import colorama
from colorama import Fore

def game_menu():
    """
    Function to display when you first run the program it display game menu screen.
    The menu has the options to display instructions or play the game by choosing continent.
    """
    print(r"""
     _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_|_|_/_/ _ \_\_| \_|\____|_|  |_/_/   \_\_| \_|
 / ___|  / \  |  \/  | ____|                    
| |  _  / _ \ | |\/| |  _|                      
| |_| |/ ___ \| |  | | |___                     
 \____/_/   \_\_|  |_|_____|                                               
    """)
    print("\nAre you ready to play?")
    print(f"\n1. Play The Game! \n2. How To Play")
    valid_choice = False
    while valid_choice is False:
        choice = input("\nEnter your choice (1 or 2):\n")
        valid_choice = menu_validate_choice(choice, ["1", "2"])
    if int(choice) == 1:
        category = continent()
    elif int(choice) == 2:
        get_instructions()

def menu_validate_choice(data, validate_menu):
    """
    Validate the choice from user in menu when they enter an integer
    between 1 or 2. Following Try statement will raise a error if the
    entered data isn't a integer or a number between 1 or 2.
    """
    try:
        if data not in validate_menu:
            raise ValueError(
                f"You've entered: {data}"
            )
    except ValueError as e:
            print(Fore.LIGHTRED_EX +
              f"\nInvalid data: {e}\n"
              + "Please enter again between 1 and 2...\n"
              + Fore.RESET)
            return False
    else:
            return True

def get_instructions():
    os.system('cls||clear')

    print(f"""
        You have three options of continents to choose from.
        Your goal is to guess the country by the chosen continent.

        If you guess a letter correctly, it will appear in the correct position in the word.
        If you guess incorrectly, a part of the hangman's body will be added to the drawing.

        If all parts of the hangman is shown you lose.
        If you guess the country correctly you win!
    """)
    # While loop to make sure user enters yes to continue to the next page
    while True:
        raw_input = input("Enter 'yes' to continue to the game:\n")
        try:
            if raw_input == "yes":
                continent()
                break
        except ValueError:
                print("Please enter 'yes to continue...")
                continue



def continent():
    """
    Function to manage the selection of continent by user to play the game.
    This function presents a list of continents for the player to choose from and
    filter countries or other elements by the chosen continent.
    """
    os.system('cls||clear')

    while True:
        try:
            user_choice = int(input(
                "Select one continent from the following options to play with:\n\n"
                " 1: America\n"
                " 2: Asia\n"
                " 3: Europe\n\n"
                " Enter a number between 1 and 3: "))
            if 1 <= user_choice <= 3:
                break
            else:
                print('Ops! You entered an invalid number. Try again\n\n')
        except ValueError:
            print('Please enter a number between 1 and 3.\n\n')
    return user_choice



def generate_country():
    """
    Function to generate a random country from the chosen continent by user.
    The function randomly chooses a country from the continent files that the player has to guess in the game.
    """
    pass

def guess_letter():
    """
    Prompts the player to guess a letter as part of a country generated in the game.
    This function ensures the player inputs a valid single character.
    """
    pass

def validate_letter():
    """
    Validates whether the guessed letter is present in the secret country.
    This function checks if the guessed letter exists in the current country 
    being guessed and make sures the user entered a singular letter and no other character.
    """
    pass

def get_back_menu():
    """
    Function to redirect user back to game menu.
    """
    pass

def play_again():
    """
    Asks the player if they want to play another round after the game ends.
    This function prompts the player to choose whether to restart the game or quit 
    after winning or losing.
    """
    pass

def main():
    """
    The main function that runs the overall game.
    This function calls all other necessary functions such as the game menu, continent
    selection, country generation, letter guessing, and checking for win/loss conditions.
    It keeps the game running in a loop until the player chooses to quit.
    """
    game_menu()
    

main()
