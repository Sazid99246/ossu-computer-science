# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Sheikh MD Sazidul Islam
# Collaborators : <your collaborators>
# Time spent    : 3 days

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
WILDCARD = '*'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
} # add '*': 0 for wildcard

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "assets/mit-6001/words.txt"

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
        freq[x] = freq.get(x,0) + 1
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
    com1 = 0
    com2 = 0
    word = word.lower()
    Trueword = ''
    for letter in word:
        if letter in 'abcdefghijklmnopqrstuvwxyz*': #add '*' for wildcard
            Trueword += letter
    for letter in Trueword:
        com1 = com1 + int(SCRABBLE_LETTER_VALUES[letter])
        
    com2 = max(7*len(word)-3*(n-len(word)), 1)
    return com1*com2
    
    
    # TO DO... Remove this line when you implement this function

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
#    print()                              # print an empty line

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
    
    hand={}
    num_vowels = int(math.ceil(n / 3))-1 #Vowels -1 for wildcard
    
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels+1, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand[WILDCARD] = 1  #asterisk for wildcard
    
    return hand

#    testList = [{'a':1, 'c':1, 'i':1, '*':1, 'p':1, 'r':1, 't':1}, 
#                {'d':2, '*':1, 'l':1, 'o':1, 'u':1, 't':1}]
#    for elm in testList:
#        print(elm)
#        yield elm
     

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
    new_hand = hand.copy()
        
    for letter in word.lower():
        if new_hand.get(letter) != None:
            new_hand[letter] = new_hand[letter] - 1
            if new_hand[letter] <= 0:
                del new_hand[letter]
    
    return new_hand    
    # TO DO... Remove this line when you implement this function

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
    word_dict = get_frequency_dict(word)
    with_wildcard(word)
    guessList = []
    validList = []
    
    for letter in word_dict.keys(): #check availabe condiction in hand
        if word_dict[letter] > hand.get(letter, 0):
            return False
    
    if with_wildcard(word):
        guessList = wildcard_letter_guess(word)
        for guessWord in guessList:
            if word_in_word_list(guessWord, word_list):
                validList.append(guessWord)
        if validList != []:
            return True
        else:
            return False
        
    else:
        if word_in_word_list(word, word_list):
            return True
        else:
            return False
    
    

      # TO DO... Remove this line when you implement this function
def wildcard_letter_guess(wordWild):
    """ Assumes wordWild is a string that include a wildcard
    Return a list - guessList contains all possible words"""
    guessList = []
    for v in VOWELS:
        guessList.append(wordWild.replace('*', v))
    return guessList
    
def with_wildcard(word):
    """ Assumes word is a string. 
        Return True if the '*' is in word; False otherwise"""
    if '*' in word:
        return True
    else:
        return False

def word_in_word_list(word, word_list):
    """ Assume word is a string; word_list is a list.
        Return True if word is in word_list; False otherwise"""
    if word in word_list:
        return True
    else:
        return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    handList = hand.values()
    total = 0
    for num in handList:
        total = total + num
    return total
      # TO DO... Remove this line when you implement this function

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
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    totScore = 0
    # As long as there are still letters left in the hand:
    while hand != {}:    
        # Display the hand
        print('Current hand: ', end='')
        display_hand(hand)
        # Ask user for input
        word = str(input('Enter word, or "!!" to indicate that you are finished: '))  
        # If the input is two exclamation points:
        if word == '!!':
        # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(word, hand, word_list):
                # Tell the user how many points the word earned,
                # and the updated total score
                totScore = totScore + get_word_score(word, calculate_handlen(hand))
                print('\"'+word+'\"', 'earned', get_word_score(word, calculate_handlen(hand)),\
                      'points.', 'Total: ', totScore, 'points.')
                
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
        print()
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    if hand == {}:
        print('Ran out of letters. Total score:', totScore, 'points.')
        return totScore
    # Return the total score as result of function
    else:
        print('Total score:', totScore, 'points.')
        return totScore
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
    
    #lowercase the letter
    letter = letter.lower()
    #innitia new_hand
    sub_hand = hand.copy()
    #define letter in hand
    #define a random letter
    a_random_letter = ''
    #define vowels and consonants
    selectedVOWELS = VOWELS[:]
    selectedCONSONANTS = CONSONANTS[:]
    for elm in VOWELS:
        if elm in hand.keys():
            selectedVOWELS = selectedVOWELS.replace(elm, '')
    for elm in CONSONANTS:
        if elm in hand.keys():
            selectedCONSONANTS = selectedCONSONANTS.replace(elm, '')
    #if letter not in the hand
    if letter not in sub_hand:
        #remains same
        return sub_hand
    #otherwise
    else:
    #select a letter from 26 alphabet without replicate
        #if letter is vowel:
        if letter in VOWELS:
            a_random_letter = random.choice(selectedVOWELS)
        #else, letter is consonant:
        else:
            a_random_letter = random.choice(selectedCONSONANTS)
    #append letter into new_hand
    sub_hand[a_random_letter] = int(sub_hand[letter])
    #remove letter into new_hand
    del sub_hand[letter]
    #return
    return sub_hand
    
        
       
    
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
    
    #print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    #initiate
    Score = 0
    Score_2 = 0
    totScore = 0
    substituteRem = True
    replayRem = True
    #number of hands
    numHand = int(input('Enter total number of hands: '))
    
    
    #deal a hand and display card
    
    
    #the game
    for i in range(numHand):
        hand = deal_hand(HAND_SIZE)
        print('Current hand: ', end='')
        display_hand(hand)
        #substitue?
        if substituteRem:
            (hand, substitueRem) = subProcess(hand, substituteRem)
            
        #score = play a hand
        Score = play_hand(hand, word_list)
        print('----------')
        
        #if choice replay,
        if replayRem:
            #play and get the score
            (Score_2, replayRem)  = replayProcess(Score, hand, word_list, replayRem)
            #choice the higher one and add it into the tot
            totScore += max(Score, Score_2)
            #clean the Score 2
            Score_2 = 0
        #no,
            #totScore += score
        else:
            totScore += Score
        
        #deal a hand
        
    #ending, print the totScore
    print('Total score over all hands: ', totScore)
          
        


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#

def replayProcess(Score, hand, word_list, replayRem):
    """ Allow user to replay.
        Ask to replay.
        If yes, play and return a additional scored.
        return original score otherwise."""        
    rYN = ''
    Score_2 = 0
    #ask input for replay
    rYN = input('Would you like to replay the hand?(yes/no) ')
    assert rYN.lower() == 'yes' or rYN.lower() == 'no', 'Please enter yes or no.'
    print()
    #yes, 
    if rYN.lower() == 'yes':
        #play and get the score
        Score_2 = play_hand(hand, word_list)
        print('----------')
        replayRem = False
        return (Score_2, replayRem)
    #no, return original
    else:
        return (Score, replayRem)
                
    

def subProcess(hand, substituteRem):
    """ Assumes hand is a dict
        ask the user choice whether make a substitute for his/her hand.
        If yes, return substitute hand"""

    sYN = ''
    sYN = input('Would you like to substitute a letter?(yes/no) ')
    l = ''
    new_hand = {}
    assert sYN.lower() == 'yes' or sYN.lower() == 'no', 'Please enter Yes or No.'
    
    if sYN.lower() == 'yes':
        l = input('Which letter would you like to replace: ')
        l = l.lower()
        assert type(l)== str, 'Why do you input a non-str? Why?'
        new_hand = substitute_hand(hand, l)
        substituteRem = False
        print()
        return (new_hand, substituteRem)
    else:
        print()
        return (hand, substituteRem)
        
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)