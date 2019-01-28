import os
import cv2
import numpy as np
from PIL import Image

img_dir = './train_images'
img_list = os.listdir(img_dir)

img_W = 625
img_H = 469

mean = [0.] * 3;
std = [0.] * 3;
counter = 0;

for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = np.array(Image.open(img_path).resize((img_W,img_H)))/255.
    mean += np.mean(img, axis = (0,1))
    std += np.std(img, axis = (0,1))
    counter += 1

img_dir = './train_images'
img_list = os.listdir(img_dir)

for img_name in img_list:
    img_path = os.path.join(img_dir, img_name)
    img = np.array(Image.open(img_path).resize((img_W,img_H)))/255.
    mean += np.mean(img, axis = (0,1))
    std += np.std(img, axis = (0,1))
    counter += 1

print (mean/(counter))
print (std/(counter))
'''
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

dataset = datasets.ImageFolder('./',
                 transform=transforms.ToTensor())

loader = DataLoader(dataset,
                         batch_size=1,
                         num_workers=0,
                         shuffle=False)

mean = 0.
std = 0.
nb_samples = 0.
for data, _ in loader:
    batch_samples = data.size(0)
    data = data.view(batch_samples, data.size(1), -1)
    mean += data.mean(2).sum(0)
    std += data.std(2).sum(0)
    nb_samples += batch_samples

mean /= nb_samples
std /= nb_samples

print(mean)
print(std)
'''
