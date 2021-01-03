# cv2.rectangle(image, start, end, color, thickness)    하나의 사각형을 그리는 함수

import cv2
import numpy as np
import matplotlib.pyplot as plt

image2 = np.full((512, 512, 3), 255, np.uint8)
image2 = cv2.rectangle(image2, (10, 10), (255, 255), (255, 0, 0), 3)    # thickness = -1 -> 안을 모두 채움

plt.imshow(image2)
plt.show()