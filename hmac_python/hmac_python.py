# Hmac python
# 
# ### Challenge Name: hmac_generate (/embsec/hmac_python/hmac_generate)
# 
# 
#     The serial device will send you a variable-length frame of data. The data
#     frame will begin with a short, little-endian integer size of the data to 
#     follow. You must generate an HMAC-SHA256 signature using the key in 
#     'hmackeyfile0.bin'.
#     
#     The data frame you will receive from the device will be formatted as follows:
#     
#     [ 0x2   ] [   variable...   ]
#     ------------------------------
#     | Size   |     Data          |
#     ------------------------------
#     
#     You must send a 32-byte HMAC-SHA256 signature to the serial device.
#     
#     [     0x20     ]
#     ----------------
#     |  HMAC(Data)  |
#     ----------------
#     
#     1. Read the HMAC key from 'hmackeyfile0.bin'
#     2. Read the size of the data from the serial device
#     3. Read the data from the serial device
#     4. Generate and send a HMAC-SHA256 over the data
#     5. Read the response
#     
# 
# 
from embsec import Serial

def hmac_generate():
    ser = Serial("/embsec/hmac_python/hmac_generate")
    # Your code goes here!

hmac_generate()
### Challenge Name: hmac_verify (/embsec/hmac_python/hmac_verify)
# 
# 
#     The serial device will send you a series of messages in the format
#     described below. For each message you must check the attached signature 
#     If verification fails, you must respond with a zero-byte '\x00'. If 
#     verification passes, you must respond with a one-byte '\x01'. When the
#     length of the message you are about to receive is zero , read a newline-
#     terminated flag.
# 
#     The serial device will send signed messages in the following format:
# 
#     ----------------------------------------
#     [ 0x2 ] [  Size bytes    ] [   0x20   ]
#     ----------------------------------------
#     | Size |     Data         | HMAC(Data) |
#     ----------------------------------------
# 
# 
from embsec import Serial

def hmac_verify():
    ser = Serial("/embsec/hmac_python/hmac_verify")
    # Your code goes here!

hmac_verify()
