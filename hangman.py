import random

WORDS = ["python", "planet", "guitar", "castle", "orange"]
MAX_INCORRECT_GUESSES = 6
HANGMAN_PICTURES = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]
def play_game():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    print(f"Guess the word one letter at a time. You can miss {MAX_INCORRECT_GUESSES} times.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\n" + HANGMAN_PICTURES[incorrect_guesses])
        print("Word: " + " ".join(letter if letter in guessed_letters else "_" for letter in secret_word))
        print("Guessed letters: " + (", ".join(guessed_letters) if guessed_letters else "none"))
        print(f"Incorrect guesses left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter (A-Z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print("\nYou win! The word was " + secret_word + ".")
                return
        else:
            incorrect_guesses += 1
            print("That letter is not in the word.")

    print("\n" + HANGMAN_PICTURES[MAX_INCORRECT_GUESSES])
    print("Game over! The word was " + secret_word + ".")


if __name__ == "__main__":
    play_game()
