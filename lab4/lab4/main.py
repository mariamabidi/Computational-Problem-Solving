__author__ = 'MA'

"""
CSCI-603 Lab 4: Wordle

A program that provides user with valid commands to play the game wordle,
user has to guess the word within six guesses, the valid commands include - 
new: Start a new game
guess <word>: Make a guess
cheat: Show the secret word
help: This is a help message
quit: End the program

Author: Mariam Abidi
"""
import linecache
import random
import sys

all_the_guesses = {}
legal_words = list()


def guess(the_word: str, guessed_word: str):
    """
    This function is used to check if the user's guessed word's characters are
    present in the secret word. Prints an empty space if the alphabet is not
    present, * if it is present but not at the correct position and ^ if it is
    at the right position.

    :param the_word: A variable to store the secret word.
    :param guessed_word: A variable to store the guessed word.
    :return:
    """
    # List to store the symbols according to the guessed word.
    guess_symbols = [' '] * 5

    # For loop to check every character.
    for user_letter in guessed_word:
        for word_letter in the_word:
            if user_letter == word_letter:
                pos = guessed_word.index(user_letter)
                if (guessed_word.index(user_letter) ==
                        the_word.index(word_letter)):
                    guess_symbols[pos] = "^"
                else:
                    guess_symbols[pos] = "*"

    # Joins the guess symbol list to print it like a string.
    collected_symbols = ''.join(guess_symbols)

    # Updating the dictionary containing all user guesses.
    all_the_guesses.update({guessed_word.upper(): collected_symbols})
    for key, value in all_the_guesses.items():
        print(key)
        print(value)


def commands():
    """
    This function prints all the valid commands.
    :return:
    """
    print("Commands:")
    print("new: Start a new game")
    print("guess <word>: Make a guess")
    print("cheat: Show the secret word")
    print("help: This is a help message")
    print("quit: End the program")


def file_read(words: str):
    """
    This function is used to read the file containing the legal words. And a
    random word is selected as a secret word if not preset.
    :param words: A variable to store the filename.
    :return: The selected secret word
    """
    user_input = len(sys.argv)
    secret_word = ""

    # Checks if the command line has a secret word
    if user_input == 1:
        with open(words) as w:
            length_of_file = len(w.readlines())
            random_integer = random.randint(1, length_of_file)
            secret_word = linecache.getline("wordle.txt", random_integer)

        with open(words) as w:
            for line in w:
                legal_words.append(line.strip())
    else:
        if len(sys.argv[1]) == 5:
            secret_word = sys.argv[1]
        else:
            print("Illegal Word")

    return secret_word


def play_game():
    """
    This function is where the actual game takes place. It checks the user
    input and runs the respective command.

    :return:
    """

    commands()
    # Random word is selected.
    selected_word = file_read("wordle.txt").upper()

    # Set to store the used alphabets.
    used_alphabets = set()
    number_of_tries = 1

    # while loop to keep track of the number of tries
    while number_of_tries < 7:
        game_start = (input("> ")).lower().split(" ")
        if game_start[0] == "new":
            all_the_guesses = {}
            main()
        elif game_start[0] == "guess" and len(game_start) == 2:
            if (len(sys.argv) == 2 and (game_start[1].upper()) ==
                    selected_word.upper()):
                guess(selected_word, game_start[1].upper())
                print("Correct Guess! You won")
                number_of_tries -= 1
            elif (game_start[1].upper()) in legal_words:

                # Updates the used alphabets set.
                for i in game_start[1]:
                    used_alphabets.add(i)

                # Checks if the secret word is provided by user.
                if (len(sys.argv) == 1 and (game_start[1].upper() + '\n') ==
                        selected_word):
                    guess(selected_word, game_start[1].upper())
                    print("Correct Guess! You won")
                    number_of_tries -= 1
                else:
                    print("Number of tries: " + str(number_of_tries) + " of 6")
                    guess(selected_word, game_start[1].upper())
                    print("Letter's used: " + str(used_alphabets))
            else:
                print("Illegal Word")
                number_of_tries -= 1

        # If command contains only guess word.
        elif game_start[0] == "guess" and len(game_start) == 1:
            print("Invalid Command!")
            number_of_tries -= 1

        # Reveals the secret word.
        elif game_start[0] == "cheat":
            print("Secret Word: " + selected_word)
            number_of_tries -= 1

        # Displays the list of commands
        elif game_start[0] == "help":
            commands()
            number_of_tries -= 1

        # Terminates the program
        elif game_start[0] == "quit":
            print("BYE!")
            exit(1)

        # Illegal Command
        else:
            print("Unknown Command: " + game_start[0])
            commands()
            number_of_tries -= 1
        number_of_tries += 1

        # If the number of tries are over.
        if number_of_tries == 7:
            print("Sorry, you lost! Better luck next time.")
            print("Secret Word: " + selected_word)
            number_of_tries -= 1


def main():
    """
    This is the main function which runs the whole game.
    :return:
    """
    # Checks if the arguments passed are not correct.
    if len(sys.argv) > 2:
        print("Usage: wordle [1st-secret-word]")
        exit(1)
    print("Welcome to the Wordle game!")
    play_game()


# Main Conditional Guard
if __name__ == '__main__':
    main()
