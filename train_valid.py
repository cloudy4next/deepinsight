
import os, sys
import pathlib
import argparse
import numpy as np
import pandas as pd

from PIL import Image
from time import time
from time import sleep
from scipy import ndimage
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from sklearn.model_selection import train_test_split
import random
import math
import shutil


parser = argparse.ArgumentParser()
parser.add_argument('--dataset-dir', default='', help='Full path to the directory.')
parser.add_argument('--target-dir', default='', help='Full path to save.')

args = parser.parse_args()
data_dir = args.dataset_dir
target_dir = args.target_dir

onlyfiles = []
cont = 0

for folder in os.listdir(data_dir):
    i = 1
    
    fold = data_dir + '/' + folder
    cnt = 0 					
    for img in os.listdir(fold):
    	
    	onlyfiles.append(img)
    	cnt += 1
    print(cnt)
    percent = math.ceil((cnt * 10) / 100) + 1
    
    target_folder = target_dir + '/' + folder


    print(target_folder)
    try:
    	os.mkdir(target_folder)
    except:
    	print(' exists')
    	continue

    for moving in range(0, int(percent)):
    	random_file = random.choice(os.listdir(fold))
    	print(random_file)
    	file_to_move = fold + '/' + random_file
    	new_file = target_folder + '/' + random_file
    	shutil.copyfile(file_to_move, new_file)
    	cont += 1

print(cont)
