
// Hardware Imports
#include "inc/hw_types.h" // Boolean type
#include "inc/hw_ints.h" // Interrupt numbers

// Driver API Imports
#include "driverlib/sysctl.h" // System control API (clock/reset)
#include "driverlib/interrupt.h" // Interrupt API

// Application Imports
#include "uart.h"

int main() {

  char flag[64];
  int ret;
  int i;
  char resp;


  // Initialize!!
  // Enable UART0 Interrupt!!
  // Enable Interrupts!!

  uart_write_str(UART2, "Device is booted!\n");

  // Initialize flag buffer
  for (i = 0; i < 64; i++) {
    flag[i] = 0;
  }
  
  // Do 10 non-blocking reads - assumes the flag is longer than 10 characters
  for (i = 0; i < 10; i++){
    ret = 0; // Clear previous result
    while (ret == 0){
      resp = uart_read(UART2, NONBLOCKING, &ret); // Wait for successful read
    }
    flag[i] = resp;
  }

  // Rest of reads are blocking - stops at newline
  flag[i] = uart_read(UART2, BLOCKING, &ret); // i == 11
  while(flag[i] != '\n'){
      i++;
      flag[i] = uart_read(UART2, BLOCKING, &ret);
  }
  uart_write_str(UART2, flag);
  
  return 0;
}
    