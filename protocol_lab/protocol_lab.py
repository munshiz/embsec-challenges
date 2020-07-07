# Protocol lab
# 
# 
# Here we will walk through the steps of building up a firmware update
# protocol. We are going to use Python to implement the updater tool
# side of the protocol (the other side being the bootloader, written
# in C). This protocol can get fairly complex, so focus on structuring
# your code well so that it can be extended a re-used throughout the
# challenges!
# ### Challenge Name: sending_data (/embsec/protocol_lab/sending_data)
# 
# 
# Implement the protocol described here, and send the contents of the
# sending_data.bin file to the bootloader.
# 
# Protocol Description: Messages are of the format specified below,
# and are always 64 bytes. Datatypes are all big-endian.
# 
#              [short]        [58 bytes]  [short]    [short]
#      -------------------------------------------------------
#     | message type (short) | data ... | unused_1 | unused_2 |
#      -------------------------------------------------------
# 
# To begin a firmware update, send a BEGIN message (message type = 1)
# to the bootloader, the other fields can be set to anything for this
# message.
# 
# Next, send the sending_data.bin file contents to the bootloader in chunks. For
# this, send FIRMWARE (message type = 2) messages, where the data field
# is the partial file contents.
# 
# Once you have sent the entire file, send a DONE (type = 3) message and
# then listen for a line that will contain the flag.
# 
# For simplicity, the firmware file size is always a multiple of 58 bytes.
# 
# 
# 
from embsec import Serial

def sending_data():
    ser = Serial("/embsec/protocol_lab/sending_data")
    # Your code goes here!

sending_data()
### Challenge Name: heartbeat (/embsec/protocol_lab/heartbeat)
# 
# 
# The bootloader can only take so much data at once and is getting bogged down by
# the constant stream of data sent its way. It cannot write the firmware to memory
# as fast as it's receiving new data.
# 
# Now, the bootloader will send a OK (message type = 4) message when it is all
# set to be sent another messsage. So, before sending any message, wait for an
# OK message, and then send just one message. After you have sent a DONE message,
# the bootloader will send an OK message, and then a flag.
# 
# 
from embsec import Serial

def heartbeat():
    ser = Serial("/embsec/protocol_lab/heartbeat")
    # Your code goes here!

heartbeat()
### Challenge Name: noise (/embsec/protocol_lab/noise)
# 
# 
# Your data is being sent over a noisy medium - some messages are getting corrupted
# and the bootloader cannot interpret the message, causing firmware update
# failures.
# 
# Add a checksum to the end of the message in the unused_1 field. This checksum is
# the sum of all the bytes in the data field.
# 
# When the bootloader receives any message, it will calculate the checksum. There is a
# chance that an error occured during transmission, and this calculated value may
# differ from the checksum field of the message. If this is the case, the bootloader
# will send a RESEND (message type = 5) message, and expect the last message to be
# re-sent.
# 
# If you receive a RESEND message instead of a OK message, re-send the last frame.
# This includes the DONE message, too!
# 
# 
# 
from embsec import Serial

def noise():
    ser = Serial("/embsec/protocol_lab/noise")
    # Your code goes here!

noise()
### Challenge Name: replay (/embsec/protocol_lab/replay)
# 
# 
# There have been instances of counterfeit update tools being used to upload
# modified firmware to cars. To prevent this, the auto company has tried to
# secure their protocol.
# 
# In order for the bootloader to verify the update tool is legitimate, a handshake
# is added to the beginning of the communication protocol. Now, messages are sent
# as follows:
# 
# 1. The update tool sends a BEGIN message to the bootloader, as before.
# 
# 2. The bootloader responds with a CHALLENGE message (type = 6) where the
#    data field contains a random number.
# 
# 3. The update tool takes the data from the CHALLENGE message and performs a
#    secret mathematical operations on it. The bootloader also knows what this
#    operation is, but you do not. The update tool must respond
#    with an ANSWER message (type = 7) where the data field is the result of the
#    secret mathematical operation on the challenge data.
# 
# 4. If the ANSWER is correct, the communications proceed normally. If incorrect, the
#    bootloader will respond WRONG (type = 8), and not accept any more information for that session.
#    You will have to wait 1 second before starting a new session.
# 
# You are an attacker who has a counterfeit update tool. You need to figure out a way
# to make it through this handshake and send modified firmware. You have attached a
# protocol analyzer to the bus, and can read out all communications. Doing this, you
# have noticed a crucial bit of information: the CHALLENGE data is random, but appears
# to only be values between [0, 255].
# 
# 1. How can you get past this handshake? (HINT: look at the listed resources!)
# 
# 2. Can you get away with observing just one legitimate handshake? How so?
# 
# 3. What is the expected maximum time the attack in question two can take? Remember that
#    penalty for a failed handshake is 1 second, ignore the time the actual
#    handshake takes for now.
# 
# 4. BONUS: implement your attack here, in python. To listen to traffic on the bus,
#    use ser.read(64), and you don't have to worry about checksums for this challenge.
#    Once you have enough information and have waited for a handshake to complete, use
#    ser.write() to mount your attack. Don't worry about the 1 second delay for this
#    attack.
# 
# Resources:
# 
# <https://en.wikipedia.org/wiki/Replay_attack>
# 
# 
# 
from embsec import Serial

def replay():
    ser = Serial("/embsec/protocol_lab/replay")
    # Your code goes here!

replay()
