#!/usr/bin/python

import cdc1m
import timeit
import sys

# ./chunk_size_speed_test.py /tmp/random.data 
#
# see bits-vs-performance.gnumeric -- shows 16 bit as being best
# performance 

def speed_test(word_size):
	cdc = cdc1m.CDC(open(sys.argv[1], 'r'), 1027, word_size)
	for size,hexdigest in cdc.chunks():
		# print "%6d %s" % (size, hexdigest)
		pass

for i in range(10):
	for size in range(12,31):
		t = timeit.Timer('speed_test(%d)' % (size), 
							setup="from __main__ import speed_test")
		s = t.timeit(1)
		print size, s



