import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape

img = cv.imread('pictures/kerala_2.webp')
cv.imshow('kerala', img)


''' translation '''
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
# +x --> Right
# +y --> Down

tranlated = translate(img, 100, 100)
# cv.imshow('translate', tranlated)

''' Rotation '''
def rotate(img, angle, rotPoint=None):
    width, height = img.shape[1], img.shape[0]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(center=rotPoint, angle=angle, scale=1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

# rotated = rotate(img, 45)
# cv.imshow('rotate', rotated)

''' Flip '''
flip = cv.flip(src=img, flipCode=1) #  1 for horizontal flip and 0 for vertical flip
cv.imshow('flip', flip)

cv.waitKey(0)