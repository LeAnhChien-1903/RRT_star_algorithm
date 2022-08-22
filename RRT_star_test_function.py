import cv2

image = cv2.imread("1.png")

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Image', grayImage)
cv2.waitKey()