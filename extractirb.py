import cv2
import os
import sys
import imageio
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

cv2.imwrite("./tmp/2.png", red_channel)
cv2.imwrite("./tmp/1.png", green_channel)
cv2.imwrite("./tmp/0.png", blue_channel)

images = []
for i in range(3):
    images.append(imageio.imread("./tmp/%s.png" %(str(i))))
#for file_name in os.listdir("./tmp"):
#    if file_name.endswith(".png"):
#        file_path = os.path.join("./tmp", file_name)
#        images.append(imageio.imread(file_path))

fileName = sys.argv[1].split("/", 1)[1].split(".",1)[0] + ".gif"
imageio.mimsave("./results/%s" % (fileName), images)
print("Written to: ./results/%s" % (fileName))

