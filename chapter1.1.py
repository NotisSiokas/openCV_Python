import cv2

img = cv2.imread("Resources/obi.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)