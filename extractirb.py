import cv2
import sys

print(sys.argv[1])

src = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)


red_channel = src[:,:,2]
blue_channel = src[:,:,0]
green_channel = src[:,:,1]

cv2.imwrite("./tmp/red_channel.jpg", red_channel)
cv2.imwrite("./tmp/green_channel.jpg", green_channel)
cv2.imwrite("./tmp/blue_channel.jpg", blue_channel)
