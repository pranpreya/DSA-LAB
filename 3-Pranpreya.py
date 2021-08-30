# Assignment 3: Program the maximum subarray problem in python.
# by: Pranpreya Samasutthi (st122602)

import matplotlib.pyplot as plt
from numpy.random import randint
import math
import time
import numpy as np

num = 10
numList = list()
nlognList = list
subarray_timeList = list()
nlogn_timeList = list()
c = 1/500000


def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = 0
    for i in range(mid, low-1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float('-inf')
    sum = 0
    max_right = 0
    for j in range(mid+1, high+1):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(arr, low, high):
    # print(arr, low, high)
    if high == low:
        return low, high, arr[low]  # base case: have only one element
    else:
        mid = math.floor((low+high)/2)
        left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)    # begin left array
        right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)  # begin right array
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


while num <= 1000000:
    rand_array = randint(-100, 100, num)
    # Actual Time for Maximum subarray
    subarray_start = time.time()
    find_maximum_subarray(rand_array, 0, len(rand_array)-1)  # 1st index is 0
    subarray_end = time.time()
    # print(num, subarray_end - subarray_start)
    numList.append(num)
    subarray_timeList.append(subarray_end - subarray_start)
    # Theoretical complexity
    complexity = c * num * np.log(num)
    nlogn_timeList.append(complexity)
    # print(num, complexity)
    num = num*10

plt.figure(1)
plt.xlabel('Number of elements')
plt.ylabel('Time spent')
plt.plot(numList, subarray_timeList, label='Actual Time')
plt.grid()
plt.legend()

plt.figure(2)
plt.xlabel('Number of elements')
plt.ylabel('Time spent')
plt.plot(numList, nlogn_timeList, label='nlogn', color='r')
plt.grid()
plt.legend()
plt.show()
