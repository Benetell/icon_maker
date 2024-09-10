import cv2 as cv
import numpy as np

# 16, 24, 32, 48,64 --- 16 szín
# felbontás és bitmélység változtatás

# - beolvasás
img = cv.imread('.\images\Screenshot_3.png', cv.IMREAD_ANYCOLOR)


def rescale(frame, size, interpolation):
    dimensions = (size, size)

    return cv.resize(frame, dimensions, interpolation=interpolation)

cv.imshow("jolesz.jpg", img)

#img = np.uint(img) * 256
#cv.imshow("lofz", img)

img_processed1 = rescale(img, 32, cv.INTER_NEAREST)
#img_processed2 = rescale(img_processed1, 16, cv.INTER_NEAREST)

cv.imwrite("jolesz2.jpg", img_processed1)
cv.waitKey(0)
