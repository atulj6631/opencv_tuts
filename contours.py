# Contours are the boundaries of a particular object
# Contours are not as same as edges. Contours are useful of object detecion, facial recognition etc

import cv2 as cv
import numpy as np


img = cv.imread('pictures/kerala_2.webp')
cv.imshow('cats', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges',canny)


''' Thresholding '''
ret, thresh = cv.threshold(src=gray, thresh=125, maxval=255, type=cv.THRESH_BINARY)
# cv.imshow('threshold', thresh)

# find contours method
contours, hierarchies = cv.findContours(image=canny, mode=cv.RETR_LIST, method=cv.CHAIN_APPROX_SIMPLE)
print('contours', len(contours))

cv.drawContours(image=blank, contours=contours, contourIdx=-1, color=(171,150,136), thickness=1) # contouridx is used to index out the contours
cv.imshow('contours', blank)


cv.waitKey(0)