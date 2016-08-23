#!/usr/bin/python

import Image
import numpy as np
import os
import struct
import sys 

fn = "/tmp/image.png"

def save(image):
	img = Image.fromarray(image)
	img.save(fn)

def show(image):
	save(image)
	os.system('xzgv -z %s' % fn)

def main():
	lst = read()
	img = lst2img(lst)
	buf = lst2buf(lst)
	ent(buf)
	show(img)

def read():
	# accepts one integer per line
	lst = []
	for line in sys.stdin.readlines():
		lst.append(int(line))
	# truncate the end to make it a square root
	sqrt = int(len(lst)**.5)
	sqr = sqrt**2
	print 'truncating', len(lst) - sqr, 'bytes'
	lst = lst[:sqr]
	return lst

def lst2img(lst):
	image_size = int(len(lst)**.5)
	assert image_size == len(lst)**.5
	img = np.array(lst)
	img = img.reshape((image_size, image_size))
	return img

def lst2buf(lst):
	lst = lst[:]
	buf = ''
	while len(lst):
		v = lst.pop(0)
		try:
			packed = struct.pack('=H', v)
		except:
			print repr(v)
			raise
		buf += packed
	return buf

def ent(buf):
	'''
	Depends on John Walker's entropy testing package 'ent':
	http://www.fourmilab.ch/random/
	'''
	entin = os.popen('random/ent -t', 'w')
	entin.write(buf)
	entin.close()

main()
