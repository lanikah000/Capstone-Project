import random

# ASCII diagrams of the hangman stages
def hangman(wrong_guess):
    stages = [
        """
    |-----
    |  |
    |
    |
    |
    |
    """,
        """
    |-----
    |  |
    |  O
    |
    |
    |
    """,
        """
    |-----
    |  |
    |  O
    |  |
    |
    |
    """,
        """
    |-----
    |  |
    |  O
    | /|
    |
    |
    """,
        """
    |-----
    |  |
    |  O
    | /|\\
    |
    |
    """,
        """
    |-----
    |  |
    |  O
    | /|\\
    | /
    |
    """,
        """
    |-----
    |  |
    |  O
    | /|\\
    | / \\
    |
    """
    ]
    return stages[wrong_guess]

# the game function
def play_hangman():
    # defining variables for the game loop
    words = ["apple", "house", "water", "chair", "thunder",
             "heart", "diamond", "skeleton", "beach"]
    word = random.choice(words)
    guessing_word = ["_"] * len(word)
    guessed = []
    wrong_guess = 0
    wrong_letters = []

    # game loop
    while True:
        print(hangman(wrong_guess))
        if wrong_guess > 0:
            print(f"Wrong guesses: {" ".join(wrong_letters)}\n")
        print(" ".join(guessing_word))
        guess = input("\nEnter a letter: ").lower()

        # edge cases
        if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please type in one letter.")
            continue
        if guess in guessed:
            print("You have already guessed this letter.")
            continue
        guessed.append(guess)

        # correct guess or wrong guess outputs
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessing_word[i] = guess
            print("Correct guess! \n")
        else:
            wrong_guess += 1
            wrong_letters.append(guess)
            print(f"Incorrect guess.\n")

        # losing or winning outputs
        if wrong_guess == 6:
            print(hangman(wrong_guess))
            print(f"You lost. The word was: {word}.\n")
            break
        if "".join(guessing_word) == word:
            print(" ".join(guessing_word))
            print("You won!\n")
            break


# game replay loop
while True:
    play_hangman()
    again = input(
        "Play again? (y to continue, any other key to exit): ").lower()
    if again == "y":
        continue
    else:
        print("Thanks for playing!")
        break