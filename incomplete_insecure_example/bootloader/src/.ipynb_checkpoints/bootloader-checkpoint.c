// Hardware Imports
#include "inc/hw_memmap.h" // Peripheral Base Addresses
#include "inc/lm3s6965.h" // Peripheral Bit Masks and Registers
#include "inc/hw_types.h" // Boolean type
#include "inc/hw_ints.h" // Interrupt numbers
//
#include <string.h>
// Driver API Imports
#include "driverlib/flash.h" // FLASH API
#include "driverlib/sysctl.h" // System control API (clock/reset)
#include "driverlib/interrupt.h" // Interrupt API
// Application Imports
#include "uart.h"
// Forward Declarations
void load_initial_firmware(void);
void load_firmware(void);
void boot_firmware(void);
long program_flash(uint32_t, unsigned char*, unsigned int);
// Firmware Constants
#define METADATA_BASE 0xFC00  // base address of version and firmware size in Flash
#define FW_BASE 0x10000  // base address of firmware in Flash
// FLASH Constants
#define FLASH_PAGESIZE 1024
#define FLASH_WRITESIZE 4
// Protocol Constants
#define OK    ((unsigned char)0x00)
#define ERROR ((unsigned char)0x01)
#define UPDATE ((unsigned char)'U')
#define BOOT ((unsigned char)'B')
// Firmware v2 is embedded in bootloader
extern int _binary_firmware_bin_start;
extern int _binary_firmware_bin_size;
// Device metadata
uint16_t *fw_version_address = METADATA_BASE;
uint16_t *fw_size_address = METADATA_BASE+2;
// Firmware Buffer
unsigned char data[FLASH_PAGESIZE];
int main(void) {
  // Initialize UART channels
  // 0: Reset
  // 1: Host Connection
  // 2: Debug
  uart_init(UART0);
  uart_init(UART1);
  uart_init(UART2);
  // Enable UART0 interrupt
  IntEnable(INT_UART0);
  IntMasterEnable();
  load_initial_firmware();
  uart_write_str(UART2, "Welcome to the BWSI Vehicle Update Service!\n");
  uart_write_str(UART2, "Send \"U\" to update, and \"B\" to run the firmware.\n");
  uart_write_str(UART2, "Writing 0x20 to UART0 will reset the device.\n");
  int resp;
  while (1){
    uint32_t instruction = uart_read(UART1, BLOCKING, &resp);
    if (instruction == UPDATE){
      uart_write_str(UART1, "U");
      load_firmware();
    } else if (instruction == BOOT){
      uart_write_str(UART1, "B");
      boot_firmware();
    }
  }
}
/*
 * Load initial firmware into flash
 */
void load_initial_firmware(void) {
  int size = (int)&_binary_firmware_bin_size;
  int *data = (int *)&_binary_firmware_bin_start;
  uint16_t version = 2;
  uint32_t metadata = (((uint16_t) size & 0xFFFF) << 16) | (version & 0xFFFF);
  program_flash(METADATA_BASE, (uint8_t*)(&metadata), 4);
  int i = 0;
  for (; i < size / FLASH_PAGESIZE; i++){
       program_flash(FW_BASE + (i * FLASH_PAGESIZE), ((unsigned char *) data) + (i * FLASH_PAGESIZE), FLASH_PAGESIZE);
  }
  program_flash(FW_BASE + (i * FLASH_PAGESIZE), ((unsigned char *) data) + (i * FLASH_PAGESIZE), size % FLASH_PAGESIZE);
}
/*
 * Load the firmware into flash.
 */
void load_firmware(void)
{
  int frame_length = 0;
  int read = 0;
  uint32_t rcv = 0;
  uint32_t data_index = 0;
  uint32_t page_addr = FW_BASE;
  uint32_t version = 0;
  uint32_t size = 0;
  uint32_t packet_size=0;
  uint32_t received_fw_bytes = 0;
  // Get version.
  rcv = uart_read(UART1, BLOCKING, &read);
  version = (uint32_t)rcv;
  rcv = uart_read(UART1, BLOCKING, &read);
  version |= (uint32_t)rcv << 8;
  uart_write_str(UART2, "Received Firmware Version: ");
  uart_write_hex(UART2, version);
  nl(UART2);
  // TODO: Read the firmware size from the fw_update tool
  rcv = uart_read(UART1, BLOCKING, &read);
  size = (uint32_t)rcv;
  rcv = uart_read(UART1, BLOCKING, &read);
  size |= (uint32_t)rcv << 8;
  // Compare to old version and abort if older (note special case for version 0).
  uint16_t old_version = *fw_version_address;
  if (version != 0 && version < old_version) {
    uart_write(UART1, ERROR); // Reject the metadata.
    SysCtlReset(); // Reset device
    return;
  } else if (version == 0) {
    // If debug firmware, don't change version
    version = old_version;
  }
  // Write new firmware size and version to Flash
  // Create 32 bit word for flash programming, version is at lower address, size is at higher address
  uint32_t metadata = ((size & 0xFFFF) << 16) | (version & 0xFFFF);
  program_flash(METADATA_BASE, (uint8_t*)(&metadata), 4);
  uart_write(UART1, OK); // Acknowledge the metadata.
  // TODO: Load the firmware into flash memory at 0x10000
  rcv = uart_read(UART1, BLOCKING, &read);
  packet_size = ((uint32_t)rcv)<<8;
  rcv = uart_read(UART1, BLOCKING, &read);
  packet_size |= (uint32_t)rcv;
  int counter=0;//count how many bytes have been written to the buffer
  int writeCounter=0;//count how many times we have written to the flash memory
  uint8_t okMessage=0;
  while(packet_size !=0)
  {
      for(int i=0; i<packet_size;i++)
      {
          rcv = uart_read(UART1, BLOCKING, &read);//reading a byte
          data[counter]=rcv;//allocating the data to the buffer
          counter++;//increment the counter
          if(counter==FLASH_PAGESIZE)
          {
              //program the flash
              program_flash(FW_BASE+writeCounter*FLASH_PAGESIZE, data, FLASH_PAGESIZE);
              writeCounter ++;
              memset(data,'\0',FLASH_PAGESIZE);//clearing the buffer
              counter=0; //resetting the counter
          }
      }
       //sending an ok message
      uart_write(UART1, okMessage);
      /*getting the frame size of the next frame*/
      rcv = uart_read(UART1, BLOCKING, &read);
      packet_size = ((uint32_t)rcv)<<8;
      rcv = uart_read(UART1, BLOCKING, &read);
      packet_size |= (uint32_t)rcv;
      if(packet_size==0)
      {
            program_flash(FW_BASE+writeCounter*FLASH_PAGESIZE, data, FLASH_PAGESIZE);
      }
  }
}
/*
 * Program a stream of bytes to the flash.
 * This function takes the starting address of a 1KB page, a pointer to the
 * data to write, and the number of byets to write.
 *
 * This functions performs an erase of the specified flash page before writing
 * the data.
 */
long program_flash(uint32_t page_addr, unsigned char *data, unsigned int data_len)
{
  unsigned int padded_data_len;
  // Erase next FLASH page
  FlashErase(page_addr);
  // Clear potentially unused bytes in last word
  if (data_len % FLASH_WRITESIZE){
    // Get number unused
    int rem = data_len % FLASH_WRITESIZE;
    int i;
    // Set to 0
    for (i = 0; i < rem; i++){
      data[data_len-1-i] = 0x00;
    }
    // Pad to 4-byte word
    padded_data_len = data_len+(FLASH_WRITESIZE-rem);
  } else {
    padded_data_len = data_len;
  }
  // Write full buffer of 4-byte words
  return FlashProgram((unsigned long *)data, page_addr, padded_data_len);
}
void boot_firmware(void)
{
  uint16_t fw_size = *fw_size_address;
  if (fw_size == 0) {
    // No firmware installed. Return to main
    return;
  }
  // TODO: Print release message
  char *release=FW_BASE+*fw_size_address;
  uart_write_str(UART1,*release);
  // TODO: Boot the firmware
}