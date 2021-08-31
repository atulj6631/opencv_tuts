# Colour Spaces

import cv2 as cv

img = cv.imread('pictures/kerala_2.webp')
cv.imshow('kerala', img)

''' BGR to Grayscale '''
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

''' BGR to HSV '''
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

''' BGR to L*a*b '''
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)


cv.waitKey(0)
