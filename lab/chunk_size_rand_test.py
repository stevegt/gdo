#!/usr/bin/python

import cdc1m
import sys

def run_test(mode, fn, word_size):
	cdc = cdc1m.CDC(open(fn, 'r'), 1027, word_size)
	for size,hexdigest in cdc.chunks():
		if mode == 'size':
			print size
		if mode == 'hash':
			print hexdigest

run_test(sys.argv[1], sys.argv[2], int(sys.argv[3]))



