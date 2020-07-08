
#include "uart.h"

int main() {
  uart_init(UART2);

  char flag[64];
  int ret;
  int i;
  char resp;

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
    