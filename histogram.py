#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Mon Oct 15 22:21:28 2018

@author: gamzeakyol
"""
# multiband histogram calculation

import numpy as np
import matplotlib.pyplot as plt
import cv2

#Creating histograms of images
def histogram(I):

    I = np.array(I)

    hist = np.zeros([256, 3])  # range through the intensity values

    for g in range(0, 256):
        hist[g, :] = np.sum(np.sum(I == g, 0),0)

    return hist

#Creating cumulative distributions
def cdf(histogram):

    cumdf = np.zeros_like(histogram)

    cumdf[0] = histogram[0]

    for i in range(1,255):
        cumdf[i] = histogram[i] + cumdf[i-1]

    cumdf = np.divide(cumdf, np.sum(histogram))

    return cumdf


#Creating lookup table
def lookup_table(pi, pj):

    LUT = np.arange(256)

    for gi in range(255):

        if (pi[gi] > np.amax(pj)):
            LUT[gi] = 256

        else:
            LUT[gi] = np.argmax(np.where(pj >= pi[gi], 1, 0))

    return LUT


#Histogram matching method
def histogram_match(lut, img, ch):

    R, C, B = np.shape(img)

    output_im = np.zeros((R,C))

    for i in range(R):
        for j in range(C):
            output_im[i,j] = lut[img[i, j, ch]]

    return output_im


#The code below is written for trying the methods
image = cv2.imread("color2.png")
image2 = cv2.imread("color1.png")

h1 = histogram(image)
h2 = histogram(image2)

c1_0 = cdf(h1[:,0])
c2_0 = cdf(h2[:,0])

c1_1 = cdf(h1[:, 1])
c2_1 = cdf(h2[:, 1])

c1_2 = cdf(h1[:, 2])
c2_2 = cdf(h2[:, 2])

LUT0 = lookup_table(c1_0, c2_0)
LUT1 = lookup_table(c1_1, c2_1)
LUT2 = lookup_table(c1_2, c2_2)


out_im0 = histogram_match(LUT0, image, 0)
out_im1 = histogram_match(LUT1, image, 1)
out_im2 = histogram_match(LUT2, image, 2)


out_im = np.dstack((out_im0, out_im1, out_im2))
output_hist = histogram(out_im)

out_im = np.divide(out_im, 255)


plt.figure()

#plt.bar(x=range(0,256), height=output_hist[:,0])
#plt.bar(x=range(0,256), height=output_hist[:,1])
#plt.bar(x=range(0,256), height=output_hist[:,2])

rgb = out_im[...,::-1]
plt.imshow(rgb)

plt.show()

#plt.imsave("outputt.png", rgb)




