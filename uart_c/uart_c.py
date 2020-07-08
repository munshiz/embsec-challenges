# Uart c
# 
# 
# In class we've talked about programming peripherals in embedded devices using
# their memory-mapped configuration and control registers. For the FLASH memory
# programming example, we followed a process of reading the FLASH section of the 
# datasheetand, identifying what steps our code needs to perform, and determining
# which registers are needed at each step. For this lesson you will be
# re-implementing the UART driver we use in all the C challenges.
# 
# Currently, the UART functions are calling an API designed specifically for our
# microcontroller, the Stellaris LM3S6965. Instead, you are asked to implement the
# same functionality using only the registers and no API calls. Make sure to read
# the datasheet and identify all the necessary steps for getting the UART
# peripheral to work correctly!
# 
# The datasheet can be found here: https://www.ti.com/lit/ds/symlink/lm3s6965.pdf
# Check out the document starting at page 432.
# ### Challenge Name: uart_challenge (/embsec/uart_c/uart_challenge)
# 
# 
# You have been provided a starting C source file (`uart_challenge/uart.c`) for
# implementing the UART functions. Currently, the `uart_write_str`, `nl`, and
# `uart_write_hex` functions are implemented. There is also `UART0_IRQHandler`,
# but you don't need worry about this; we'll learn about it later this week!).
# Your task is to implement the `uart_init`, `uart_read`, and `uart_write`
# functions.
# 
# This challenge will only check that you implemented the functions for the
# `UART2` channel (see the `#define UART2 2` line). However, if you have time and
# are in search of a challenge, you should try to make the three functions also
# perform the correct configuration if given the `UART1` channel. `UART0` is
# reserved for a special reset purpose and has different functionality.
# 
# As we found in the FLASH example, the register definitions and bit fields can be
# found in `inc/lm3s6965.h` in the `lib/stellaris` folder. The easiest way to find
# the correct places in this large header file is to search for 'uart'. Read below
# for more specific instructions on what each function should do.
# 
# **uart_init**: This function sets up the UART clocks and data format
# configuration. For our purposes, the data length should be 8 bits with no parity
# check. The baud rate can be set to a value of 0x0a.0x36 (first part is the
# integer component, second part is the fractional component). At the end of this
# function, UART should be enabled. Remember to implement this for UART2! The
# datasheet is your greatest ally in figuring out how to achieve this.
# 
# **uart_read**: This function should return 8 bit value received by the UART2
# peripheral, and place a success value in the variable pointed to be `read`.
# There are two types of reads: blocking and non-blocking. For a blocking read,
# the function should wait until received data is available (there is a register
# that will tell you this!) and return the data along with `1` in the `read`
# variable. For a non-blocking read, the function should check if data is
# available. If available, return the received value and place `1` in the `read`
# variable. Otherwise, return `0` and place `0` in the `read` variable.
# 
# **uart_write**: This function should perform a blocking write to the UART data
# output, where the value is taken from the `data` function argument. Since the
# function blocks, it should wait to transmit data until the UART is *not* busy.
# 
# All of this functionality will be evaluated with the test routine in
# `uart_challenge/uart_challenge.c` . This routine is very similar to the
# `intro_c` challenge, where this time **you** wrote the UART driver code and the
# blocking/non-blocking functionality should be exercised.
# 
# Please ask questions! Whether they be about the datasheet, what the register
# definitions are, how to use the C binary logic operators to create the right
# values; this is not a simple assignment. There is much to learn about embedded
# programming and peripheral control procedures! 
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def uart_challenge():
    subprocess.check_output([f'(cd uart_challenge && make CHALLENGE=uart_challenge)'], shell=True)
    resp0, resp1, resp2 = embsec.grade_emulated(f'./uart_challenge/gcc/main.bin', f'/embsec/uart_c/uart_challenge')
    stdout, stdin = resp2
    return (extract_flag(stdout))
    
uart_challenge()

