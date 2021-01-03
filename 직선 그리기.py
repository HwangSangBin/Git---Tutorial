# cv2. line(image, start, end, color, thickness)    하나의 직선을 그리는 함수

import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = np.full((512, 512, 3), 255, np.uint8)
image1 = cv2.line(image1, (0, 0), (255, 255), (255, 0, 0), 3)

plt.imshow(image1)
plt.show()