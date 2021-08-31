# gradients and edge detection are mathematically different concepts but application wise it is similar

import cv2 as cv
import numpy as np

img = cv.imread('pictures/kerala_2.webp')
cv.imshow('pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

''' Laplacian '''
lap = cv.Laplacian(src=gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap)) # since gradents can be negative (positive and negative slopes), the negative values are removed by giving absolute and the converted to uint8
cv.imshow('Laplace', lap)

''' Sobel '''
sobelx = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(src=gray, ddepth=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Combined sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('canny edge', canny)

cv.waitKey(0)