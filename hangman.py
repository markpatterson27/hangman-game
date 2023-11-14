# Console based hangman game.

import random
import os

# Constants
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone", "hangman",
         "computer", "science", "programming", "mathematics", "player", "condition",
         "reverse", "water", "board", "geeks", "keyboard", "laptop", "headphone",
         "mouse", "printer", "scanner", "software", "hardware", "network", "server")

HANGMAN_STAGES = (
"""
  -------
  |/    |
  |
  |
  |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |
  |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |     |
  |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |     |
  |     |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |    /|
  |     |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |    /|\\
  |     |
  |
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |    /|\\
  |     |
  |    /
  |
 /|\\
-----------
""","""
  -------
  |/    |
  |     O
  |    /|\\
  |     |
  |    / \\
  |
 /|\\
-----------
""")

# Functions
def clear_screen():
    """Clears the screen."""
    os.system("cls" if os.name == "nt" else "clear")

def get_random_word():
    """Returns a random word from the WORDS tuple."""
    return random.choice(WORDS)

def splash_screen():
    """The splash screen."""
    print("""
             _   _                                               ----- 
            | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __       |    o
            | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\      |   /|\\
            |  _  | (_| | | | | (_| | | | | | | (_| | | | |     |   / \\
            |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|     |
                               |___/                            v1.0
    """)
    input("Press enter to continue...")
    clear_screen()


def hangman():
    """The hangman game."""
    try:
        # game outer loop
        while True:
            # Setup
            word = get_random_word()
            guessed_letters = []
            guessed_word = ["_"] * len(word)
            wrong_guesses = 0

            # game inner loop
            while True:
                clear_screen()
                print("Hangman game. Try to guess the word. (CTRL+C to quit)")
                print(HANGMAN_STAGES[wrong_guesses])
                print(" ".join(guessed_word), end='    ')
                print("(Guessed letters: " + ", ".join(guessed_letters),")")
                print()

                # check if player has won
                if "_" not in guessed_word:
                    print("You win!")
                    break

                # check if player has lost
                if wrong_guesses == len(HANGMAN_STAGES)-1:
                    print("You lose!")
                    break

                # make sure player enters a single letter
                while True:
                    guess = input("Guess a letter: ").lower()
                    if len(guess) == 1 and guess.isalpha():
                        # check if letter has already been guessed
                        if guess in guessed_letters:
                            print("You have already guessed that letter.")
                        else:
                            break
                    else:
                        print("Invalid guess. Please enter a single letter.")

                # add guess to guessed letters
                guessed_letters.append(guess)

                # check if guess is in word
                if guess in word:
                    # add guess to guessed word
                    for i in range(len(word)):
                        if word[i] == guess:
                            guessed_word[i] = guess 
                else:
                    # increment wrong guesses
                    wrong_guesses += 1

            # Ask the player if they want to play again
            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                break

        print("\nGoodbye!")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()
    

# Main
if __name__ == "__main__":
    splash_screen()
    hangman()
