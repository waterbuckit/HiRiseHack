from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os
import sys

Image.MAX_IMAGE_PIXELS = None

if not os.path.exists('img'):
	os.mkdir("img")
root = sys.argv[1]
print(root)
response = requests.get(root)
img = Image.open(BytesIO(response.content))
filename = root.split("/")[-1][:-4]
img.save("img/" + filename + ".tiff")

"""
root = "https://hirise-pds.lpl.arizona.edu/PDS/EXTRAS/RDR/ESP/ORB_060100_060199/"
page = requests.get(root)
soup = BeautifulSoup(page.content, features="html5lib")

if not os.path.exists('img'):
	os.mkdir("img")

# _IRB.NOMAP.JP2   
#_IRB.NOMAP.browse.jpg

for a in soup.find_all('a', href=True)[1:]:
	url = root + a['href'] + a['href'][:-1] + "_IRB.NOMAP.JP2"
	print(url)
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	img.save("img/" + a['href'][:-1] + ".tiff")
"""
