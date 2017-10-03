#!/usr/bin/python
import numpy as np
import time
import matplotlib.pyplot as plt

def gen_neighbours(img, x, y):
	
	width = img.shape[0]-1
	height = img.shape[1]-1	

	coordinates = []
	for i in [x-1, x, x+1]:
		for j in [y-1, y, y+1]:
			if( (i < 0) or (i >= width) or (j < 0) or (j >= height) or (i == x and j == y)):
				continue
			else:
				coordinates.append((i,j))
		
	return coordinates
			
def neighbours_elevated(neighbours, img, threshold):
	for i in neighbours:
		if(img[i] > threshold/2.0):	
			return 1
	return 0

def filter_out_neighbours(img, neighbours):
	for i in neighbours:
		img[i] = 0.0
	return img
	
#Basic Algorithm O(n^2)
def basic(img, threshold=50):

	width = img.shape[0]-1
	height = img.shape[1]-1

	for x in range(0, width):
		for y in range(0, height):
			if(img[x,y] > (threshold) ):
				neighbours = gen_neighbours(img, x, y)
				if(neighbours_elevated(neighbours, img, threshold)):
					img = filter_out_neighbours(img, neighbours)
			
	return img

# Testing
def unit_test():
	test_img = np.load("test_img.npy")
	filtered_image = basic(test_img)

	
	return

unit_test()
