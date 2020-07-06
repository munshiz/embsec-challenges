# Intro python
# 
# In this lesson you will learn how to interact with the course system with Python. 
# This course is split up into a series of lessons each with specific learning goals.
# Each lesson contains a series of challenge for you to complete. The challenges
# will require you to learn from online resources such as https://docs.python.org/,
# https://en.cppreference.com/w/c/language, and, our favorite, https://stackoverflow.com/.
# 
# After completing a given challenge, a flag will be dispensed to you!
# ### Challenge Name: read_example (/embsec/intro_python/read_example)
# 
# Each challenge will require you to interact with a system over a serial connection. 
# The python interface for communicating with this system is identical to the pyserial
# package (https://pythonhosted.org/pyserial/) used to communicate with traditional 
# serial ports. Instead of using serial.Serial, you will use embsec.Serial and instead
# of connecting to /dev/<your device>, you will connect to /embsec/<lesson name>/<challenge name>. 
# 
# For example, in this challenge you will connect to /embsec/intro_python/read_example. Or in code:
# 
#     >> from embsec import Serial
#     >> ser = Serial('/embsec/intro_python/read_example')
# 
# Now that you have a connection, you will be able to read and write to the system. For this
# challenge, all you need to do is read from the serial connection and print out the
# received data until a newline character is received
# 
#     >> d = ser.read()
#     >> while d != b'\n':
#     >>     print(d.decode(), end='')
#     >>     d = ser.read()
# 
# 
from embsec import Serial

def read_example():
    ser = Serial("/embsec/intro_python/read_example")
    # Your code goes here!

read_example()
### Challenge Name: write_example (/embsec/intro_python/write_example)
# 
# 
# For this challenge, we can follow the same set up as above by importing Serial
# from embsec, and connecting to ('/embsec/intro_python/write_example') . After, all you need to do is
# write a string to the serial device, and then read from the serial connection
# until the newline character is received, and print out the received message.
# 
#     >> ser = Serial('/embsec/intro_python/write_example')
#     >> ser.write(b'hello world!\n')
#     >> print(ser.read_until())
# 
# 
from embsec import Serial

def write_example():
    ser = Serial("/embsec/intro_python/write_example")
    # Your code goes here!

write_example()
