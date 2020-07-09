
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
  // Implement me!!
}

uint8_t uart_read(uint8_t uart, int blocking, int *read)
{
  // Implement me!!
}

void uart_write(uint8_t uart, uint32_t data)
{
  // Implement me!!
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
    