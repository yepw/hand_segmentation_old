import os
import random
from PIL import Image

root = "/home/intuitivecomputing/light-weight-refinenet/datasets/GTEA/Old_Masks"


for path, subdirs, files in os.walk(root):
    for name in files:
        print name
	im = Image.open('Old_Masks/'+name).resize((625,468))
	'''
	pixels = list(im.getdata())
	print(im)
	print(pixels)
	'''
	im_p = im.convert("P")
	'''
	pixels_p = list(im_p.getdata())
	print(im_p)
	print(pixels_p)
	'''
	im_p.save('Masks/'+name)
