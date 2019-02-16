import re
import numpy as np


def gcd_list(list):
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return np.gcd(list[0], list[1])
    return np.gcd(list[0] , gcd_list(list[1:]))


#############################################################################################################################################

f = open("encrypted_text/vigenere_encrypted_text.txt" , "r")
encrypted_text = f.read()

# remove all whitespaces
encrypted_text = re.sub('\s+','',encrypted_text)

bigram = []
bigram_occurence = []
bigram_position = []
bigram_gap = []

for i in range(len(encrypted_text) - 1):
    current = encrypted_text[i] + encrypted_text[i + 1]

    if current in bigram:
       bigram_occurence[bigram.index(current)] += 1
       bigram_position[bigram.index(current)].append(i)

    else:
       bigram.append(current)
       bigram_occurence.append(1)
       bigram_position.append([i])


for pos in bigram_position:
     if len(pos) == 1:
         bigram_gap.append(0)
     else:
         all_gap = []
         for i in range(len(pos)):
             for j in range(i+1 , len(pos)):
                 all_gap.append(abs(pos[i]-pos[j]))

         print(all_gap)
         bigram_gap.append(gcd_list(all_gap))


print(bigram)
print(bigram_occurence)
print(bigram_position)
print(bigram_gap)
