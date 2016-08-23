#!/usr/bin/python

import cv2
import numpy as np
import os
import random
import sys 

image_size = 800

def save(image):
	rows,cols,depth = image.shape
	cv2.imwrite('/tmp/bitmap.png', image)

def show(image):
	save(image)
	os.system('xzgv -z /tmp/bitmap.png')


raw = [ random.randrange(2**10, 2**16) for i in range(image_size * image_size) ]
img = np.array(raw)
print img
img = img.reshape(image_size, image_size)

show(img)

