import cv2
import numpy as np
import os
import sys
import imageio
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

brightness = 50 

try:
    # create tmp file
    os.mkdir("./tmp")
    # create results
    os.mkdir("./results")
except OSError:
    (OSError)

src = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED)

red_channel = src[:,:,2]
blue_channel = src[:,:,0]
green_channel = src[:,:,1]

cv2.imwrite("./tmp/2.jpg", red_channel)
cv2.imwrite("./tmp/1.jpg", green_channel)
cv2.imwrite("./tmp/0.jpg", blue_channel)

toImprove = cv2.imread("./tmp/0.jpg")
hsv = cv2.cvtColor(toImprove, cv2.COLOR_BGR2HSV)
hsv[:,:,2] += brightness
toImprove = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("./tmp/0.jpg", toImprove)

images = []
for i in range(3):
    images.append(imageio.imread("./tmp/%s.jpg" %(str(i)))) 


print("Extracted...")
#for file_name in os.listdir("./tmp"):
#    if file_name.endswith(".jpg"):
#        file_path = os.path.join("./tmp", file_name)
#        images.append(imageio.imread(file_path))

#fileName = sys.argv[1].split("/", 1)[1].split(".",1)[0] + ".gif"
#imageio.mimsave("./results/%s" % (fileName), images)
#print("Written to: ./results/%s" % (fileName))

