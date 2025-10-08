import random


# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows ASCII-Phase"""
    print(STAGES[mistakes])


    display_word = ""
    for letter in secret_word:
        display_word += (letter + " ") if letter in guessed_letters else "_ "
    print("Word:", display_word)
    print()



def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    #print("Secret word selected: " + secret_word)  # for testing, later remove this line

    guessed_letters = []
    mistakes = 0

    # Phase 0 + Unterstriche anzeigen
    display_game_state(mistakes, secret_word, guessed_letters)

    #For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed: ", guess)


if __name__ == "__main__":
    play_game()
