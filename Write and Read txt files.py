#!/usr/bin/env python3
# A Write and Read Script script in python
# Created by Jason Srilofung 5/1/2022


#Todays goal is to write a script that ask 
#   What is your name
#   What is your favorite color
#   What was your first pet's name
#   What is your mother's maiden name
#   What elementary school did you attend
# Name the infomation in a file that is called hackme.txt
# Later a scrfipt that reads hackme.txt and print out here is some to hack and print the infomation

#The inputs that the user have to answer

from distutils import text_file


question_1 = input("What is your name?\n")
question_2 = input("What is your favorite color\n")
question_3 = input("What was your first pet's name?\n")
question_4 = input("What is your mother's maiden name?\n")
question_5 = input("What elementary school did you attend?\n")

# Saving the answers into a txt file and opens the file

f = open("hackme.txt" , "w")

f.write(question_1 + "\n")
f.write(question_2 + "\n")
f.write(question_3 + "\n")
f.write(question_4 + "\n")
f.write(question_5 + "\n")

#Closes the file

f.close()






