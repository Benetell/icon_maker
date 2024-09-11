

import cv2 as cv
import numpy as np

# Kép beolvasása
img = cv.imread('icon_maker\\images\\red.jpg', cv.IMREAD_ANYCOLOR)

def icon(frame, size, interpolation):
    two_d = np.float32(frame.reshape((-1,3)))
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _,label, center = cv.kmeans(two_d, 8, None , criteria, attempts=10, flags=cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape((frame.shape))


    dimensions2 = (size, size)
    resized = cv.resize(res, dimensions2, interpolation)
    return resized

img_processed = icon(img, 32, cv.INTER_NEAREST)


cv.imwrite("icon_maker\\images\\final.jpg", img_processed)

cv.waitKey(0)
cv.destroyAllWindows()
