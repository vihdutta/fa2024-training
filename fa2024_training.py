import numpy as np
import math

# Welcome to the M-STARX GitHub + Python training file! If you've made it here
# you already completed a few steps, so good job! You can complete this training
# by accomplishing every task marked with "TODO". When you complete a step,
# remove the "TODO" comment! Once you've cleared every "TODO" statement, push
# your final file to your GitHub branch :)

# Note: this tutorial is very basic, especially if you're more experienced coder.
# We often have people joining the team from a wide variety of skill levels, so this is just
# intended to get everyone's personal machines set up and give people a basic familiarity with
# GitHub and Python syntax. I promise you'll learn tons of more involved stuff as the year 
# progresses on your subteam!!

# TODO: if your IDE throws and a "Module Not Found" error on line 1 and/or 2 when you run 
# this code, you need to use pip (or pip3) to install numpy. Importing libraries
# is a crucial part of Python, and pip is a great way to quickly install them to
# your computer. 
# You can run "pip install numpy" to download the numpy library.

# TODO: Use the "git checkout -b" command to create a new branch in the repository
# and switch to it. Name your branch your uniqname, and run "git status" to make sure
# you successfully switched to it. If it says "on branch {uniqname}", you did it right!

# To practice with Python, you'll write a couple functions to manipulate a numpy array,
# as well as a main script to run those functions on a sample array

# TODO: Complete the function fillArray()
# This function fills a numpy array with values from data_list in order.
# If size is specified, the array is declared with shape (1, size). If size is 
# unspecified, the array is declared with the same number of rows and columns, which is math.sqrt(len(data_list))
def fillArray(data_list, size=None):
    if size == None:
        # TODO: initialize a numpy array array with equal number of rows and columns
        
    print(arr.shape) # check your work: prints the shape of the array


# TODO: Complete the main script
# Lists are a common Python container, similar to vectors in C++ and MATLAB
list = [1, 2, 3, 4] # this is a really simple list, with 5 elements

# TODO: if the list has a square number of elements (i.e., 1, 4, 9, 16), call fillArray() with no size argument
# Else, call fillArray() with a size argument equal to the list's length


# TODO: Push your final changes to your GitHub branch in 3 steps:
#   1. Stage your changes for commit using the "git add" command. You can type the filename,
#      or just use "git add --all" to stage all the files you've changed in the repository.
#   2. Commit your changes to the reppository with "git commit -m "{commit message}"". Your
#      commit message should be short but descriptive!
#   3. Push your changes using the command "git push".
#   4. Check that you changes pushed successfully by running "git status".