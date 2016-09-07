#!/usr/bin/python

'''
stdin buffering performance test

./stdin_buffer_test.py     1 < /tmp/random.data
./stdin_buffer_test.py  4096 < /tmp/random.data
./stdin_buffer_test.py 65536 < /tmp/random.data

'''

import sys
import timeit

size = int(sys.argv[1])

def readall(size):
	while True:
		x = sys.stdin.read(size)
		if len(x) == 0:
			break

print "read %d bytes at a time..." % size
t = timeit.Timer('readall(%d)' % (size), 
					setup="from __main__ import readall")
s = t.timeit(1)
print "%9.5f seconds" % s

