import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('blank', blank)

# img = cv.imread('pictures/cat.jpg')
# cv.imshow('cat', img)

''' painting it a particular colour '''
# blank[:] = 1,43,98
# cv.imshow('green', blank)
# blank[200:300, 300:400] = 0,0,255

''' draw the rectangle '''
# cv.rectangle(blank, pt1=(10,10), pt2=(blank.shape[1]//2, blank.shape[0]//2), color=(0,255,31), thickness=2) # thickness=-1 full body is painted
# cv.imshow('rectangle', blank)

''' draw a circle '''
# cv.circle(blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(45,56,12), thickness=4)
# cv.imshow('circle', blank)

''' draw line '''
# cv.line(blank, pt1=(30,30), pt2=(450,490), color=(30,254,192), thickness=24)
# cv.imshow('line', blank)

''' write text '''
cv.putText(blank, text='hello', org=(250, 300), color=(90,12,45), fontFace=cv.FONT_HERSHEY_COMPLEX, fontScale=2.0, thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)