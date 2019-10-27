# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:39:57 2019

@author: inter000
"""

import numpy as np
import matplotlib.pyplot as plt

def show_plot(points):
    shape_1 = points[0].shape[1]
    
    plot_x = np.append(np.arange(0, shape_1, 1), 0) * 2 * 3.14 / shape_1
    fig = plt.figure(figsize=[10, 10])
    axs = fig.add_subplot(projection="polar")
    plt.thetagrids(np.arange(0, 360, 360.0/shape_1), labels=np.arange(0, shape_1, 1))
    
    for x in points[0]:
        plot_y = np.append(x, x[0])
        axs.plot(plot_x, plot_y, color="red")

    for x in points[1]:
        plot_y = np.append(x, x[0])
        axs.plot(plot_x, plot_y, color="green")

    plt.show()

def get_pareto(points):
    pareto = np.empty([0, points.shape[1]])
    not_pareto = np.empty([0, points.shape[1]])
    ones_array = np.ones([points.shape[1], 1])
    
    pareto_val = (np.sum((points[i] <= points).dot(ones_array) == points.shape[1]) for i in range(points.shape[0]))
    for val, point in zip(pareto_val, points):
        if val > 1:
            not_pareto = np.vstack((not_pareto, point))
        else:
            pareto = np.vstack((pareto, point))
            
    return not_pareto, pareto

def main():
    N, M = (map(int ,input('Enter N and M: ').split()))
    points = np.random.sample((N, M))
    show_plot(get_pareto(points))
    
if __name__ == '__main__':
    main()