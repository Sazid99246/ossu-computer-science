import random
import string

WORDLIST_FILENAME = "words.txt"

# Helper function to load words from the words.txt file
def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, "r") as file:
        words = file.read().split()
    print(len(words), "words loaded.")
    return words

# Helper function to choose a random word from the word list
def choose_word(wordlist):
    return random.choice(wordlist)

# Helper function to check if the word has been guessed completely
def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

# Helper function to get the word with guessed letters displayed and unguessed letters replaced with an underscore and space (_)
def get_guessed_word(secret_word, letters_guessed):
    return "".join(letter if letter in letters_guessed else "_ " for letter in secret_word)

# Helper function to get all available letters that have not been guessed
def get_available_letters(letters_guessed):
    return "".join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

# Main function to play the Hangman game
def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")

    guesses_remaining = 6
    letters_guessed = []
    warnings_remaining = 3

    while guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guess in "aeiou":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
        print("------------")

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break

    if not is_word_guessed(secret_word, letters_guessed):
        print("Sorry, you ran out of guesses. The word was", secret_word)

# Helper function to check if the guessed letters of my_word match the corresponding letters of other_word
def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False
    return True

# Helper function to print all words in wordlist that match my_word
def show_possible_matches(my_word):
    matching_words = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matching_words:
        print("Possible word matches are:", " ".join(matching_words))
    else:
        print("No matches found")

# Main function to play the Hangman game with hints
def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")

    guesses_remaining = 6
    letters_guessed = []
    warnings_remaining = 3

    while guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        if guess == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        if not guess.isalpha() or len(guess) != 1:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:",
                      get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose one guess:",
                      get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if guess in "aeiou":
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
        print("------------")

        if is_word_guessed(secret_word, letters_guessed):
            total_score = guesses_remaining * len(set(secret_word))
            print("Congratulations, you won!")
            print("Your total score for this game is:", total_score)
            break

    if not is_word_guessed(secret_word, letters_guessed):
        print("Sorry, you ran out of guesses. The word was", secret_word)


if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
