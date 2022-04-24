#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by Jason Srilofung 4/15/2022


#Todays goal is to write a script that prompts user name and prints hello and their input and prints a affirmations
# extra goal is to let the user input age and print out their age in two years


user_name = input("What is your name? ")
user_age = input("What is your age? ")

print("Greetings {0}".format(user_name))
print("I hope you have a nice day {0}".format(user_name))
print("You're  {0}".format(user_age))

user_input = int(user_age)
set_year = int(2)

total_years = user_input + set_year

print("In two year you're gonna be {0}".format(total_years) + " years old")