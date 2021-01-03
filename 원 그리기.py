# cv2.circle(image, center, radian, color, thickness)    하나의 원을 그리는 함수

import cv2
import numpy as np
import matplotlib.pyplot as plt

image3 = np.full((512, 512, 3), 255, np.uint8)
image3 = cv2.circle(image3, (255, 255), 30, (0, 255, 0), 3)

plt.imshow(image3)
plt.show()