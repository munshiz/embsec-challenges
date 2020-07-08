# Review python
# 
# 
# In this guided lab session we will review programming in
# Python. We'll mostly cover control flow, lists, dictionaries,
# and the struct module.
# During this lab, we'll do one challenge together, one in pairs,
# and you will do one on your own.
# Good luck! And remember that lab is a good
# time to ask questions!
# ### Challenge Name: review_notes (/embsec/review_python/review_notes)
# 
# 
# Here, we are going to remind you of some functions of the Python
# language. We'll talk about lists, dictionaries, loops and iterating,
# and control flow.
# 
# Lists - a collection of data types. The items in a list can be altered,
# and have a fixed order. Also, there can be duplicates in a list. Items in
# a list are usually accessed by their index, which starts at 0.
# 
# You can create an empty list, or initialize it with some items already in it
# 
#     >> list_a = []  # an empty list
# 
#     >> list_b = [1, 2, 'blah']  # this list is initialized with data, the data can be mixed types!
# 
# Add new entries to the end of a list with '.append()', or join lists with '+'
# 
# Dictionary - a collection of data types, where each entry has a key
# associated with it. This key, not an index, is used to access the entires
# because a dictionary doesn't have a fixed order like a list.
# A dictionary can't have entries with duplicate keys.
# 
# Create dictionaries similarly to lists, and access the items by their key
# 
#     >> dict_a = {}  # an empty dictionary
# 
#     >> dict_b = {'key1': 'val1', 'key2': 2}
# 
#     >> dict_b['key_2']
# 
#     >> 2
# 
# There are many ways to add to a dictionary, here let's look at two:
# 
#     >> mydict = {}
# 
#     >> mydict['key1'] = 123  # option 1: use a new index key
# 
#     >> mydict.update({'key2': 456})  # option 2: use .update() to add one (or more!) items
# 
# Loops - Python provides many ways to loop and iterate through lists and data. For loops, there
# are generally two approaches. The first is by using an index. This is similar to how loops are
# done in C, but is a little cumbersome in Python. Instead, we often iterate through, shown in the
# second example.
# 
# For dictionaries, we need to iterate, as dictionaries don't have indexes. The first dictionary
# example shows how we can iterate through the keys, and access their entries. An approach that is
# usually better is to iterate through the keys and values together, shown in the second dictionary
# example.
# 
# Control flow - Besides the 'if' 'else' statements you will see in following examples, it may be
# handy to use the 'break' and 'continue' statements in loops. These serve different purposes - 'break'
# exits a loop completely, while 'continue' just skips to the next iteration of the loop. There is
# also the 'pass' statement, which is just a placeholder and does nothing.
# 
# The following code cell demonstrates some of these topics. Feel
# free to experiment with them! This cell isn't a challenge, so it
# won't dispense a flag.
# 
# 


mylist = [1, 2, 3]
mydict = {'key1': 1, 'key2': 2, 'key3': 3}

for i in range(0, len(mylist)):  # using an index
    pass

for item in mylist:  # iterating
    pass

for key in mydict:  # the basic approach
    value = mydict[key]  # an extra step is needed to access the entry

for key, value in mydict.items():  # a more flexible approach
    value += 1  # let's add one to each entry

### Challenge Name: splitting_integers (/embsec/review_python/splitting_integers)
# 
# 
# (FOLLOW ALONG WITH INSTRUCTOR)
# 
# Generate a random unsigned integer (a value between 0, 2^32), using the string
# 'splitting_integers' to seed random. Represent this
# integer as two little endian unsigned shorts, packed together using the struct
# module. The first short will represent the upper half of the integer’s bits,
# while the second short will represent the lower bits.
# 
# Resources:
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
from embsec import Serial

def splitting_integers():
    ser = Serial("/embsec/review_python/splitting_integers")
    # Your code goes here!

splitting_integers()
### Challenge Name: skeleton_script (/embsec/review_python/skeleton_script)
# 
# 
# (DO IN PAIRS)
# 
# Fill in the blanks to complete this script.
# This will generates a list of random values, takes the sum of all of them.
# Additionally, it constructs a dictionary that keeps track of how many
# occurrences of each number there are in the list.
# 
# 

import random

random.seed(0xDEADBEEF)

mylist = []  # an empty list

mydict = ... # TODO: create an empty dictionary

mysum = 0  # start accumulator at zero

for ... # TODO: set up this loop to run 10 times
    myrandom = ...  # TODO: generate a random number such that 0 <= myrandom <= 10
    ...  # TODO: add the random number to the mylist

    ... # TODO: keep track of how many times this number has occured, using mydict.
        # (cont'd from above) this will take a few lines of code. How are you
        # going to handle the first time a number appears?

    ... # TODO: accumulate the random values in mysum

#  Print out all our results:
print("Final list:")
print(str(mylist))
print("Final dictionary:")
print(str(mydict))
print("Final sum:")
print(str(mysum))

#  Ignore this, this is for the grader:
import pickle
from embsec import Serial
def test_script():
    ser = Serial('/embsec/review_python/skeleton_script')
    ser_dat = pickle.dumps((mylist, mydict, mysum))
    ser.write(ser_dat + b'\n')
    return ser.read_until()

test_script()
### Challenge Name: integer_flipping (/embsec/review_python/integer_flipping)
# 
# 
# (DO AFTER LAB)
# 
# Generate any non-zero random unsigned short (values between 1 and 2^16). Additionally,
# multiply this value by two. Pack these two values together in a struct of big-endian
# unsigned short, and unsigned integer in the following format. Send this over serial.
# 
# 
#     -------------------------------------------------------------------------------------
#     | random value (datatype = unsigned short) | doubled value (datatype = unsigned int)|
#     -------------------------------------------------------------------------------------
# 
# 
# It may be helpful to use the splitting_integers solution we wrote together in
# lab to guide your solution.
# 
# Take a look at the Struct module documentation below to see how to specify endianness,
# datatypes, and pack multiple values together into structs.
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
from embsec import Serial

def integer_flipping():
    ser = Serial("/embsec/review_python/integer_flipping")
    # Your code goes here!

integer_flipping()
