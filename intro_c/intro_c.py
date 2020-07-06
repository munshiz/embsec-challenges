# Intro c
# 
# In this lesson you will learn how to interact with the course system. This
# course is split up into a series of lessons each with specific learning goals.
# Each lesson contains a series of challenge for you to complete. The challenges
# will require you to learn from online resources such as https://docs.python.org/,
# https://en.cppreference.com/w/c/language, and, our favorite, https://stackoverflow.com/.
# 
# After completing a given challenge, a flag will be awarded to you!
# ### Challenge Name: read_example (/embsec/intro_c/read_example)
# 
# These introductory C challenges somewhat mirror the serial device you
# interacted with in the introductory Python challenges. In `read_example`,
# you waited for a full line to be received from the serial connection. In this
# C version, you will be reading in the flag string from the serial port byte-by-byte
# and sending back a full string to the host. If you had two serial ports, you
# could think of this as receiving the flag from one device, and sending it to
# the other!
# 
# To complete this challenge, you will need to use the serial communication
# functions in `uart.c`. Remember to `#include` the UART header file
# (`uart.h`) in your solution. Pay attention to the `if` statements in those
# functions; you may have to do some setup at the beginning of your program.
# The C challenges work differently from the Python challenges. You have to write
# your own C source file, where the name is determined by the challenge (you can
# see the expected file name in the python window below following `f'gcc`).
# For this challenge, a skeleton program has been provided for you that
# implements the necessary `main` function. In future challenges, you will
# likely have to make the file yourself.
# 
# To complete this challenge, your solution must complete the following steps:
# 
#     1. Read newline-terminated flag string from the host, byte-by-byte
#     2. Send the full flag as a string back to the host
# 
# Resources:
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def read_example():
    subprocess.check_output([f'(cd read_example && make CHALLENGE=read_example)'], shell=True)
    resp0, resp1, resp2 = embsec.grade_emulated(f'./read_example/gcc/main.bin', f'/embsec/intro_c/read_example')
    stdout, stdin = resp2
    return (extract_flag(stdout))
    
read_example()

### Challenge Name: write_example (/embsec/intro_c/write_example)
# 
# This challenge is similar to the previous one. The same setup applies to
# this one! The functionality to implement is listed below:
# 
#     1. Write a newline-terminated string to the host
#     2. Read newline-terminated flag string from the host, byte-by-byte
#     3. Send the full flag as a string back to the host
# 
# Resources:
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def write_example():
    subprocess.check_output([f'(cd write_example && make CHALLENGE=write_example)'], shell=True)
    resp0, resp1, resp2 = embsec.grade_emulated(f'./write_example/gcc/main.bin', f'/embsec/intro_c/write_example')
    stdout, stdin = resp2
    return (extract_flag(stdout))
    
write_example()

