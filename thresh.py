# binarizing an image and thresholding

import cv2 as cv

img = cv.imread('pictures/cat.jpg')
cv.imshow('cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)


''' simple thresholding '''
threshold, thresh = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY)
# thresh variable holds the image
# threshold holds the threshold value in this case '150'
cv.imshow('Simple Threshold', thresh)

threshold, thresh_inv = cv.threshold(src=gray, thresh=150, maxval=255, type=cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

''' Adaptive Threshold '''
# the computer will iself find the threshold valuee to binarize
adaptive_thresh = cv.adaptiveThreshold(src=gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY, blockSize=15, C=6)
'''
adaptiveMethode -> in this case it is mean value, so it taes the mean value of the near by block
blocksize -> kernel size
C -> an integer value u can subtract from the mean value inorder to fine tune the threshold
'''
cv.imshow('adaptive thresholding', adaptive_thresh)


cv. waitKey(0)