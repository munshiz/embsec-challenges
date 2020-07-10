
// Hardware Imports
#include "inc/hw_memmap.h" // Peripheral Base Addresses
#include "inc/lm3s6965.h" // Peripheral Bit Masks and Registers
#include "inc/hw_types.h" // Boolean type

// Driver API Imports
#include "driverlib/sysctl.h" // Stystem Control API (clock/reset)

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
  switch (uart){
    case UART0:
      UART0_CTL_R &= ~(UART_CTL_UARTEN); // Disable UART
      UART0_IBRD_R &= ~(UART_IBRD_DIVINT_M); // Set integer baudrate part
      UART0_IBRD_R |= 0x0a;
      UART0_FBRD_R &= ~(UART_FBRD_DIVFRAC_M); // Set fractional baudrate part
      UART0_FBRD_R |= 0x36;
      UART0_LCRH_R &= ~(UART_LCRH_WLEN_M); // Set 8-bit word
      UART0_LCRH_R |= UART_LCRH_WLEN_8;
      UART0_CTL_R |= UART_CTL_UARTEN; // Enable UART
      break;
    case UART1:
      UART1_CTL_R &= ~(UART_CTL_UARTEN); // Disable UART
      UART1_IBRD_R &= ~(UART_IBRD_DIVINT_M); // Set integer baudrate part
      UART1_IBRD_R |= 0x0a;
      UART1_FBRD_R &= ~(UART_FBRD_DIVFRAC_M); // Set fractional baudrate part
      UART1_FBRD_R |= 0x36;
      UART1_LCRH_R &= ~(UART_LCRH_WLEN_M); // Set 8-bit word
      UART1_LCRH_R |= UART_LCRH_WLEN_8;
      UART1_CTL_R |= UART_CTL_UARTEN; // Enable UART
      break;
    case UART2:
      UART2_CTL_R &= ~(UART_CTL_UARTEN); // Disable UART
      UART2_IBRD_R &= ~(UART_IBRD_DIVINT_M); // Set integer baudrate part
      UART2_IBRD_R |= 0x0a;
      UART2_FBRD_R &= ~(UART_FBRD_DIVFRAC_M); // Set fractional baudrate part
      UART2_FBRD_R |= 0x36;
      UART2_LCRH_R &= ~(UART_LCRH_WLEN_M); // Set 8-bit word
      UART2_LCRH_R |= UART_LCRH_WLEN_8;
      UART2_CTL_R |= UART_CTL_UARTEN; // Enable UART
      break;
    default:
      break;
  }
}

uint8_t uart_read(uint8_t uart, int blocking, int *read)
{
  switch (uart){
    case UART0:
      if (blocking) {
        while (UART0_FR_R & UART_FR_RXFE); // Wait for byte (FIFO empty)
        *read = 1;
        return UART0_DR_R & 0xFF; // Return Rx value from data register
      } 
      if (UART0_FR_R & UART_FR_RXFF) { // Check if byte is available (FIFO full)
        *read = 1;
        return UART0_DR_R & 0xFF; // Return Rx value
      } else {
        *read = 0;
        return 0;
      }
      break;
    case UART1:
      if (blocking) {
        while (UART1_FR_R & UART_FR_RXFE); // Wait for byte (FIFO empty)
        *read = 1;
        return UART1_DR_R & 0xFF; // Return Rx value from data register
      } 
      if (UART1_FR_R & UART_FR_RXFF) { // Check if byte is available (FIFO full)
        *read = 1;
        return UART1_DR_R & 0xFF; // Return Rx value
      } else {
        *read = 0;
        return 0;
      }
      break;
    case UART2:
      if (blocking) {
        while (UART2_FR_R & UART_FR_RXFE); // Wait for byte (FIFO empty)
        *read = 1;
        return UART2_DR_R; // Return Rx value from data register
      } 
      if (UART2_FR_R & UART_FR_RXFF) { // Check if byte is available (FIFO full)
        *read = 1;
        return UART2_DR_R; // Return Rx value
      } else {
        *read = 0;
        return 0;
      }
      break;
    default:
      return 0;
      break;
  }
}

void uart_write(uint8_t uart, uint32_t data)
{
  switch (uart){
    case UART0:
      while (UART0_FR_R & UART_FR_BUSY); // Wait for UART ready
      UART0_DR_R = data; // Write data
      break;
    case UART1:
      while (UART1_FR_R & UART_FR_BUSY); // Wait for UART ready
      UART1_DR_R = data; // Write data
      break;
    case UART2:
      while (UART2_FR_R & UART_FR_BUSY); // Wait for UART ready
      UART2_DR_R = data; // Write data
      break;
    default:
      break;
  }
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
  // Implement Me!!
}
    