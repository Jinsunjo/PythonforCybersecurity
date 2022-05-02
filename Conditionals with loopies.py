#!/usr/bin/env python3
# A Conditional script in python
# Created by Jason Srilofung 5/1/2022
#The three goals is ask the user how is their day and takes the imput and print it out
#If the answer is y print out yes it is
# Update make the loop a def function to be recalled

#takes input of the user's name

userName = input("What is your name? ")

print("greetings {0}".format(userName))

# input that ask the user if the day is good

userDay = input("Is today a good day? (y/n) ")

#The start of the if statement
def conditionals():
    if userDay == "y":
        print("Yes it is {0}".format(userName))

    for x in range(10):
        print("Yes it is {0}".format(userName))

    else:
        print("Hope you day gets better {0}".format(userName))

#print yes it is 10 times

#recall the fucntion

conditionals()


