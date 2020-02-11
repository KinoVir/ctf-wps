import cv2
import numpy as np

img_rgb = cv2.imread('51.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('template2.png', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#设定阈值
threshold = 0.2
#res大于70%
loc = np.where( res >= threshold)

print(loc[0][len(loc[0])-1])
print(loc[1][len(loc[1])-1])
