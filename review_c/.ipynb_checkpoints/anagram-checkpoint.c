#include <stdio.h>
#include <stdint.h>
#include "uart.h"

uint8_t isAnagram (char* str_a, char* str_b) {
    int ind = 0;
    char characters[25];
    for (int l = 0; l < 25; l++){
        characters[l] = 0;
    }

    while (str_a[ind] != '\0'){
        ind++;
    }
    
    for (int z = 0; z <= ind; z++){
        if (str_a[z] != ' ' && str_a[z] != '\0'){
            characters[z] = str_a[z];
        }
    }
    
    int ind2 = 0;
    while (str_b[ind2] != '\0'){
        for (int h = 0; h < 25; h++){
            if (str_b[ind2] != ' ' && characters[h] == str_b[ind2]){
                characters[h] = 0;
                break;
            }
        }
        ind2++;
    }
    
    for (int f = 0; f < 25; f++){
            if (characters[f] != 0){
                return 0;
            }
    }
    return 1;
} 

int main () {
    uart_init(UART2);
    int ret;
    uint8_t numTests;
    char str_a[50];
    char str_b[50];
    uint8_t strPtr = 0;
    uint8_t testResult = 0;
    
    // Get ammount of tests
    numTests = uart_read(UART2, BLOCKING, &ret);

    // Begin main program loop
    for (int i = 0; i < numTests; i++) {
        char value = 0;
        uint8_t strPtr = 0;

        // Recieve first string
        while (value != 10) {
            value = uart_read(UART2, BLOCKING, &ret);
            str_a[strPtr++] = value;
        }
        str_a[(strPtr-1)] = '\0';  // Replaces newline with null terminator
        value = 0;
        strPtr = 0;

        // Recieve next string
        while (value != 10) {
            value = uart_read(UART2, BLOCKING, &ret);
            str_b[strPtr++] = value;
        }
        str_b[(strPtr-1)] = '\0';

        // Return result of test
        testResult = isAnagram(str_a, str_b);
        uart_write(UART2, (char) testResult);
    }

    return 0;
}
