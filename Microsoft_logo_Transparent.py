import cv2
import numpy as np

image = cv2.imread("Input\Microsoft_logo.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA).astype(np.float32)

image[(70<image[:, :, 0]) &(image[:, :, 0]<100) & (70<image[:, :, 1]) & 
      (image[:, :, 1]<100) & (70<image[:, :, 2]) & (image[:, :, 2]<100)] \
      *= (1, 1, 1, 0)

image = image.astype(np.uint8)

cv2.imwrite("Output\Microsoft_Transparent.png", image)
cv2.imshow("Microsoft logo Transparent",image)
cv2.waitKey()
