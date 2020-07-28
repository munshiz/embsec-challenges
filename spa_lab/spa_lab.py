# Spa lab
# 
# 
# Practice simple power analysis (SPA) on a password checker that uses strcmp(),
# and see why you should never use it for this!
# ### Challenge Name: spa_easy (/embsec/spa_lab/spa_easy)
# 
# 
# The traces in this challenge are nicely triggered and aligned. Take a look at the
# code provided to you to understand how to get and plot multiple traces together, then
# modify this code to suit your needs. When you have found the correct PIN, the legend on
# the plot will say so. Send this PIN value with the correct_pin variable over serial.
# 
# 

from embsec import Serial
import spa_client as sc

def spa_easy():
    ser = Serial("/embsec/spa_lab/spa_easy")
    client = sc.DataClient(path='passwordtrigger')

    # dat = client.fetch('1234')
    # sc.plot_trace(dat, smooth=20)
    # dat = client.fetch('5678')
    # sc.plot_trace(dat, smooth=20)
    # sc.show_plot()

    correct_pin = 1234  # set this to the answer you find, the code below will submit it
    ser.write('{}\n'.format(correct_pin).encode())  # send PIN
    return ser.read_until()  # gets flag


spa_easy()
### Challenge Name: spa_hard (/embsec/spa_lab/spa_hard)
# 
# 
# Now that you've worked on that nice waveform, try a harder one! Try and see which features appear
# dependent on the passcode.
# 
# 

from embsec import Serial
import spa_client as sc

def spa_hard():
    ser = Serial("/embsec/spa_lab/spa_hard")
    client = sc.DataClient(path='password')

    # dat = client.fetch('1234')
    # sc.plot_trace(dat, smooth=20)
    # dat = client.fetch('5678')
    # sc.plot_trace(dat, smooth=20)
    # sc.show_plot()

    correct_pin = 1234  # set this to the answer you find, the code below will submit it
    ser.write('{}\n'.format(correct_pin).encode())  # send PIN
    return ser.read_until()  # gets flag


spa_hard()
