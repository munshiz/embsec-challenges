// Include the uart header!
#include "uart.h"
int main(void)
{
  // Variable setup
    char flag[50];
    int i;
    for (i = 0; i < 50; i++){
        flag[i] = 0;
    }
  // Initialize serial
    uart_init(UART2);
  // Read characters from serial into a string until a newline is received
    i = 0;
    int ret;
    flag[i] = uart_read(UART2, BLOCKING, &ret);
    while (flag[i] != '\n') {
        i++;
        flag[i] = uart_read(UART2, BLOCKING, &ret);
    }
  // Send the full string back over serial
    uart_write_str(UART2, flag);
  return 0;
}