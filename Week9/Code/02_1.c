/* 
Author: PokMan Ho pok.ho19@imperial.ac.uk
Script: 02_1.c
Desc: print terminal message (Ex.1,2)
Input: clang 02_1.c -o 02_1;./02_1
Output: terminal output
Arguments: 2
Date: Dec 2019
*/

#include <stdio.h>

int main (void){
	printf("declare var -- all missing variable type declaration\n");
	printf("declare var -- y=5, missing \";\"\n");
	printf("print var -- value of x: i, missing \"%%\"\n");
	printf("print declared var -- value of z: %%f instead of i\n");
	printf("Return 0 to the OS -- missing \"/*\"\n");
}
