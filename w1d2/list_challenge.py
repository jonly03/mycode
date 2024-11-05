#!/usr/bin/env python3
from utilities import custom_print, num_prompt

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
custom_print("My favorite character is", heroes[2])

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.
user_input = num_prompt("Enter an int between 1 and 100")
print(user_input)

nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
print(f"Max of {nums} is {max(nums)}")
