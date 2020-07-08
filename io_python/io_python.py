# Io python
# 
# In this lesson you will learn about the IO functions of Python.
# This will enable you to read and write files as well as 
# read and write to serial devices such as the secure bootloader 
# you are designing during this course. A series of challenges
# follow which will require you to read Python documentation
# as well as other online resources. Good luck!### Challenge Name: echo_int (/embsec/io_python/echo_int)
# 
# 
#     1. Read a big-endian short from the serial device
#     2. Increment the integer by 1
#     3. Send the integer as a big-endian short back to the serial device
# 
# Resources:
# 
# <https://en.wikipedia.org/wiki/Endianness>
# 
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# 
# <https://docs.python.org/3/library/struct.html>
# 
# 
# 
from embsec import Serial

def echo_int():
    ser = Serial("/embsec/io_python/echo_int")
    # Your code goes here!

echo_int()
### Challenge Name: send_file (/embsec/io_python/send_file)
# 
# 
# 
#     1. Read 'file.bin' from your local system
#     2. Calculate the size
#     3. Send the size as a little-endian short
#     4. Send the file to serial device
# 
#     The serial device expects a little-endian short indicating the size of the
#     incoming data and then size bytes of data. The format is represented below:
#     
#     [ 0x02 ]  [ variable ]
#     ---------------------
#     | Length |  Data... |
#     ---------------------
# 
# Resources:
# 
# <https://en.wikipedia.org/wiki/Endianness>
# 
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# 
# <https://docs.python.org/3/library/struct.html>
# 
# <https://docs.python.org/3/tutorial/inputoutput.html>
# 
# 
from embsec import Serial

def send_file():
    ser = Serial("/embsec/io_python/send_file")
    # Your code goes here!

send_file()
### Challenge Name: send_large_file (/embsec/io_python/send_large_file)
# 
# 
#     1. Read 'large_file.bin' from your local system
#     3. Send the data in frames to the serial device (frame format below)
#     4. Send zero-length frame to indicate end of transmission
# 
#     The serial device expects that a frame begins with a little-endian short 
#     indicating the size of the frame and then frame data. The maximum frame 
#     size is 16 bytes. The frame format is represented below:
#     
#     [ 0x02 ]  [ up to 0xE bytes ]
#     ----------------------------
#     | Length |      Data...    |
#     ----------------------------
#     
# Resources:
# <https://en.wikipedia.org/wiki/Endianness>
# <https://en.wikipedia.org/wiki/Integer_%28computer_science%29>
# <https://docs.python.org/3/library/struct.html>
# <https://docs.python.org/3/tutorial/inputoutput.html>
# <https://pyserial.readthedocs.io/en/latest/shortintro.html>
# 
# 
from embsec import Serial

def send_large_file():
    ser = Serial("/embsec/io_python/send_large_file")
    # Your code goes here!

send_large_file()
