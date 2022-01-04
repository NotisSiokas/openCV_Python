import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")



width,height = 460,450
pts1 = np.float32([[225,90],[430,140],[164,380],[367,428]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output", imgOutput)


cv2.waitKey(0)

#pts1 = np.float32([[346,150],[192,287],[282,439],[496,485]])
