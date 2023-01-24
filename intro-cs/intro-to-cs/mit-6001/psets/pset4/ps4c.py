# Problem Set 4C
# Name: Sheikh MD Sazidul Islam
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'assets/mit-6001/words_pset4.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        t_dict = {}
        
        for n in range(len(VOWELS_LOWER)):
            t_dict[VOWELS_LOWER[n]] = vowels_permutation[n]
            t_dict[VOWELS_LOWER[n].upper()] = vowels_permutation[n].upper()
            
        for c in CONSONANTS_LOWER:
            t_dict[c] = c
            
        for c in CONSONANTS_UPPER:
            t_dict[c] = c
            
        return t_dict

    
    def apply_transpose(self, transpose_dict):
        e_message = ''
        
        for c in self.message_text:
            if c in transpose_dict:
                e_message += transpose_dict[c]
            else:
                e_message += c
                
        return e_message
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        n_words = []
        vowels_permutations = get_permutations(VOWELS_LOWER)
        n_p = len(vowels_permutations)
        d_messages = []
        
        for v_p in vowels_permutations:
            transpose_dict = self.build_transpose_dict(v_p)            
            d_mess = self.apply_transpose(transpose_dict)
            d_messages += [d_mess]
            d_words = d_mess.split()
            n = 0
            
            for word in d_words:
                if is_word(self.valid_words,word):
                    n += 1
            n_words += [n]
        n_words_max = max(n_words)

        if n_words_max == 0:
            return (self.message_text)
        else:
            results = []
            for n in range(len(n_words)):
                if n_words[n] == n_words_max:
                    results += [d_messages[n]]
            return results

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())