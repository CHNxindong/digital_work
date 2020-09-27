# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 9:11
# @Author  : dong xin
# @File    : work102.py
# @Software: PyCharm

# subject : equalizeHist for rgb image and simply operate on rgb color space.
import cv2 as cv
import numpy as np

# -1 represents rgb
raw = cv.imread("input/10.png", -1)
# if the img is too big, we should resize it firstly
# x, y = raw.shape[0:2]
# raw = cv.resize(raw, (int(y / 5), int(x / 5)))

# split to 3 channels r g b
B, G, R = cv.split(raw)

# equalizeHist for r g b respectly
EB = cv.equalizeHist(B)
EG = cv.equalizeHist(G)
ER = cv.equalizeHist(R)
# when finish the operater then merge them into together
rgbhist = cv.merge((EB, EG, ER))

res = np.hstack((raw, rgbhist))
cv.imshow('equalizeHist', res)
cv.waitKey()
cv.destroyAllWindows()

cv.imwrite('output/10.png', res)
