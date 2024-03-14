# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""

"""
Muhammad Dzaky Farhan
Part A
"""

import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter a message: ")
print("Message:", message)

#create the Caesar cypher

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
    else: #uppercase
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

