import cv2

src = cv2.imread("./img/" +, cv2.IMREAD_UNCHANGED)

red_channel = src[:,:,2]

cv2.imwrite("./tmp/", red_channel)

