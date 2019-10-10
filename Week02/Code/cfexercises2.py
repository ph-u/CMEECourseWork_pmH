#!/bin/env python3

# Author: PokMan Ho pok.ho19@imperial.ac.uk
# Script: cfexercises2.py
# Desc: loop testing with different "hello" versions
# Input: python3 cfexercises2.py
# Output: 22-lined hellos
# Arguments: 0
# Date: Oct 2019

for j in range(12):
	if j % 3 == 0:
		print(j,'j0_hello')

for j in range(15):
	if j % 5 == 3:
		print(j,'j1_hello')
	elif j % 4 == 3:
		print(j,'j2_hello')

z=0
while z != 15:
	print(z,'z1_hello')
	z=z+3

z=12
while z<100:
	if z==31:
		for k in range(7):
			print(k,'zk_hello')
	elif z==18:
		print(z,'z2_hello')
	z=z+1