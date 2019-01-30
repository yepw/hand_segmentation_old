import six
import sys
sys.path.append('../../')

from models.resnet import ResNetLW Bottleneck
from utils.helpers import prepare_img
import matplotlib 

import glob

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch

from PIL import Image

cmap = np.load('../../utils/cmap.npy')
has_cuda = torch.cuda.is_available()
img_dir = '../imgs/GETA/'
imgs = glob.glob('{}*[0-9].png'.format(img_dir))
n_classes = 40

# Initialise models
'''
model_inits = { 
    'rf_lw50_nyu'    : rf_lw50,
    'rf_lw101_nyu'   : rf_lw101, # key / constructor
    'rf_lw152_nyu'   : rf_lw152,
    }

models = dict()
for key,fun in six.iteritems(model_inits):
    net = fun(n_classes, pretrained=True).eval()
    if has_cuda:
        net = net.cuda()
    models[key] = net
'''
model = ResNetLW(Bottleneck, [3, 4, 6, 3], num_classes=num_classes)
model = model.load_state_dict(torch.load(cached_file, map_location=map_location), strict=False)
model = model.eval()
model = model.cuda()
    
# Figure 4 from the supplementary
n_cols = len(models) + 2 # 1 - for image, 1 - for GT
n_rows = len(imgs)

plt.figure(figsize=(16, 12))
idx = 1

with torch.no_grad():
    for img_path in imgs:
        img = np.array(Image.open(img_path))
        msk = cmap[np.array(Image.open(img_path.replace('.png', '_mask.png')))]
        orig_size = img.shape[:2][::-1]
        
        img_inp = torch.tensor(prepare_img(img).transpose(2, 0, 1)[None]).float()
        if has_cuda:
            img_inp = img_inp.cuda()
        
        plt.subplot(n_rows, n_cols, idx)
        plt.imshow(img)
        plt.title('img')
        plt.axis('off')
        idx += 1
        
        plt.subplot(n_rows, n_cols, idx)
        plt.imshow(msk)
        plt.title('gt')
        plt.axis('off')
        idx += 1
        
        for mname, mnet in six.iteritems(models):
            segm = mnet(img_inp)[0].data.cpu().numpy().transpose(1, 2, 0)
            segm = cv2.resize(segm, orig_size, interpolation=cv2.INTER_CUBIC)
            segm = cmap[segm.argmax(axis=2).astype(np.uint8)]
            
            plt.subplot(n_rows, n_cols, idx)
            plt.imshow(segm)
            plt.title(mname)
            plt.axis('off')
            idx += 1
