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
			
def neighbour_elevated(neighbour, img, threshold):
	if(img[neighbour] > threshold/4.0):	
		return 1
	return 0

def filter_out_neighbour(img, neighbour):
	img[neighbour] = 0.0
	return img
	
#Basic Algorithm O(n^2)
def basic(img, threshold=50):

	width = img.shape[0]-1
	height = img.shape[1]-1

	for x in range(0, width):
		for y in range(0, height):
			if(img[x,y] > (threshold) ):
				neighbours = gen_neighbours(img, x, y)
				for i in neighbours:
					if(neighbour_elevated(i, img, threshold)):
						img = filter_out_neighbour(img, i)
			
	return img

# Testing
# Easy way to demo is to change the scaling in neighbour elevated
def unit_test():
	test_img = np.load("test_img.npy")
	filtered_image = basic(test_img)

	x = 50
	y = 100
	q = 50

	plt.figure(1)
	plt.subplot(211)
	plt.title("Test Img")
	plt.xlim(x, x+q)
	plt.ylim(y, y+q)
	plt.imshow(test_img, interpolation="none", cmap='Greys_r', vmin=0)
	plt.colorbar()
	
	plt.subplot(212)
	plt.title("Filtered Image")
	plt.xlim(x, x+q)
	plt.ylim(y, y+q)
	plt.imshow(filtered_image, interpolation="none", cmap='Greys_r', vmin= 0)
	plt.colorbar()
	plt.show()
	
	return

unit_test()
