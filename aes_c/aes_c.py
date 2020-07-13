# Aes c
# 
#  In this lesson you will learn how to use the C library
# BearSSL to encrypt and decrypt with the AES algorithm. This
# lesson requires an understanding of C IO, byte manipulation,
# and endianess. Good luck!
# ### Challenge Name: aes_decrypt (/embsec/aes_c/aes_decrypt)
# 
# 
#     The host tool is sending you an encrypted messaged. The message 
#     is in the following format:
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
import embsec
import subprocess
from core.util import extract_flag

def aes_decrypt():
    subprocess.check_output([f'gcc -I../../lib/uart aes_decrypt.c ../../lib/uart/uart_linux.c -o aes_decrypt'], shell=True)
    stdout, stdin = embsec.grade_c(f'./aes_decrypt', f'/embsec/aes_c/aes_decrypt')
    
    return (extract_flag(stdout))
    
aes_decrypt()

### Challenge Name: aes_encrypted_echo (/embsec/aes_c/aes_encrypted_echo)
# 
# 
#     The host tool is sending you an encrypted message. Decrypt
#     the message and send it back encrypted with a different IV. The 
#     message needs to be formatted as follows:
#     
#     [ 0x10 ] [      0x2      ] [ variable...]
#     ----------------------------------------
#     |  IV   | Ciphertext Size | Ciphertext |
#     ----------------------------------------
#     
#     1. Read the AES key from 'aeskeyfile.bin'
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
import embsec
import subprocess
from core.util import extract_flag

def aes_encrypted_echo():
    subprocess.check_output([f'gcc -I../../lib/uart aes_encrypted_echo.c ../../lib/uart/uart_linux.c -o aes_encrypted_echo'], shell=True)
    stdout, stdin = embsec.grade_c(f'./aes_encrypted_echo', f'/embsec/aes_c/aes_encrypted_echo')
    
    return (extract_flag(stdout))
    
aes_encrypted_echo()

