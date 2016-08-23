#!/usr/bin/python

import Image
import numpy as np
import os
import random
import struct
# import sys 

image_size = 400
fn = "/tmp/image.png"

def save(image):
	img = Image.fromarray(image)
	img.save(fn)

def show(image):
	save(image)
	os.system('xzgv -z %s' % fn)

def main():
	lst = generate()
	img = lst2img(lst)
	buf = lst2buf(lst)
	ent(buf)
	show(img)

def generate():
	lst = []
	for i in range(image_size**2):
		# v = i % 2**16  # not random
		# v = random.randrange(0, 2**8-1)  # not very random
		v = struct.unpack('=H', os.urandom(2))[0]  # very random
		# v = random.randint(2**10, 2**16-1)  # random enough
		# v = random.randint(2**14, 2**16-1) # too light
		# v = random.randrange(0, 2**16-1) 
		lst.append(v)
	return lst

def lst2img(lst):
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
	entin = os.popen('random/ent -t', 'w')
	entin.write(buf)
	entin.close()

main()
