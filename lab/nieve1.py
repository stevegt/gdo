#!/usr/bin/python

import random
import sys

bits = 16

def rotr(x, size):
	'''bitwise rotate right'''
	x = (x >> 1) | ((x << size-1) & 2**size-1)
	return x

def rhash(seed, src):
	random.seed(seed)
	T = [ random.randrange(2**bits) for i in range(256) ]
	h = seed
	for byte in src:
		h = rotr(h,bits) ^ T[ord(byte)];
		yield h

def src_stdin():
	while True:
		c = sys.stdin.read(1)
		if not len(c):
			break
		yield c
	
def main():
	src = src_stdin()
	hashes = rhash(422, src)
	for h in hashes:
		# print "%x" % h
		print h

main()
