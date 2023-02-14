import os
import cv2 as cv
from PIL import Image, UnidentifiedImageError
Image.MAX_IMAGE_PIXELS = 1000000000
from matplotlib import pyplot as plt
import numpy as np
import time

t = time.time()

imgs = 'G:\\My Drive\\Brain Image Segmentation\\ESE 440-1\\Deep Learning Images_Labeled'
masks = 'G:\\My Drive\\Brain Image Segmentation\\ESE 440-1\\Image Masks'

#imgs = '/gpfs/scratch/tkral/Deep Learning Images_Labeled'
#masks = '/gpfs/scratch/tkral/Image_masks'

def fill(arr):
    arr = np.array(arr, dtype='uint8')
    hmap = arr
    hmap = np.maximum.accumulate(arr, 1) & np.maximum.accumulate(arr[:, ::-1], 1)[:, ::-1]
    vmap = np.maximum.accumulate(arr, 0) & np.maximum.accumulate(arr[::-1, :], 0)[::-1, :]
    #plt.imshow(vmap)
    #plt.show()
    return hmap & vmap

def create(dir, newdir):
    files = os.listdir(dir)
    files = sorted(files)

    for filename in files:
        if os.path.isdir(dir + '\\' + filename):
            create(dir + '\\' + filename, newdir)
        elif filename != 'desktop.ini':
            try:
                print(dir + "\\" + filename)
                img = Image.open(dir + "\\" + filename).convert('RGB')  # giving PIL.Image.DecompressionBombError
            except FileNotFoundError:
                print("Unable to open image file:", filename)
            except UnidentifiedImageError:
                print("Ignoring roi file:", filename)
                continue
            print('opening', filename)
            copy = np.array(img, 'uint8')
            rc = copy[:,:,0]
            gc = copy[:,:,1]
            bc = copy[:,:,2]
            thresh = 255//2
            rc[rc>thresh] = 1
            rc[rc != 1 ] = 0
            gc[gc>thresh] = 1
            gc[gc != 1 ] = 0
            bc[bc>thresh] = 1
            bc[bc != 1 ] = 0
            blines = ~rc & gc
            ylines = gc & ~bc
            copy = ylines | blines
            kernel = np.ones((9, 9), dtype='uint8')
            dilated = cv.dilate(copy, kernel, iterations=1)
            dilated = fill(dilated)
            dilated = (dilated*255).astype(np.uint8)
            dilated = Image.fromarray(dilated)
            dilated.save(newdir + '\\' + filename[:len(filename) - 4] + '_mask.tif')
            print(filename[:len(filename) - 4] + '_mask.tif saved')

create(imgs, masks)
print("Done in:", time.time()-t)