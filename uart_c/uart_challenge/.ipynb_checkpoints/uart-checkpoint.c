
// Hardware Imports
#include "inc/hw_memmap.h" // Peripheral Base Addresses
#include "inc/lm3s6965.h" // Peripheral Bit Masks and Registers

// Component Header
#include "uart.h"

// UART Channels - You can use these names, but don't uncomment them!
// #define UART0 0
// #define UART1 1
// #define UART2 2

// Reading modes - You can use these names, but don't uncomment them!
// #define NONBLOCKING 0
// #define BLOCKING 1

void uart_init(uint8_t uart)
{ 
  UART2_CTL_R &= ~(UART_CTL_UARTEN);
  UART2_IBRD_R &= 0xFFFF0000;
  UART2_IBRD_R |= 0xA;
  UART2_FBRD_R &= ~(0x3F);
  UART2_FBRD_R |= 0x36;
  UART2_LCRH_R &= ~(0x60);
  UART2_LCRH_R |= UART_LCRH_WLEN_8;
  UART2_CTL_R |= UART_CTL_UARTEN;

}

uint8_t uart_read(uint8_t uart, int blocking, int *read)
{
  // Implement me!!
    if ((UART2_FR_R & UART_FR_RXFE) == UART_FR_RXFE && blocking == NONBLOCKING){  
        *read = 0;
        return 0;
    } 
    while((UART2_FR_R & UART_FR_RXFE) == UART_FR_RXFE){
        continue;
    }
    *read = 1;
    return UART_DR_DATA_M & UART2_DR_R;
}

void uart_write(uint8_t uart, uint32_t data)
{
    while (UART2_FR_R & UART_FR_BUSY == UART_FR_BUSY)
    {
         continue;
    }
    UART2_DR_R = data;
}

void uart_write_str(uint8_t uart, char *str) {
  while (*str) { // Loop until null terminator
    uart_write(uart, (uint32_t)*str++);
  }
}

inline void nl(uint8_t uart) {
  uart_write(uart, '\n');
}

void uart_write_hex(uint8_t uart, uint32_t data) {
  uint32_t nibble;

  for (int shift = 28; shift >= 0; shift -=4) {
    nibble = (data >> shift) & 0xF;
    if (nibble > 9) {
      nibble += 0x37;
    } else {
      nibble += 0x30;
    }
    uart_write(uart, nibble);
  }
}


void UART0_IRQHandler(void)
{
}
    