#!/usr/bin/python

import hashlib
import numpy
import sys

'''
Content Defined Chunking library
reference implementation of CDC1 algorithm in pure python

This code is a pythonic reimplementation of cdc1.py.

This will produce a list of block sizes on stdout:

	dd if=/dev/urandom bs=9k count=320 > /tmp/r1
	./cdc1p.py < /tmp/r1

...which must exactly match the output of:

	./cdc1.py < /tmp/r1


'''

class CDC(object):

	def __init__(self, srcfh, seed, word_size):
		''' 
		srcfh must be a callable with no args, and must return 1 
		byte, or the empty string on EOF, e.g.:

		CDC(lambda: sys.stdin.read(1), ...)

		'''
		self.seed = seed
		self.word_size = word_size
		self.max_chunk_size = 2**word_size - 1
		self.avg_chunk_size = 2**(word_size-3)
		self.min_chunk_size = 2**(word_size-5)
		self.mask = self.avg_chunk_size - 1
		self.src = srcfh
		self.chunk = ''
		assert seed != 0
		assert seed <= self.max_chunk_size
		numpy.random.seed(seed)
		# T is a 256 byte array filled with random integers
		# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
		self.T = [ numpy.random.randint(2**word_size) for i in range(256) ]

	def rotr(self, x):
		'''bitwise rotate right'''
		x = (x >> 1) | ((x << self.word_size-1) & 2**self.word_size-1)
		return x

	def get_chunk(self):
		h = self.seed
		self.chunk = ''
		found = False
		while True:
			buf = self.src()
			if len(buf) == 0:
				break
			for byte in buf:
				assert len(byte) == 1
				self.chunk += byte
				csize = len(self.chunk) 
				if csize < self.min_chunk_size - 256:
					continue
				if csize == self.max_chunk_size:
					found = True
					break
				# rolling hash based on buzhash
				# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
				h = self.rotr(h) ^ self.T[ord(byte)];
				if csize < self.min_chunk_size:
					continue
				if (h & self.mask) == 0:
					found = True
					break
			if found:
				break
		return len(self.chunk)

def print_chunk_sizes():
	cdc = CDC(lambda: sys.stdin.read(1), 1027, 16)
	while True:
		size = cdc.get_chunk()
		if size == 0:
			break
		print size

def print_chunk_specs():
	cdc = CDC(lambda: sys.stdin.read(1), 1027, 16)
	while True:
		size = cdc.get_chunk()
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		print "%6d %s" % (size, h.hexdigest())

if __name__ == '__main__':
	print_chunk_sizes()
	# print_chunk_specs()