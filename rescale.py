import cv2 as cv

img = cv.imread('pictures/cat_large.jpg')
# cv.imshow('cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# rescaled_img = rescaleFrame(img, scale=0.2)
# cv.imshow('cat', rescaled_img)

# def changeRes(width, height):
#     # will only work on live video
#     capture.set(3, width)
#     capture.set(4, height)

cv.waitKey(0)