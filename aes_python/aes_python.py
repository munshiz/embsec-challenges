# Aes python
# 
#  In this lesson you will learn how to use the Python library
# PyCryptodome to encrypt and decrypt with the AES algorithm. This
# lesson requires an understanding of Python IO, byte manipulation,
# and endianess. Good luck!
# ### Challenge Name: aes_decrypt (/embsec/aes_python/aes_decrypt)
# 
# 
#     The serial device is sending you a message encrypted with the key
#     stored in aeskeyfile.bin. The message is in the following format:
#        
#     [ 0x10 ] [      0x2      ] [ variable...]
#     ----------------------------------------
#     |  IV   | Ciphertext Size | Ciphertext |
#     ----------------------------------------
#     
#     1. Read the AES key from 'aeskeyfile0.bin'
#     2. Read the 16 byte initialization vector (IV) from the serial device
#     3. Read the ciphertext size (formatted as a little-endian short) from the serial device
#     4. Read the ciphertext from the serial device
#     5. Decrypt the ciphertext using 128-bit AES in CBC mode
#     
# Resources:
# 
# <https://docs.python.org/3/library/struct.html>
# 
# <https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html>
# 
# 
from embsec import Serial

def aes_decrypt():
    ser = Serial("/embsec/aes_python/aes_decrypt")
    # Your code goes here!

aes_decrypt()
### Challenge Name: aes_encrypt_file (/embsec/aes_python/aes_encrypt_file)
# 
# 
#     You need to send an encrypted message to the serial device. Encrypt
#     the contents of 'plaintext.bin' with the key found in 'aeskeyfile.bin' 
#     and a random IV. The message needs to be formatted as follows:
#     
#     [ 0x10 ] [      0x2      ] [ variable...]
#     ----------------------------------------
#     |  IV   | Ciphertext Size | Ciphertext |
#     ----------------------------------------
# 
#     1. Read the AES key from 'aeskeyfile1.bin'
#     2. Encrypt the plaintext located in 'plaintext.bin'
#     3. Send the IV to the serial device
#     4. Send the ciphertext size (formatted as a little-endian short) to the serial device
#     5. Send the ciphertext to the serial device
#     6. Read the response
# 
# Resources:
# 
# <https://docs.python.org/3/library/struct.html>
# 
# <https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html>
# 
# 
# 
from embsec import Serial

def aes_encrypt_file():
    ser = Serial("/embsec/aes_python/aes_encrypt_file")
    # Your code goes here!

aes_encrypt_file()
### Challenge Name: aes_encrypted_echo (/embsec/aes_python/aes_encrypted_echo)
# 
# 
#     The serial device is sending you an encrypted message. Decrypt
#     the message and send it back encrypt with a different IV. The 
#     message needs to be formatted as follows:
#     
#     [ 0x10 ] [      0x2      ] [ variable...]
#     ----------------------------------------
#     |  IV   | Ciphertext Size | Ciphertext |
#     ----------------------------------------
#     
#     1. Read the AES key from 'aeskeyfile2.bin'
#     2. Read the 16 byte initialization vector (IV) from the serial device
#     3. Read the ciphertext size (formatted as a little-endian short) from the serial device
#     4. Read the ciphertext from the serial device
#     5. Decrypt the ciphertext using 128-bit AES in CBC mode
#     2. Re-encrypt the plaintext with the same key but a new IV
#     3. Send the IV to the serial device
#     4. Send the ciphertext size (formatted as a little-endian short) to the serial device
#     5. Send the ciphertext to the serial device
#     6. Read the response
# 
# 
# 
from embsec import Serial

def aes_encrypted_echo():
    ser = Serial("/embsec/aes_python/aes_encrypted_echo")
    # Your code goes here!

aes_encrypted_echo()
