# Review c
# 
# In this lesson you will review some of the topics of the C language you
# learned in the Hardware Module earlier this year. By understanding these 
# topics, you will be prepared to complete your design implementations, and
# become solid C programmers! If you get stuck during these challenges,
# checkout the C language documentation and the Hardware Module, as well as
# review the C lecture.
# 
# For the first challenges, you should work with a partner. This will get you used
# to pair programming remotely, which will be necessary during the hardware challenge.
# You and a partner will be modifying the *int_to_bin.c* and *anagram.c* files to
# complete challenges 1 and 2.
# 
# Challenges 3 and 4 are to be completed individually, they serve as practice for reading
# and understanding C code. You will just be adding comments to the Jupyter Notebook.
# Remember to push your notebook at the end of the day so we can read your answers!
# 
# Good luck!### Challenge Name: int_to_bin (/embsec/review_c/int_to_bin)
# 
# 
# You are building a device that can convert an input from a number pad
# [0-9] and convert it into a binary string of ASCII ones and zeros. You
# and your partners task is to construct a function that consumes an uint8_t
# and writes the binary representation to a buffer. The output should include
# any leading zeros. Here are a few examples:
# 
#     0    ->   "00000000"
# 
#     5    ->   "00000101"
# 
#     14   ->   "00001110"
# 
#     255  ->   "01111111"
# 
# Helpful resources:
# 
# <https://en.wikipedia.org/wiki/C_data_types#Fixed-width_integer_types>
# 
# <http://www.asciitable.com/>
# 
# 
# 
import embsec
import subprocess
from core.util import extract_flag

def int_to_bin():
    subprocess.check_output([f'gcc -I../../lib/uart int_to_bin.c ../../lib/uart/uart_linux.c -o int_to_bin'], shell=True)
    stdout, stdin = embsec.grade_c(f'./int_to_bin', f'/embsec/review_c/int_to_bin')
    
    return (extract_flag(stdout))
    
int_to_bin()

### Challenge Name: anagram (/embsec/review_c/anagram)
# 
# 
# In this challenge, you are building a device that can solve various puzzles.
# For this specific task, you will be completing a functionality that checks if two
# words are anagrams. You and a partner must create a function that allows for this
# feature. The function will consume two C strings and return 1 if the strings are
# anagrams of eachother. Otherwise, it should return 0. 
# 
# A word is considered an anagram if the letters can be scrambled into another word
# with no letters left over. 
# 
#     isAnagram("hamlet", "amleth") -> 1
#     
#     isAnagram("oh lame saint", "the mona lisa") -> 1
# 
#     isAnagram("dormitory", "dirty room") -> 1
# 
#     isAnagram("panama", "panam") -> 0
# 
#     isAnagram("embedded", "security") -> 0
# 
# You can assume that the inputs will only contain characters [a-z] and " ", 
# but only " " can be repeated or removed without violating the anagram rule.
# 
import embsec
import subprocess
from core.util import extract_flag

def anagram():
    subprocess.check_output([f'gcc -I../../lib/uart anagram.c ../../lib/uart/uart_linux.c -o anagram'], shell=True)
    stdout, stdin = embsec.grade_c(f'./anagram', f'/embsec/review_c/anagram')
    

anagram()### Challenge Name: annotate_1 (/embsec/review_c/annotate_1)
# 
# 
# In this challenge you will simply analyze the following snippit of code.
# First, add annotations to each line with a '//' describing breifly what that
# line will do. Also, identify what the values of the variables on line 8 might
# be when it runs. Finally, draw a memory map of the program that keeps track of
# global and local variables and where they are stored. 
# 
# 
#include <stdio.h>

final int MAX_VALUE = 90;                           //

void updateValue (int* value_ptr, int modifier) {   //
    int newVal = modifier*(*value_ptr);             //
    *value_ptr = newVal;                            //

    if (*value_ptr > MAX_VALUE) {                   //
        printf("You win!\n%p\n%d", value_ptr, *value_ptr); //What will this line output?
    }
}

int main() \{
    int score = 1;                              //
    
    for (int i = 1; i <= 5; i++) {              //
        updateValue(&score, i);                 //
    }
}
### Challenge Name: annotate_2 (/embsec/review_c/annotate_2)
# 
# 
# This challenge is very similar to the previous challenge, but is conceptually harder.
# It is good practice for getting familiar with pointers and other memory related quirks
# of the C language.
# 
# 
#include <stdio.h>  //

int foo (int e) {   //
    int i = 2;      //
    int* i_p = &i;  //

    return 2*(*i_p) + 2*i + e/i; // Draw a memory map of the program here
}

int bar (int* c, int* d) {
    printf("%p", c);  // What will the output of this be?

    if (*c > 7) {           //
        return foo(*d);     //
    }
    else {
        return (*d + 1);    //
    }
}

int main() {
    int a;                  //
    int b = 0;              //
    int cnt = 0;            //

    for (a = 10; (a + b) < 16; a-=1) {   //
        b = bar(&a, &b);                 //
        cnt++;                           //
    }
    printf("%d", cnt);    // What will the output of this be?

    return 0;
}
