#!/usr/bin/python

'''
Generate a continuous stream of a given pattern of characters 

Example:
	./generate.py 0            # all zeros
	./generate.py 255          # all ones
	./generate.py 65 53 53 65  # A55A (alternating bits)

'''

import sys

pattern = map(int, sys.argv[1:])

while True:
	for i in pattern:
		sys.stdout.write(chr(i))


