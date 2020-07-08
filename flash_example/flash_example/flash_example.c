
// Hardware Imports
#include "inc/hw_memmap.h" // Peripheral Base Addresses
#include "inc/lm3s6965.h" // Peripheral Bit Masks and Registers

// Application Imports
#include "uart.h"

int main(void)
{

    uart_init(UART2);

    // Erase second 1 KB block    
    FLASH_FMA_R &= ~(FLASH_FMA_OFFSET_M); // Clear address field
    FLASH_FMA_R |= 0x00000C00; // Address 1024
    FLASH_FMC_R |= (FLASH_FMC_WRKEY | FLASH_FMC_ERASE); // Set write Key and erase bit
    while (FLASH_FMC_R & FLASH_FMC_ERASE); // Wait until erase bit is 0

    // Program first 32-bit value (address 0x400 = 1024)
    FLASH_FMA_R &= ~(FLASH_FMA_OFFSET_M); // Clear address field
    FLASH_FMA_R |= 0x00000C00; // Address 1024
    FLASH_FMD_R = 0x12345678; // Data value
    FLASH_FMC_R |= (FLASH_FMC_WRKEY | FLASH_FMC_WRITE); // Set write key and write bit
    while (FLASH_FMC_R & FLASH_FMC_WRITE); // Wait until write bit is 1

    // Program second 32-bit value (address 0x404 = 1028)
    FLASH_FMA_R &= ~(FLASH_FMA_OFFSET_M);
    FLASH_FMA_R |= 0x00000C04;
    FLASH_FMD_R = 0xDEADBEEF;
    FLASH_FMC_R |= (FLASH_FMC_WRKEY | FLASH_FMC_WRITE);
    while (FLASH_FMC_R & FLASH_FMC_WRITE);

    // Program second 32-bit value (address 0x408 = 1032)
    FLASH_FMA_R &= ~(FLASH_FMA_OFFSET_M);
    FLASH_FMA_R |= 0x00000C08;
    FLASH_FMD_R = 0xBAD01234;
    FLASH_FMC_R |= (FLASH_FMC_WRKEY | FLASH_FMC_WRITE);
    while (FLASH_FMC_R & FLASH_FMC_WRITE);

    // Program second 32-bit value (address 0x40C = 1036)
    FLASH_FMA_R &= ~(FLASH_FMA_OFFSET_M);
    FLASH_FMA_R |= 0x00000C0C;
    FLASH_FMD_R = 0xABCDEF00;
    FLASH_FMC_R |= (FLASH_FMC_WRKEY | FLASH_FMC_WRITE);
    while (FLASH_FMC_R & FLASH_FMC_WRITE);

    // Print out the programmed flash values
    uint32_t *address = (uint32_t*)0x00000C00;
    int i;
    for (i = 0; i < 4; i++){
        uart_write_str(UART2, "Flash value at address ");
        uart_write_hex(UART2, (uint32_t)address);
        uart_write_str(UART2, ": ");
        uart_write_hex(UART2, *(address));
        uart_write_str(UART2, ".   ");
        address+=1;
    }
    nl(UART2);

    
    // Read in flag
    char flag[50];
    int ret;
    for (i = 0; i < 50; i++){
        flag[i] = 0;
    }
    
    i = 0;
    flag[i] = uart_read(UART2, BLOCKING, &ret);
    while(flag[i] != '\n'){
        i += 1;
        flag[i] = uart_read(UART2, BLOCKING, &ret);
    }
    uart_write_str(UART2, flag);
    
  return 0;
}
