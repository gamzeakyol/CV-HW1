#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:21:28 2018

@author: gamzeakyol
"""
# multiband histogram calculation

import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

def histogram(I):
    R, C, B = I.shape # allocate the histogram
    hist = np.zeros([256, 1, B], dtype=np.uint8) # range through the intensity values
    
    for g in range(256):
        hist[g, 0,...] = np.sum(np.sum(I == g, 0), 0)
    return hist

image = img.imread('color1.png')
print(image.shape)

x = histogram(image)
print(x[:,:,0])

#plt.hist(x[:,:,0])
#plt.hist(x[:,:,1])
plt.hist(x[:,:,2])

