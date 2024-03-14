# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""

"""
Muhammad Dzaky Farhan
Part B
"""


from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

#frequency of each letter
letter_counts = Counter(message)
#print(letter_counts)

#find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    if freq > maxFreq and letter in string.ascii_letters:
        maxFreq = freq
        maxLetter = letter
print("Max Ocurring Letter:", maxLetter)

#predict shift
#assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = ord(maxLetter.lower()) - ord('e')
print("Predicted Shift:", shift)

#Part C
#create the Caesar cypher

message = input("Enter a message: ")
print("Message:", message)

offset = int(input("Enter an offset: "))  #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        shiftedIndex = (index + offset) % totalLetters 
        keys[letter] = letters[shiftedIndex]
        invkeys[letters[shiftedIndex]] = letter
    else: 
        shiftedIndex = (index + offset - totalLetters) % totalLetters
        keys[letter] = letters[shiftedIndex+totalLetters]
        invkeys[letters[shiftedIndex+totalLetters]] = letter
        

print("Cypher Dict:", keys)

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter)
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list inot string

#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list inot string



for shift in range(totalLetters):
        keys = {}  # use dictionary for letter mapping
        invkeys = {}  # use dictionary for inverse letter mapping, you could use inverse search from original dict
        for index, letter in enumerate(letters):
        # cypher setup
            if index < totalLetters: #lowercase
                shiftedIndex = (index + shift) % totalLetters 
                keys[letter] = letters[shiftedIndex]
                invkeys[letters[shiftedIndex]] = letter
            else: 
                shiftedIndex = (index + shift - totalLetters) % totalLetters
                keys[letter] = letters[shiftedIndex+totalLetters]
                invkeys[letters[shiftedIndex+totalLetters]] = letter

        # decrypt
        decryptedMessage = []
        for letter in message:
            if letter == ' ':  # spaces
                decryptedMessage.append(letter)
            else:
                decryptedMessage.append(invkeys[letter])

        
        print()
        print("Shift: {}, Decrypted Message: {}".format(shift, ''.join(decryptedMessage)))


