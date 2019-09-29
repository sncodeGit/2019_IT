# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 10:56:57 2019
Фильтр Гаусса
@author: inter000

Environment:
Python 3.5.2
[GCC 5.4.0 20160609] on linux
"""
import matplotlib.pyplot as plt
import numpy as np
import math

def add_noise(img, rate=5):
    img[::rate, ::rate, :] = 1
    return

def get_kernel(window_size, sigma):
    kernel = np.zeros((window_size, window_size))
    mean = window_size // 2
    for x in range(window_size):
        for y in range(window_size):
            kernel[x][y] = math.exp( (-0.5 * (x - mean) / sigma) ** 2.0 + 
            ((y - mean) /sigma) ** 2.0) / (2 * math.pi * sigma * sigma)
    kernel /= kernel.sum()
    return kernel

def filter(img, window_size, sigma):
    gauss_img = np.zeros_like(img)
    kernel = get_kernel(window_size, sigma)
    mean = window_size // 2
    for k in range(img.shape[2]): # color channel
        for i in range(mean, img.shape[0]-mean): # rows
            for j in range(mean, img.shape[1]-mean): # columns
                window = img[i-mean:i+mean+1, j-mean:j+mean+1, k]
                gauss_img[i,j,k] = (kernel*window).sum()
    return gauss_img

# Input -> Noise -> Gaussian filter -> Show
def main():
    # Input
    print("Enter a name for the photo")
    img_name = input() 
    img = plt.imread(img_name)[:, :, :3] # :3 for RGB model
    
    print("Enter a windows size:")
    window_size = int(input())
    
    print("Enter a sigma:")
    sigma = int(input())
    
    # Noise
    add_noise(img)
    
    # Gaussin filter
    gauss_img = filter(img, window_size, sigma)

    # Show
    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(gauss_img)
    plt.show()
    
# Function main() call
main()