# Hmac c
# 
# ### Challenge Name: hmac_generate (/embsec/hmac_c/hmac_generate)
# 
# 
#         The host tool will send you a variable-length frame of data. The data
#         frame will begin with a short, little-endian integer size of the data to 
#         follow. You must generate an HMAC-SHA256 signature using the key in 
#         'hmackeyfile0.bin'.
#     
#         The data frame you will receive from the device will be formatted as follows:
#     
#         [ 0x2   ] [   variable...   ]
#         ------------------------------
#         | Size   |     Data          |
#         ------------------------------
#     
#         You must send a 32-byte HMAC-SHA256 signature to the serial device.
#     
#         [     0x20     ]
#         ----------------
#         |  HMAC(Data)  |
#         ----------------
#     
#         1. Read the HMAC key from 'hmackeyfile0.bin'
#         2. Read the size of the data from the serial device
#         3. Read the data from the serial device
#         4. Generate and send a HMAC-SHA256 over the data
#         5. Read the response
#     
#     
# 
import embsec
import subprocess
from core.util import extract_flag

def hmac_generate():
    subprocess.check_output([f'gcc -I../../lib/uart hmac_generate.c ../../lib/uart/uart_linux.c -o hmac_generate'], shell=True)
    stdout, stdin = embsec.grade_c(f'./hmac_generate', f'/embsec/hmac_c/hmac_generate')
    
    return (extract_flag(stdout))
    
hmac_generate()

### Challenge Name: hmac_verify (/embsec/hmac_c/hmac_verify)
# 
# 
#         The host tool will send you a series of messages in the format
#         described below. For each message you must check the attached signature 
#         If verification fails, you must respond with a zero-byte '\x00'. If 
#         verification passes, you must respond with a one-byte '\x01'. When the
#         length of the message you are about to receive is zero , read a newline-
#         terminated flag.
#     
#         The serial device will send signed messages in the following format:
#     
#         ------------------------------------------
#         [ 0x2 ] [   variable...    ] [    0x20   ]
#         ------------------------------------------
#         | Size   |     Data         | HMAC(Data) |
#         ------------------------------------------
#     
# 
import embsec
import subprocess
from core.util import extract_flag

def hmac_verify():
    subprocess.check_output([f'gcc -I../../lib/uart hmac_verify.c ../../lib/uart/uart_linux.c -o hmac_verify'], shell=True)
    stdout, stdin = embsec.grade_c(f'./hmac_verify', f'/embsec/hmac_c/hmac_verify')
    
    return (extract_flag(stdout))
    
hmac_verify()

