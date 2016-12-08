#!/usr/bin/python

'''
Content Defined Hashing library
- reference implementation of CDH1 algorithm in pure python
- we only do strong hashing here; call cdc library to do chunking

This will produce a list of hashes on stdout:

	dd if=/dev/urandom bs=10k count=320 | ./cdh1.py 

'''

import hashlib
import numpy
import sys

import cdc1p 

# CDC = cdc1p.CDC

class CDC(object):

def hash_stream(srcfh, seed, word_size):
	assert seed != 0
	numpy.random.seed(seed)
	# streamhash = hashlib.sha256()
	cdc = CDC(lambda: srcfh.read(4096), seed, word_size)
	totalsize = 0
	while True:
		size = cdc.get_chunk()
		if size == 0:
			break
		totalsize += size
		# streamhash.update(cdc.chunk)
		chunkhash = hashlib.sha256(cdc.chunk)
		yield size,"sha256:%s" % chunkhash.hexdigest()
	# yield None,None
	# yield totalsize,streamhash.hexdigest()

def print_hashes():
	hashes = hash_stream(sys.stdin, 1027, 16)
	for size,h in hashes:
		if size is None:
			print '==='
			continue
		print "%6d %s" % (size, h)

'''
class CDH(object):

	def __init__(self, srcfh, seed, word_size):
		self.seed = seed
		self.word_size = word_size
		self.src = srcfh
		assert seed != 0
		numpy.random.seed(seed)
		self.streamhash = hashlib.sha256()
		self.chunkhash = None
		self.chunk = None

	def hash_stream(self):
		cdc = CDC(lambda: sys.stdin.read(4096), self.seed, self.word_size)
		while True:
			size = cdc.get_chunk()
			if size == 0:
				break
			self.streamhash.update(cdc.chunk)
			self.chunkhash = hashlib.sha256(cdc.chunk)
			yield self.chunkhash.hexdigest()
		yield self.streamhash.hexdigest()
			
def print_hashes():
	cdc = CDC(lambda: sys.stdin.read(1), 1027, 16)
	while True:
		size = cdc.get_chunk()
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		print "%6d %s" % (size, h.hexdigest())

def print_hashes():
	cdh = CDH(sys.stdin, 1027, 16)
	cdh
	cdc1_init(cdc, lambda: sys.stdin.read(1))
	while True:
		size = cdc1_get_chunk(cdc)
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		print "%6d %s" % (size, h.hexdigest())

def cdc1_get_chunk(self):
	h = self.seed
	self.chunk = ''
	found = False
	while True:
		buf = self.src()
		if len(buf) == 0:
			break
		for byte in buf:
			self.chunk += byte
			csize = len(self.chunk) 
			if csize < self.min_chunk_size - 256:
				continue
			if csize == self.max_chunk_size:
				found = True
				break
			# rolling hash based on buzhash
			# http://www.dcs.gla.ac.uk/~hamer/cakes-talk.pdf
			h = cdc1_rotr(self, h) ^ self.T[ord(byte)];
			if csize < self.min_chunk_size:
				continue
			if (h & self.mask) == 0:
				found = True
				break
		if found:
			break
	return len(self.chunk)

'''

if __name__ == '__main__':
	print_hashes()

