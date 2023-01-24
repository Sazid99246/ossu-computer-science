# Problem Set 4B
# Name: Sheikh MD Sazidul Islam
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("assets/mit-6001/story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'assets/mit-6001/words_pset4.txt'

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words

    def build_shift_dict(self, shift):
        try:
            assert 0 <= shift < 26
            num_to_letter_mappling = {i: letter for i, letter in enumerate(string.ascii_lowercase)}
            shift_dict = {}
            
            for key, value in zip(num_to_letter_mappling.keys(), num_to_letter_mappling.values()):
                try:
                    shift_dict[value] = num_to_letter_mappling[key + shift]
                except:
                    shift_dict[value] = num_to_letter_mappling[key + shift - 26]
            
            shift_dict_upper = {key.upper(): value.upper() for key, value in zip(shift_dict.keys(), shift_dict.values())}
            shift_dict.update(shift_dict_upper)

            return shift_dict
        
        except AssertionError:
            print("Invalid shift parameter.  Please choose a value between 0 and 26")

        except Exception as e:
            print(e)    

    def apply_shift(self, shift):        
        shift_dict = self.build_shift_dict(shift)
        message_list = [shift_dict[letter] if letter.isalpha() else letter for letter in self.message_text]
        return ''.join(message_list)
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        
    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    def change_shift(self, shift):
        assert 0 <= shift < 26
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

class CiphertextMessage(Message):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        max_word_count = 0
        best_shift = 0
        for shift in range(1,26):
            word_list = self.apply_shift(26-shift) \
                .strip(string.punctuation) \
                .split()

            english_word_count = sum(1 for word in word_list if word in self.valid_words)

            if english_word_count > max_word_count:
                max_word_count = english_word_count
                best_shift = shift

        if best_shift == 0:
            return (best_shift, self.message_text)
        else:
            return (best_shift, self.apply_shift(26 - best_shift))


if __name__ == '__main__':
    plaintext = PlaintextMessage('hello', 2)
    actual1 = plaintext.get_message_text_encrypted()
    expected1 = 'jgnnq'
    print(f'Expected Output: {expected1}')
    print(f'Actual Output: {actual1}')
    print('Test Successful: ', actual1 == expected1)

    plaintext = PlaintextMessage('hello', 0)
    actual2 = plaintext.get_message_text_encrypted()
    expected2 = 'hello'
    print(f'Expected Output: {expected2}')
    print(f'Actual Output: {actual2}')
    print('Test Successful: ', actual2 == expected2)

    ciphertext = CiphertextMessage('jgnnq')
    actual3 = ciphertext.decrypt_message()
    expected3 = (2, 'hello')
    print(f'Expected Output: {expected3}')
    print(f'Actual Output: {actual3}')
    print('Test Successful: ', actual3 == expected3)

    ciphertext = CiphertextMessage('hello')
    actual4 = ciphertext.decrypt_message()
    expected4 = (0, 'hello')
    print(f'Expected Output: {expected4}')
    print(f'Actual Output: {actual4}')
    print('Test Successful: ', actual4 == expected4)

    # Decrypt Example Message
    story_string = get_story_string()
    cm = CiphertextMessage(story_string)
    print(cm.decrypt_message())