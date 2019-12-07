import cv2
import sys

print(sys.argv[1])

src = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)


red_channel = src[:,:,2]

cv2.imwrite("./tmp/redchannel.jpg", red_channel)

