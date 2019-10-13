# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 01:11:52 2019
Генерация индексов выборки
@author: inter000
"""

import math
import numpy as np

def getSetIndices(N, n_batches, ratio):
    """
    Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].
    Returns:
        generator for batch indices [i, j, k]
    """
    length = (N - 1) // (n_batches + (1 / ratio))
    inds = np.array([0, 0, 0])

    for i in range(n_batches):
        inds[1] = inds[0] + length * (1 / ratio)
        inds[2] = inds[1] + length
        inds = list(map(math.floor, inds))
        yield inds
        inds[0] += length

def main():
    for inds in getSetIndices(100, 5, 0.25):
        print(inds)

if __name__ == '__main__':
    main()