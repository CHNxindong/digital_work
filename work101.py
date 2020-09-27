# from PIL import ImageOps
# import cv2
#
# im = cv2.imread('glass.jpg')
# # cv2.imshow('im1', im)
# # cv2.waitKey(0)
#
# eq = ImageOps.equalize(im)
# cv2.imshow('image2', eq)
# cv2.waitKey(0)
# cv2.imwrite('work1/glass_1.jpg', eq)



import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('glass.jpg', 0)
cv2.imshow('img1', img)

equ = cv2.equalizeHist(img)
# res = np.hstack((img, equ))
# #stacking images side-by-side
# cv2.imshow('img', res)
cv2.imshow('img', equ)
cv2.waitKey()
cv2.destroyAllWindows()
