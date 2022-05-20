#!/usr/bin/env python3
# Automatic Script that guess passwords in python
# Created by Jason Srilofung 5/11/2022
#Use a list to find passwords for the user

#import the modules 

import os
import crypt
from unittest import result

from end.CH06.bruteforceAttack import test_password

#The functions that test the user password

def userpassword(alorithm_salt, hashed_password, password_guess):

    #Uses the salt to hash guess
    hashed_guess = crypt.crypt(password_guess, alorithm_salt)
    #Compares salt guess and the hashed password
    if hashed_guess == hashed_password:
        return True
    return False

#Function that loads the dictionary file from user

dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path + "/top1000.txt", "r")

passwords = f.readlines()

#Ask the user for the Algorithm and Salt
algorithm_salt = input("What is the algorithm and salt? ")

#Ask the user for the Salted Hash
hashed_password = input("What is the full hashed password?")

#Loop and read each password and guess

for password in passwords:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("Found your password :3 {0}".format(password))
        break