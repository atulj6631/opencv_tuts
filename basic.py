import cv2 as cv

img = cv.imread('pictures/cat.jpg')
cv.imshow('cat', img)

''' converting to gray scale '''
# gray = cv.cvtColor(src=img, code=cv.COLOR_BGR2GRAY )
# cv.imshow('Gray', gray)

''' Blur the image '''
# blur = cv.GaussianBlur(src=img, ksize=(7,7), sigmaX=cv.BORDER_DEFAULT)
# cv.imshow('Blur' ,blur)

''' Edge cascade '''
# canny = cv.Canny(image=img, threshold1=int(125), threshold2=int(175))
# cv.imshow('canny', canny)

''' dilated '''
# dilated = cv.dilate(src=canny, kernel=(3,3), iterations=7)
# cv.imshow('dilated', dilated)


''' Eroding '''
# eroded = cv.erode(src=dilated, kernel=(3,3), iterations=1)
# cv.imshow('eroded', eroded)

''' Resize '''
resized = cv.resize(src=img, dsize=(500,500), interpolation=cv.INTER_AREA)  # cv.INTER_AREA is used when decreasing the size, and cv.INTER_LINEAR is used whe enlarging
cv.imshow('resize', resized)  # cv.INTER_CUBIC gives the best quality but is computationally expensive

''' Cropping '''
cropped = img[50:200, 100:350]
cv.imshow('cropping', cropped)

cv.waitKey(0)
