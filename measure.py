import cv2
import matplotlib.pyplot as plt
import numpy as np


def canny(image):
    gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,100,200)#change ratio to outline defferent amounts of objects
    return canny

image = cv2.imread('(720).jpg')
lane_image=np.copy(image)
canny=canny(lane_image)
plt.imshow(canny)
plt.show()
