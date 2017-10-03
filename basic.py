#!/usr/bin/python
import numpy as np
import time

test_img = np.load("test_img.npy")

#Supporting Functions
def gen_neighbours(img, x, y):
	
	width = img.shape[0]-1
	height = img.shape[1]-1	

	#coordinates to examine
	coordinates = []
	for i in [x-1, x, x+1]:
		for j in [y-1, y, y+1]:
			if( (i < 0) or (i >= width) or (j < 0) or (j >= height) or (i == x and j == y)):
				continue
			else:
				coordinates.append((i,j))
		
	return coordinates
				

#Basic Algorithm O(n^2)
def basic(img, threshold=50):

	width = img.shape[0]-1
	height = img.shape[1]-1

	for x in range(0, width):
		for y in range(0, height):
			if(img[x,y] > (threshold/2.0) ):
				neighbours = gen_neighbours(img, x, y)
				print neighbours
				#if(neighbours_elevated(neighbours)):
				#	filter_out_neighbours(img, x, y)
			


basic(test_img)
