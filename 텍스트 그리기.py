# cv2.putText(image, text, position, font_type, font_scale, color)      하나의 텍스트를 그리는 함수

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, "SangBin", (0, 200), cv2.FONT_ITALIC, 2, (0, 0, 255))

plt.imshow(image)
plt.show()