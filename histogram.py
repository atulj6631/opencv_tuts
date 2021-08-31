import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('pictures/cat.jpg')
cv.imshow('cats', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

# for gray scale images

# mask = cv.bitwise_and(src1=gray, src2=gray, mask=circle)
# cv.imshow('masked image', mask)


# ''' grayscale histogram '''
# gray_hist = cv.calcHist(images=[gray], channels=[0], mask=mask, histSize=[256], ranges=[0,256] )

# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of bins')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', mask)

plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of bins')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()



cv.waitKey(0)