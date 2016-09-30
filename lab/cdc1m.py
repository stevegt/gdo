#!/usr/bin/python

import hashlib
import mmap
import numpy
import os
import sys

'''
Content Defined Chunking library
reference implementation of CDC1 algorithm in pure python

This code is a pythonic reimplementation of cdc1.py, using mmap for
file I/O.

This will produce a list of chunk sizes on stdout:

	dd if=/dev/urandom bs=9k count=320 > /tmp/r1
	./cdc1m.py /tmp/r1

...which must exactly match the output of:

	./cdc1.py < /tmp/r1


'''

class CDC(object):

	def __init__(self, srcfh, seed, word_size):
		''' 
		srcfh must be an open filehandle on an mmap()able file, e.g.:

		CDC(open("/tmp/foo", ...)

		'''
		self.seed = seed
		self.word_size = word_size
		# If word size is 16, then max chunk size is 64512; this allows a
		# chunk to fit into a UDP datagram. UDP over IP has 65507 usable
		# payload bytes available.  65507 - 64512 leaves us 995 bytes for
		# our own protocol header(s).
		self.max_chunk_size = 2**word_size - 1024
		self.avg_chunk_size = 2**(word_size-3)
		self.min_chunk_size = 2**(word_size-5)
		self.mask = self.avg_chunk_size - 1
		self.srcfh = srcfh
		self.srcfno = srcfh.fileno()
		self.chunk_start = None
		self.chunk_size = None
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

	def chunks(self):
		file_size = os.fstat(self.srcfno).st_size
		self.chunk_start = 0
		pagesize = mmap.PAGESIZE
		while True:
			# create new mmap frame for every chunk search
			mmap_offset = int(self.chunk_start / pagesize) * pagesize
			frame_offset = self.chunk_start - mmap_offset
			mmap_size = min(
					self.max_chunk_size+frame_offset, 
					file_size-mmap_offset)
			if self.chunk_start == file_size or mmap_size == 0:
				# eof
				break
			frame = mmap.mmap(self.srcfno, 
						mmap_size,
						mmap.MAP_PRIVATE, 
						mmap.PROT_READ,
						offset=mmap_offset)
			# search for next chunk
			h = self.seed
			self.chunk_size = 0
			# iterate until delimiter found or end of frame; 
			# end of frame == max_chunk_size
			for byte in frame[frame_offset:]:
				self.chunk_size += 1
				if self.chunk_size < self.min_chunk_size - 256:
					continue
				# rolling hash based on buzhash
				# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
				h = self.rotr(h) ^ self.T[ord(byte)];
				if self.chunk_size < self.min_chunk_size:
					continue
				if (h & self.mask) == 0:
					# found a delimiter
					break
			# we only get here if we found a delimiter, hit
			# max_chunk_size, or hit eof
			h = hashlib.sha256(
					frame[frame_offset:frame_offset+self.chunk_size])
			yield self.chunk_size, h.hexdigest()
			self.chunk_start += self.chunk_size

def print_chunk_sizes():
	cdc = CDC(open(sys.argv[1], 'r'), 1027, 16)
	for size,hexdigest in cdc.chunks():
		print size

def print_chunk_specs():
	cdc = CDC(open(sys.argv[1], 'r'), 1027, 16)
	for size,hexdigest in cdc.chunks():
		print "%6d %s" % (size, hexdigest)

if __name__ == '__main__':
	# print_chunk_sizes()
	print_chunk_specs()
