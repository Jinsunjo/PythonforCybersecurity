#!/usr/bin/env python3
# A Write and Read Script script in python
# Created by Jason Srilofung 5/1/2022


import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

#Opens up the file for reading

f = open(dir_path + "/hackme.txt" , "r")

#Reads the file and print it on the screen

contents = f.read()
print(contents)

f.close
