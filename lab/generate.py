#!/usr/bin/python

import sys

pattern = map(int, sys.argv[1:])

while True:
	for i in pattern:
		sys.stdout.write(chr(i))


