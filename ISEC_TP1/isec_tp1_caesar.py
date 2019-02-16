'''

Given an encrypted text with the caesar algorithm, find the associated plain text

most common letters in french : https://en.wikipedia.org/wiki/Letter_frequency

'''

import numpy as np
import re


def decipher(text , key):
    res = []
    for c in text:
        res.append(chr((ord(c)-key+26)%26 + ord('a')))

    return ''.join(res)

#####################################################################################################################################

f = open("encrypted_text/caesar_encrypted_text.txt" , "r")
encrypted_text = f.read()

# remove all whitespaces
encrypted_text = re.sub('\s+','',encrypted_text)

frequencies = np.zeros(26)

# ord : get the ascii code
# chr : get the char from ascii code
for c in encrypted_text:
    if(ord(c) >= 97 and ord(c) <= 122):
        frequencies[ord(c)-ord('a')]+=1

frequencies /= len(encrypted_text)

most_common_letter = chr(np.argmax(frequencies) + ord('a'))

keys = []
letter_frequencies = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
possibilities = []

for i in range(26):
    key = (ord(most_common_letter) - ord(letter_frequencies[i]) + 26) % 26
    possibilities.append(decipher(encrypted_text, key))
    print("Possibility",i,"  (key = ", chr(key + ord('a')), "): ", possibilities[i])









