import cv2
import numpy as np

image = cv2.imread("test.png", 1)
img = cv2.resize(image, (460, 460))

kernel = np.array([1/16, 1/8, 1/16, 1/8, 1/4, 1/8, 1/16, 1/8, 1/16])
kernel2 = np.array([1/10, 1/10, 1/10, 1/10, 1/5, 1/10, 1/10, 1/10, 1/10])
kernel3 = np.array([1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9])

output = cv2.filter2D(img, -1, kernel)
output2 = cv2.filter2D(img, -1, kernel2)
output3 = cv2.filter2D(img, -1, kernel3)

#cv2.imshow('original', img)
cv2.imshow('a', output)
cv2.imshow('b', output2)
cv2.imshow('c', output3)
cv2.waitKey(0)