import random
from ascii_art import STAGES
from word_list import WORDS
from valid_letters import LETTERS
from valid_letters import NUMBERS


def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):

    print(STAGES[mistakes])
    if mistakes == 1:
        print(f"You've made one mistake so far")
    else:
        print(f"You've made {NUMBERS[mistakes]} mistakes so far")
    letters = ""
    for char in secret_word:
        if char in guessed_letters:
            letters += char
        else:
            letters += "_"
    print(f"Your current progress:{letters.upper()}")



def is_word_revealed(secret_word, guessed_letters):
    found_letters = 0
    for char in secret_word:
        if char in guessed_letters:
            found_letters += 1
    return found_letters == len(secret_word)




def play_game():
    print("Welcome to Snowman Meltdown!")

    secret_word = get_random_word() #Ich initialisiere die Variable mit dem Namen secret_word auf den Rückgabewert der Funktion mit dem Namen get_random_word
    guessed_letters = []
    mistakes = 0

    display_game_state(mistakes, secret_word, guessed_letters)

    while not is_word_revealed(secret_word, guessed_letters) and mistakes < len(STAGES) -1:
        valid_input = True
        # nach ersten Buchstaben fragen und merken
        guess = input("Guess a letter: ")
        #Usereingabe von whitespaces befreien
        guess = guess.strip()
        #Usereingabe Buchstabe in Kleinbuchstaben umwandeln .lower()
        guess = guess.lower()
        #zähle die Buchstaben
        length_of_input = len(guess)
        #wenn das mehr als ein Buchstabe ist, Fehlermeldung
        if length_of_input > 1 or length_of_input < 1:
            valid_input = False
            print("Only exactly one letter allowed. Try again.")
        #wenn Sonderzeichen, Fehlermeldung
        if valid_input and not guess in LETTERS:
            valid_input = False
            print("Only latin characters allowed. Try again.")
        #überprüfen ob Buchstabe in secret_word ist
        if valid_input and guess in secret_word:
            guessed_letters.append(guess)
        elif valid_input:
            mistakes = mistakes + 1
        #wenn ja, merken das Buchstabe in secret_word ist, wenn nein, merken das Fehler bei stages
        display_game_state(mistakes, secret_word, guessed_letters)

    if is_word_revealed(secret_word, guessed_letters):
        print("You saved the snowman!")
        print(f"The word was: {secret_word}")
    else:
        print("The snowman melted.")
        print(f"The word was: {secret_word}")

    print("Do you want to play again?")
    if input("Y/N ").upper() == "Y":
        play_game()