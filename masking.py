import cv2 as cv
import numpy as np

img = cv.imread('pictures/cat.jpg')
cv.imshow('cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
cv.imshow('mask', mask)


masked = cv.bitwise_and(src1=img, src2=img, mask=mask)
cv.imshow('masked image', masked)


cv.waitKey(0)