# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

""
Muhammad Dzaky Farhan
""

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = "Hail Shakes!"
crib_substring = "Hail"
print(crib_substring)

##Break the code via brute force search
#Part C)
flag = 0 #initial number of tries
start = time.time()
for i in range(26):
    for j in range(26):
        for k in range(26):
            flag += 1
            #In this line the i,j and k turns into letters 
            key = letters[i] + letters[j] + letters[k]
            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key=key,
                                plugs="AA BB CC DD EE")
            decrypt = engine.encipher(ShakesHorribleMessage)

            #if they found the "Hail" phrase they will print immediately in here so it wont run another loop.
            if crib_substring in decrypt:
                    print(decrypt)
                    break
        else:
            continue    
        break
    else:
        continue
    break

print("key =",key)

end = time.time()


#Print the Decoded message
print("decrypted message : ",decrypt)

#Part C)
#Using Time we could calculate the time by only subtract the end time and the start time, by declaring the start on the which line and end 
#by declaring the start on the which line and end on which line
#PS : You have to import module time

print("Execution time",end-start)

#Part D)
#Using flag as an integer, on the first so it will count how many tries on the loop it have to be in the third nested loop so 
#so it count all the nesteds loop.
print("Number of tries", flag)

#I think in the 1940s it would take like a minimum of 24 hour because of lack technology

#Part E)



