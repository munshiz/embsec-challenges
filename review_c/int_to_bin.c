#include <stdio.h>
#include <stdint.h>
#include "uart.h"

void intToBin (uint8_t target, char* buffer) {
    /* Your code goes here */

} 

int main () {
    uart_init(UART2);
    uint8_t value;
    int ret;
    char binaryStr[9];

    // Begin main program loop
    while (value != 10) {
        value = uart_read(UART2, BLOCKING, &ret);
        intToBin(value, binaryStr);
        uart_write_str(UART2, binaryStr);
    }

    return 0;
}
