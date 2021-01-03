# cv2.findContours(image, mode, method)     외각 찾기

# mode: Contours를 찾는 방법
# RETR_EXTERNAL: 바깥쪽 line 찾기
# RETR_LIST: 모든 line을 찾지만, Hierarchy 구성X
# RETR_TREE: 모든 line 찾고, 모든 Hierarchy 구성O

# method: Contours들을 찾는 근사치 방법
# CHAIN_APPROX_NONE: 모든 Contours 포인트 저장
# CHAIN_APPROX_SIMPLE: Contours Line을 그릴 수 있는 포인트 저장

# 입력 이미지는 Grat Scale Threshold 전처리 과정이 필요하다.

# cv2.drawContours(image, contours, contour_index, color, thickness)       외각 그리기

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("zzangu.jpg")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
plt.show()

contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()