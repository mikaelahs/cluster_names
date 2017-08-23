'''
Created: May 25, 2017
@author mhoffmanstapleton@usfca.edu
'''

class sound:
    '''
    This class is responsible for converting a word to its soundex version. It contains two functions: __init__(), which
    initializes attributes, and get_soundex(), which returns the soundex.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.soundex = None

    def get_soundex(self, word):
        '''
        Given a word, this function returns the soundex of that word. It follows the rules outlined in the assignment description.
        :param word: the word to be converted
        :type word: string
        :return: the soundex of the given word
        :rtype: string
        '''
        soundex_elements = []
        soundex_elements.append(word[0].upper())    # Get the first entry of the soundex
        index = 1
        length = 1
        # Get the remaining entries of the soundex (limited to four entries)
        while length < 4:
            # Checks to make sure there enough letters left in the word
            try:
                if word[index].lower() in ['b', 'f', 'p', 'v']:
                    soundex_elements.append('1')
                    index += 1
                    length += 1
                elif word[index].lower() in ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']:
                    soundex_elements.append('2')
                    index += 1
                    length += 1
                elif word[index].lower() in ['d', 't']:
                    soundex_elements.append('3')
                    index += 1
                    length += 1
                elif word[index].lower() == 'l':
                    soundex_elements.append('4')
                    index += 1
                    length += 1
                elif word[index].lower() in ['m', 'n']:
                    soundex_elements.append('5')
                    index += 1
                    length += 1
                elif word[index].lower() == 'r':
                    soundex_elements.append('6')
                    index += 1
                    length += 1
                # In this case, the letter is skipped and the entry is not filled
                else:
                    index += 1
            # If there aren't enough letters left in the word, then the current entry is given a 0
            except:
                soundex_elements.append('0')
                length += 1
            # Checks to see that there are't repeating entries (except in the case of 0s)
            if length > 1:
                if soundex_elements[length - 1] == soundex_elements[length - 2]:
                    if soundex_elements[length - 1] == '0':
                        continue
                    else:
                        del soundex_elements[length - 1]
                        length -= 1
        self.soundex = ''.join(soundex_elements)
        return self.soundex
