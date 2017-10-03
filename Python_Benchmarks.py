"""
This file contains different implmentations and benchmarks of
neighbour algorithms for use in AST326-Lab1

Rules for benchmarks:

Each benchmark shall...
#1 Use the same image (1288x964)
#2 Take in an image and threshold as parameters
#3 Be run on the same computer
#4 Not be required to insure proper arguments

Each benchmark produce an image where any dually-elevated event is set to 0.

A dually-elevated event is as follows:

A pixel with ADU value greater than the given threshold with
a neighbouring pixel which is greater than half the given threshold.

All benchmarks will be evaluated over 100 trials of the same image.
"""

#imports
import numpy as np
import time
from multiprocessing.pool import ThreadPool
from multiprocessing.pool import Pool
from collections import deque

#Load Test Image (Already Dark Current Subtracted)
test_img = np.load("test_img.npy")

#Example Function ~0.32s (0.10 with Pool)
def ExampleFunction(img,threshold=50):
	X = img.shape[0]-1
	Y = img.shape[1]-1
	neighbours = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
				       for y2 in range(y-1, y+2)
				       if (-1 < x <= X and
					   -1 < y <= Y and
					   (x != x2 or y != y2) and
					   (0 <= x2 <= X) and
					   (0 <= y2 <= Y))]
	for i in range(X):
		for j in range(Y):
			if(img[i,j] > threshold): #elevated pizel found
				surrounding_elevated_pixles = [k for k in neighbours(i,j) if(img[k] > threshold/2)] #Check neighbours
				if(len(surrounding_elevated_pixles) != 0):#If there is a neighbouring elevated pixel
					for pix in surrounding_elevated_pixles:
						img[pix] = 0;
					img[i,j] = 0;
	return img

"""
N_Trials = 100
start = time.time()
for i in range(N_Trials):
	Function1(test_img)
diff = time.time()-start

print("Results for Benchmark 1: %f s; Time Per Image %f s" % (diff, diff/N_Trials))
#Pool(4).map(ExampleFunction,[test_img]*N_Trials) #How to use Pool
"""

def Function1(img,threshold=50):
	return

def Function2(img,threshold=50):
	return
 
# ~0.0050s, (~0.0017s with Pool)
def Function3(img,threshold=50):
	def CheckNeighbours(x,y):
		return np.count_nonzero(img[max(0,x-1):min(964,x+2),max(0,y-1):min(1288,y+2)] > threshold/2) < 2
	elevated_point = np.where(img > threshold)
	img[elevated_point] *= np.vectorize(CheckNeighbours)(elevated_point[0],elevated_point[1])
	return img

