#!/usr/bin/python

'''
compare different RNG outputs given the same seed
'''


import random
import numpy
import sys

seed = int(sys.argv[1])
random.seed(seed)
numpy.random.seed(seed)

while True:
	a = random.randrange(2**16)
	b = numpy.random.randint(2**16)
	assert a == b, (a, b)


