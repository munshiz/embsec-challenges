# One time pad
# 
# This lab covers an security flaw that arises in the one time pad when the same pad is used more than once. When 
# two messages are XORed with the same pad, you can XOR the ciphertexts together to get rid of the pad entirely. Use 
# this lab to explore how to XOR two strings, and then crack this poor implementation of the "Two time pad." ### Challenge Name: xor (/embsec/one_time_pad/xor)
# 
# 
# The XOR operation is very common in cryptography and security, since it is very useful and also very fast. It's used in
# many algorithms, including AES and the one time pad. Here, use the Python bitwise XOR to XOR two strings together.
#     
#     1. Read in two byte strings of length 16 from the serial device
#     2. Do a bitwise XOR on each character
#     3. Make a byte string out of the XORed result of each pair of characters
#     4. Send the byte string back over the serial
# 
# Resources:
# <https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html>
# 
# Additional resources (For the one-line solution. Do this AFTER completing it for the first time if you want an added challenge):
# <https://docs.python.org/3.3/library/functions.html#zip>
# 
# 
from embsec import Serial

def xor():
    ser = Serial("/embsec/one_time_pad/xor")
    # Your code goes here!

xor()
### Challenge Name: two_time_pad (/embsec/one_time_pad/two_time_pad)
# 
# 
# The one time pad (OTP) is theoretically a perfectly secure encryption method that cannot be cracked. However,
# the main downside is that you must first exchange a pre-shared key that is the same size as the plaintext. Poor
# implementation of the OTP leads to severe vulnerabilities.
# 
# In this challenge, you will be given two ciphertexts which have been XORed using the same OTP. It is your job to
# extract the message from these ciphertexts given them and a list of possible plaintexts.
# 
#     1. Read in the two byte string ciphertexts of length 16
#     2. Read in the list of all possible plaintexts from "plaintexts.txt"
#     3. Perform your attack
#     4. Send back the two decoded ciphertexts (order does not matter)
# 
# Both of the plaintext strings will be contained within "plaintexts.txt"
# 
# The key to this attack is that when you XOR something with itself, it becomes zero. So for any number x, x ^ x is 0. 
# Here, you will be given two ciphertexts which look like A ^ K and B ^ K. If you XOR these together (A ^ K ^ B ^ K), 
# the key will cancel out, leaving you witl A ^ B. After this, cryptanalysis comes in to finish guessing the message. 
# However, in place of complicated cryptanalysis, you have been given a list of possible plaintexts which you will use 
# to crack the one time pad. 
# 
# Resources:
# <https://en.wikipedia.org/wiki/One-time_pad>
# <https://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html>
# <http://www.crypto-it.net/eng/attacks/two-time-pad.html>
# 
# 
from embsec import Serial

def two_time_pad():
    ser = Serial("/embsec/one_time_pad/two_time_pad")
    # Your code goes here!

two_time_pad()
