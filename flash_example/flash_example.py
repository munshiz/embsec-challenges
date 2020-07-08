# Flash example
# 
# 
# This lesson provides a peripheral programming example that accompanies the
# Flash example from the datasheet lecture. 
# ### Challenge Name: flash_example (/embsec/flash_example/flash_example)
# 
# 
# The code for writing and checking Flash memory can be found in `flash_example.c`.
# The code follows the process described in the lecture, using the register definitions
# and bit field definitions from the Stellaris library.
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def flash_example():
    subprocess.check_output([f'(cd flash_example && make CHALLENGE=flash_example)'], shell=True)
    resp0, resp1, resp2 = embsec.grade_emulated(f'./flash_example/gcc/main.bin', f'/embsec/flash_example/flash_example')
    stdout, stdin = resp2
    return (extract_flag(stdout))
    
flash_example()

