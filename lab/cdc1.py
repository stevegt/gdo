#!/usr/bin/python

import hashlib
import numpy
import sys

'''
Content Defined Chunking library
reference implementation of CDC1 algorithm in pure python

This code is purposely not very pythonic; the intent is to make it
easier to translate to C or other languages.

This will produce a list of block sizes on stdout:

	dd if=/dev/urandom bs=9k count=320 | ./cdc1.py 

'''

class CDC1(object):

	def __init__(self):
		# roughly translates to a C struct
		self.src = None
		self.seed = None
		self.word_size = None
		self.max_chunk_size = None
		self.avg_chunk_size = None
		self.min_chunk_size = None
		self.mask = None
		self.chunk = ''
		# T is a 256 byte array filled with random integers
		# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
		self.T = None

def cdc1_init(self, src, seed, word_size):
	''' 
	src must be a callable with no args, and must return 1 
	byte, or the empty string on EOF, e.g.:

	cdc1_init(self, lambda: sys.stdin.read(1))

	'''
	self.src = src
	self.seed = seed
	self.word_size = word_size
	self.max_chunk_size = 2**word_size - 1
	self.avg_chunk_size = 2**(word_size-3)
	self.min_chunk_size = 2**(word_size-5)
	self.mask = self.avg_chunk_size - 1
	assert seed != 0
	assert seed <= self.max_chunk_size
	numpy.random.seed(seed)
	# T is a 256 byte array filled with random integers
	# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
	self.T = [ numpy.random.randint(2**word_size) for i in range(256) ]

def cdc1_rotr(self, x):
	'''bitwise rotate right'''
	x = (x >> 1) | ((x << self.word_size-1) & 2**self.word_size-1)
	return x

def cdc1_get_chunk(self):
	h = self.seed
	self.chunk = ''
	while True:
		buf = self.src()
		if len(buf) == 0:
			break
		# XXX reference implementation, only processes one byte at a time
		assert len(buf) == 1
		byte = buf[0]
		self.chunk += byte
		csize = len(self.chunk) 
		if csize < self.min_chunk_size - 256:
			continue
		if csize == self.max_chunk_size:
			break
		# rolling hash based on buzhash
		# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
		h = cdc1_rotr(self, h) ^ self.T[ord(byte)];
		if csize < self.min_chunk_size:
			continue
		if (h & self.mask) == 0:
			break
	return len(self.chunk)

def print_chunk_sizes():
	cdc = CDC1()
	cdc1_init(cdc, lambda: sys.stdin.read(1), 1027, 16)
	while True:
		size = cdc1_get_chunk(cdc)
		if size == 0:
			break
		print size

def print_chunk_specs():
	cdc = CDC1()
	cdc1_init(cdc, lambda: sys.stdin.read(1), 1027, 16)
	while True:
		size = cdc1_get_chunk(cdc)
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		print "%6d %s" % (size, h.hexdigest())

if __name__ == '__main__':
	print_chunk_sizes()
	# print_chunk_specs()
