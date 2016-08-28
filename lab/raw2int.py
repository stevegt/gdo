#!/usr/bin/python

'''
convert input byte stream to 16-bit ascii integers, one per line

dd if=/dev/urandom bs=1k count=320 | ./raw2int.py | ./randtest.py

'''

import struct
import sys 

while True:
	txt = sys.stdin.read(2)
	if len(txt) < 2:
		break
	print struct.unpack('=H', txt)[0]

