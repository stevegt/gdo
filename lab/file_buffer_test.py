#!/usr/bin/python

'''
file buffering performance test
'''

import sys
import timeit

fn = sys.argv[1]

print "prime fs page cache...",
open(fn,'r').read()
print "done"

def readall(fn, size):
	fh = open(fn, 'r')
	while True:
		x = fh.read(size)
		if len(x) == 0:
			break
	fh.close()

for size in (1,4096,65536):
	print "read %d bytes at a time..." % size
	t = timeit.Timer('readall("%s", %d)' % (fn, size), 
						setup="from __main__ import readall")
	s = t.timeit(10)
	print "%9.5f seconds" % s

