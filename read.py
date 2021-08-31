import cv2 as cv

# reading images

# img = cv.imread('pictures/cat_large.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0)

# reading videos

capture = cv.VideoCapture('videos/cat_video.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF==ord('d'): # if the button "d" is pressed
        break
capture.release()
cv.destroyAllWindows()


