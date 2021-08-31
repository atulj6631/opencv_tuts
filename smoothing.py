# smooting is done to remove/reduce noise, 

import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


img = cv.imread('pictures/cat_large.jpg')
# cv.imshow('cat', img)

resized = rescaleFrame(img, scale=0.3)
cv.imshow('resize', resized)

''' averaging -> for a 3x3 kernel the center pixel will be the average of all other pixels surrounding it 
this is computed for all pixels in the image'''

average = cv.blur(src=resized, ksize=(3,3))
cv.imshow('Average Blur', average)


''' Gaussian Blur -> similar execution as averaging, except each
 surrounding pixel is given a weighted value, then the products of the average of the weights is given to the center
 it is less blurred as compared to averaging but it is more natural'''

gauss = cv.GaussianBlur(src=resized, ksize=(3,3), sigmaX=0)
cv.imshow('Gauss', gauss)


''' Median Blur -> same as averaging, but the center pixel is given the median value
better reduction in noise (salt and pepper noise)
'''

median = cv.medianBlur(src=resized, ksize=3)
cv.imshow('median', median)


''' Bi-Lateral blurring -> most effective '''
bilateral = cv.bilateralFilter(src=resized, d=10, sigmaColor=35, sigmaSpace=25) 
# sigmaColor specifies how many surrounding colors will influence the pixel computatuion
# sigmaspace defines from how much pixel distance the surrounding pixels will influence the main pixel computation
cv.imshow('bilateral', bilateral)

cv.waitKey(0)