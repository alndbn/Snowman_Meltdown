import random
from ascii_art import STAGES
from word_list import WORDS


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows ASCII-Phase"""
    print(STAGES[mistakes])


    display_word = ""
    for letter in secret_word:
        display_word += (letter + " ") if letter in guessed_letters else "_ "
    print("Word:", display_word)
    print()


def is_word_revealed(secret_word, guessed_letters):
    """returns True, if guessed_letters contains all letters from secret_word"""
    return all(letter in guessed_letters for letter in secret_word)


def play_game():
    """conns the game play with input, hits/mistake, win/loose message"""
    secret_word = get_random_word() #Ich initialisiere die Variable mit dem Namen secret_word auf den Rückgabewert der Funktion mit dem Namen get_random_word
    print("Welcome to Snowman Meltdown!")
    #print("Secret word selected: " + secret_word)  # for testing, later remove this line

    guessed_letters = []
    mistakes = 0

    # Phase 0 + Unterstriche anzeigen
    display_game_state(mistakes, secret_word, guessed_letters)


    while not is_word_revealed(secret_word, guessed_letters) and mistakes < len(STAGES) -1:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!")
        else:
            mistakes += 1
            print("Wrong guess")

        display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_revealed(secret_word, guessed_letters):
        print("You saved the snowman!")
        print(f"The word was: {secret_word}")
    else:
        print("The snowman melted.")
        print(f"The word was: {secret_word}")



