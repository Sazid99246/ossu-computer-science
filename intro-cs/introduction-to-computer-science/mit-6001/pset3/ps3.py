# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Sheikh Md. Sazidul Islam
# Collaborators :
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

        The score for a word is the product of two components:

        The first component is the sum of the points for letters in the word.
        The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    word_score = 0

    word_score = sum(SCRABBLE_LETTER_VALUES.get(letter, 0)
                     for letter in word.lower())

    # Calculate the second component of the score
    word_length = len(word)
    second_component = 7 * word_length - 3 * (n - word_length)
    second_component = max(second_component, 1)

    # Calculate the total score for the word
    total_score = word_score * second_component

    return total_score

#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    return ""

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    hand_clone = hand.copy()
    for letter in word.lower():
        if letter in hand_clone.keys():
            hand_clone[letter] -= 1

    for letter in hand_clone:
        if hand_clone[letter] < 0:
            hand_clone[letter] = 0

    return hand_clone


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    word = word.lower()
    hand_clone = hand.copy()
    word_dict = {}

    for letter in word:
        word_dict.setdefault(letter, 0)
        word_dict[letter] += 1

    if word in word_list and word.find("*") == -1:
        for letter in word:
            if letter in hand:
                hand_clone[letter] = hand_clone[letter] - word_dict[letter]
            else:
                return False

    elif word not in word_list and word.find("*") != -1:
        matched_word = []
        in_wordlist = False
        for vowel in VOWELS:
            word_replace = word.replace("*", vowel)
            if word_replace in word_list:
                matched_word.append(word_list[word_list.index(word_replace)])
                in_wordlist = True
        if len(matched_word) == 0:
            return False
        if in_wordlist:
            for letter in word:
                if letter in hand:
                    hand_clone[letter] = hand_clone[letter] - word_dict[letter]
                else:
                    return False

    else:
        return False

    for value in hand_clone.values():
        if value < 0:
            return False
        else:
            return True


#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    total = 0
    for value in hand.values():
        total += value

    return total


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """
    total_points = 0
    running = True

    while running:
        print("Current Hand: ", end="")
        display_hand(hand)
        word = str(
            input(("Enter a word, or \"!!\" to indicate you are finished: "))).lower()
        if word == "!!":
            break

        #  initializes when the user inputs a word
        hand = update_hand(hand, word)
        #  executes if the input word is valid
        if is_valid_word(word, hand, word_list):
            print("\"{0}\" earned {1} points.".format(
                word, get_word_score(word, calculate_handlen(hand))), end=" ")
            total_points += get_word_score(word, calculate_handlen(hand))
            print("Total points for this hand: {}".format(total_points))
            print()
        #  executes when the input word is invalid
        else:
            print("\"{}\" is not a valid word. Please choose another word.".format(word))
            print()

        #  terminates the loop if hand has no more letters
        if calculate_handlen(hand) == 0:
            print("Ran out of letters. Total score for this hand: {}".format(
                total_points))
            running = False

    return total_points


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    hand_clone = hand.copy()

    alphabet = string.ascii_lowercase
    sub_letter = random.choice(
        [char for char in alphabet if char != letter and char not in hand])

    for key in hand:
        if letter == key:
            if sub_letter not in hand:
                hand_clone[sub_letter[0]] = hand[key]
                del(hand_clone[letter])

    return hand_clone


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

#  substitute count, once per game
    sub_count = 1
    #  replay count
    replay_count = 1
    #  gets hand and hand size
    num_hands = int(input(("Enter total nnumber of hands: ")))
    hand = deal_hand(HAND_SIZE)
    #  if replay is already used, used initial hand for substitute loop
    initial_hand = hand
    #  display current hand to the user
    print("Current Hand: ", end=""), display_hand(hand)
    #  total score for all hands
    overall_points = 0

    while num_hands >= 1:
        #  score for each hand
        total_points_hand = 0

        #  loop for substituting a letter in hand
        while sub_count >= 1:
            #  executes when replay option is already used
            #  this is necessary since replay loop won't be executed again
            #  but num_hands should always be deducted by 1 after each round
            if replay_count == 0:
                num_hands -= 1
                hand = deal_hand(HAND_SIZE)
                print()
                print("Current Hand: ", end=""), display_hand(hand)
            #  ask the user for substitute
            answer_sub = input(
                "Type 'yes' to substitute a letter, 'no' otherwise: ").lower()
            #  executes subsitute_hand() function with the passed letter
            if answer_sub == 'yes':
                sub_count -= 1
                letter = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter)
                break
            #  terminate the loop
            elif answer_sub == 'no':
                break

        #  executes when replay option is already used
        #  this is necessary since replay loop won't be executed again
        #  but num_hands should always be deducted by 1 after each round
        if replay_count == 0:
            num_hands -= 1
            hand = deal_hand(HAND_SIZE)

        print()
        hand_score = play_hand(hand, word_list)

        while replay_count >= 1:
            #  print series of hyphens as divider
            print("----------------------------------------------")
            replay = input(
                "Type 'yes' to replay the hand, 'no' otherwise: ").lower()
            if replay == 'no':
                #  executed if the player wished to sub a letter in the 1st round
                #  sub_count loop won't be executed again so another hand should be dealt for the user
                if sub_count == 0:
                    hand = deal_hand(HAND_SIZE)
                while sub_count >= 1:
                    #  create new hand
                    hand = deal_hand(HAND_SIZE)
                    #  display current hand to the user in case of substitution
                    print("Current Hand: ", end=""), display_hand(hand)
                    print()
                    #  ask the user for substitute
                    answer_sub = input(
                        "Type 'yes' to substitute a letter, 'no' otherwise: ").lower()
                    #  executes subsitute_hand() function with the passed letter
                    if answer_sub == 'yes':
                        sub_count -= 1
                        letter = input(
                            "Which letter would you like to replace: ")
                        hand = substitute_hand(hand, letter)
                        break

                    elif answer_sub == 'no':
                        break

                #  deduct number of hands by 1 since a new hand will be played
                num_hands -= 1
                print()
                #  new variable for the returned total score of play_hand function
                new_hand_score = play_hand(hand, word_list)

            #  retain number of hands but replay option won't be executed again
            elif replay == 'yes':
                print()
                #  new variable for the returned total score of play_hand function
                new_hand_score = play_hand(hand, word_list)
                replay_count -= 1
                #  deduct the initial hand but not the replayed hand
                num_hands -= 1
                break
        #  get overall points for all hands
        overall_points += max(hand_score, new_hand_score)

    print("--------------------------")
    print("Total score overall hands: {}".format(overall_points))

    return overall_points


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
