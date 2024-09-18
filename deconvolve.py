# -*- coding: utf-8 -*-
"""
Author: Yichao
Date: 2024-08-28
Description: Deconvolution (discrete)

Usage:
    - Ensure that numpy and scipy are installed: pip install numpy scipy
    - Replace the example x[n] and y[n] with your own data.
"""


import numpy as np
from scipy.signal import deconvolve

# Example input signal x[n] and output signal y[n]
# Suppose length of x[n] is smaller than h[n]
# x = np.array([1, 2, 1])  # Replace with your actual input signal
# y = np.array([2, 8, 14, 12, 4])  # Replace with your actual output signal

x = np.array([1, 2, 1])  # Replace with your actual input signal
y = np.array([2, 8, 14, 13, 7, 3, 1])  # Replace with your actual output signal

# Deconvolution to find h[n]
h, remainder = deconvolve(y, x)

# print("Computed impulse response using scipy h[n]:", h)
# print("Remainder:", remainder)

# Self defined deconvolution function
def custom_deconvolve(x, y):

    len_y = len(y) # N = N1 + N2 - 1
    len_x = len(x)
    len_h = len_y - len_x + 1
    h = np.zeros(len_h)

    x = x[::-1]

    for ii in range(len_h):
        if ii < len_x:
            sum_temp = 0
            for jj in range(ii):
                sum_temp += x[-ii+jj-1] * h[jj]
            h[ii] = (y[ii] - sum_temp) / x[-1]
        elif ii < len_y-1:
            sum_temp = 0
            for jj in range(len_x-1):
                sum_temp += x[jj] * h[ii-2+jj]
            h[ii] = (y[ii] - sum_temp) / x[-1]
        else:
            continue
    return h

h1 = custom_deconvolve(x, y)
print("Computed impulse response using self defined function h1[n]:", h1)