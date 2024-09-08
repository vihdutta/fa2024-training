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

# To practice with Python, you'll write a couple functions to manipulate a numpy array,
# as well as a main script to run those functions on a sample array

# This function fills a numpy array with values from data_list in order.
# If size is specified, the array is declared with shape (1, size). If size is 
# unspecified, the array is declared with the same number of rows and columns, which is math.sqrt(len(data_list))
def fillArray(data_list, size=None):
    arr = None
    if size == None:
        # check your work:
        arr = np.empty((int(math.sqrt(len(data_list))),int(math.sqrt(len(data_list)))))
        if (arr.shape == (math.sqrt(len(data_list)), math.sqrt(len(data_list)))): print("Array Initialized Correctly!")
    else:
        arr = np.empty((1,size))
        if (arr.shape == (1, size)): print("Array Initialized Correctly!") # check your work: prints the shape of the array
    for i, item in enumerate(data_list):
      arr[int(i / arr.shape[0])][i % arr.shape[0]] = item
    
    # returns the array
    return arr

# Lists are a common Python container, similar to vectors in C++ and MATLAB
data_list = [1, 2, 3, 4] # this is a really simple list, with 5 elements

# array in a variable
arr = fillArray(data_list)

arr_mod = np.cos(np.log(np.abs(arr)))

arr_3d = np.expand_dims(arr_mod, 2)

print(f"Final Array: \n{arr_3d}")
