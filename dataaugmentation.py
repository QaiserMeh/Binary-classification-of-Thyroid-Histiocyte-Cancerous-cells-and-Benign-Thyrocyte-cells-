# -*- coding: utf-8 -*-
"""DataAugmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2M83-lOoFRM5ngVlT-Foe5cTplgS9Wn
"""

from google.colab import drive
drive.mount('/content/drive')

import os
import cv2
import matplotlib.pyplot as plt

path = '/content/drive/MyDrive/DS/benign' 
images=os.listdir(path)
type(images)
len(images)

img_data=[]
for img in images:
    img_arr=cv2.imread(os.path.join(path,img))
    img_data.append(img_arr)

plt.figure(figsize=(20,20))
for i in range(len(img_data)):
    plt.subplot(10,10,i+1)
    plt.imshow(img_data[i])

from keras.preprocessing.image import ImageDataGenerator
from skimage import io

# Construct an instance of the ImageDataGenerator class
# Pass the augmentation parameters through the constructor. 

datagen = ImageDataGenerator(
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='reflect')

i = 0
for batch in datagen.flow_from_directory(directory='/content/drive/MyDrive/DS', classes=["benign"],
                                         batch_size=16,  
                                         target_size=(1200, 1600),
                                         color_mode="rgb",
                                         save_to_dir='/content/drive/MyDrive/TF2', 
                                         save_prefix="aug", 
                                         save_format="png"):
    i += 1
    if i > 24:
        break

pip install split-folders[full]

import splitfolders
input_folder='/content/drive/MyDrive/hist_ben_dataset'
splitfolders.ratio(input_folder, output="/content/drive/MyDrive/hist_ben_split",
                  seed=42, ratio=(.7,.2,.1),
                  group_prefix=None)