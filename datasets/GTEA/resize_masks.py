import os
import random
from PIL import Image

root = "/home/intuitivecomputing/light-weight-refinenet/datasets/GTEA/Old_Masks"


for path, subdirs, files in os.walk(root):
    for name in files:
        print name
	im = Image.open('Old_Masks/'+name).resize((625,468))
	
	im_p = Image.new('P', (625,468),color = 39)
	newimdata = []		
	for color in im.getdata():
	    if color == 100:
		newimdata.append(1)
	    elif color == 150:
		newimdata.append(2)
	    else:
		newimdata.append(0)
	im_p.putdata(newimdata)
	im_p.putpalette([
    		0, 0, 0, # black background
    		255, 0, 0, # index 1 is red
    		255, 255, 0, # index 2 is yellow
	])
	im_p.save('Masks/'+name)
	print(im_p.mode)
	print(im_p.palette)
	color = im_p.getcolors()
	print(color)
