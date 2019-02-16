
import re


def decipher(text , a , b):
    res = []

    for c in text:
        d = ord(c) - ord('a') - b
        if d<0:
            d+=26

        res.append(chr((d*a%26) + ord('a')))

    return ''.join(res)


##########################################################################################################################################


f = open("encrypted_text/affine_encrypted_text.txt" , "r")
encrypted_text = f.read()

# remove all whitespaces
encrypted_text = re.sub('\s+','',encrypted_text)

a_values = [1,3,5,7,9,11,15,17,19,21,23,25]


for i in range(12):
    for b in range(26):
        a = a_values[i]

        print("(",a,",",b,")")
        print(decipher(encrypted_text,a,b))