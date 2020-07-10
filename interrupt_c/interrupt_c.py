# Interrupt c
# 
# 
# We went over interrupts and ISRs in class, seeing how they can be used to
# offload some CPU tasks to the peripherals. As part of the design challenge, you
# are writing a bootloader that connects to python host tools and performs
# firmware updates. Because the bootloader is emulated and we don't have access to
# real hardware, there is a built-in reset functionality that is triggered by
# writing to an un-used UART channel. In this challenge, you will be setting up
# the interrupt for UART0 and writing a simple ISR that resets the emulated
# device.
# 
# Here is the link for the datasheet again: https://www.ti.com/lit/ds/symlink/lm3s6965.pdf
# ### Challenge Name: interrupt_challenge (/embsec/interrupt_c/interrupt_challenge)
# 
# 
# As with the UART challenge, you have been provided with starting `uart.c`,
# `interrupt_challenge.c`, and `startup_gcc.c` files. However, all three UART
# channels are implemented using the hardware registers. Your task is to modify
# the `uart_init` function for the `UART0` case so that it enables the **receive
# interrupt** signal. You will also implement the ISR for UART0, which must clear
# the interrupt flag, check for a specific received value, and then reset the
# device. The ISR must also be defined in `startup_gcc.c`. Finally, you must
# modify the `main` function so that global interrupts are enabled, as we
# discussed during lecture.
# 
# **uart_init**: You must search the Stellaris datasheet to find the correct
# register for enabling the UART0 receive interrupt. Just as last time, you'll
# need to find the correct regsiter definition and bit fields in `inc/lm3s6965.h`
# in the `lib/stellaris` folder. This should only result in one extra line in
# `uart_init`; make sure to enable the interrupt **before** UART is enabled at the
# end of the function!
# 
# **UART0_IRQHandler**: This is the UART0 ISR. As we discussed, the first thing
# you need to do is clear the pending interrupt bit in the correct UART0 register.
# Once again, the datasheet is your best friend! After clearing the receive
# interrupt bit, the ISR needs to check if the value `0x20` was received over the
# UART0 channel. *Hint!* You can still use the `uart_*` functions in the `uart.c`
# file even during an ISR. Finally, if the value `0x20` is received, call the
# `SysCtlReset();` function to restart the device. This is a function from the
# Stellaris Driver library, so you don't need to worry about it. Just call it!
# 
# **startup_gcc.c**: Even though you have written the ISR code, the device still
# needs to know what function to execute when the UART0 interrupt occurs. In
# `startup_gcc.c` there is a large table of functions, most of which say
# `IntDefaultHandler`. To define the UART0 ISR, you must change
# `IntDefaultHandler` to instead say `UART0_IRQHandler` on the line corresponding
# to the 'UART0 Rx and Tx' interrupts. You should be able to tell which line
# corresponds to UART0 by looking at the code in this file. Additionally, you need
# to add a function prototype for `UART0_IRQHandler` in `startup_gcc.c` before the
# vector table definition. You will have to declare it as `extern` because the
# function is actually defined in `uart.c`.
# 
# **main() in interrupt_challenge.c**: This is the main function that runs to test
# your interrupt setup. You'll notice that no UART channels are initialized at the
# start. You'll have to add the appropriate initialization code for the UARTs.
# Second, the global interrupts need to be enabled. The first function needed for
# this, `IntEnable(<interrupt number>)`, will allow the provided interrupt signal
# to pass through the NVIC. You will have to search through the `inc/hw_ints.h`
# file in `lib/stellaris` for the appropriate definition to pass as an argument.
# There should be only one option for specifying the UART0 interrupt signal. The
# second function needed for enabling interrupts is to enable global interrupts to
# the CPU, which you do by calling `IntMasterEnable();`. You don't need to add any
# arguments to this, just make sure it gets called **after** calling `IntEnable`.
# 
# As with the UART challenge, please ask questions! If you need help finding the
# right register definitions in the header files, or the correct interrupt number
# in the interrupts header, we are happy to help. Hopefully you are more
# comfortable reading and understanding the datasheet now, so you should be able
# to find the correct bits to write for enabling the UART0 receive interrupt.
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def interrupt_challenge():
    subprocess.check_output([f'(cd interrupt_challenge && make CHALLENGE=interrupt_challenge)'], shell=True)
    resp0, resp1, resp2 = embsec.grade_emulated(f'./interrupt_challenge/gcc/main.bin', f'/embsec/interrupt_c/interrupt_challenge')
    stdout, stdin = resp2
    return (extract_flag(stdout))
    
interrupt_challenge()

