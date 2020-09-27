# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 9:11
# @Author  : dong xin
# @File    : work101.py
# @Software: PyCharm

# subject : equalizeHist for gray image.
import cv2
import numpy as np

# 0 means gray
img = cv2.imread('input/5.png', 0)

# process for equalizeHist
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('equalizeHist', res)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('output/5.png', res)
