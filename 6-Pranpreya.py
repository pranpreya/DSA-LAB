# Assignment 6: Implement BucketSort and Radix sort
# Pranpreya Samasutthi (st122602)
import math

from numpy.random import randint
import time
import random


def bucket_sort(arr):
    b = []
    n = len(arr)
    # make b[i] an empty list
    for i in range(n):
        b.append([])

    # insert arr[t] into b[ceil(n*arr[i])]
    for i in range(n):
        index_b = math.ceil(n * arr[i])
        if index_b != len(arr):
            b[index_b].append(arr[i])
        else:
            b[len(arr) - 1].append(arr[i])

    # Sort array b with Insertion
    for i in range(n):
        b[i] = insertion_sort(b[i])

    # concatenate list b[0], b[1], .. together
    k = 0
    for i in range(n):
        for j in range(len(b[i])):
            arr[k] = b[i][j]
            k += 1
    return arr


def insertion_sort(b):
    for j in range(1, len(b), 1):
        key = b[j]  # set key as second value
        i = j - 1  # set i for comparison
        while i >= 0 and b[i] > key:  # Ascending order
            b[i + 1] = b[i]
            i = i - 1
        b[i + 1] = key
    return b


def radix_sort(arr):
    # find max number of input array
    max_num = max(arr)

    # use counting sort to sort every digit from least to max digit
    digit = 1
    while math.floor(max_num/digit) > 0:
        counting_sort(arr, digit)
        digit = digit * 10  # change digit to front 1 step


def counting_sort(arr, digit):
    c = [0] * 10  # assume that max_number in array is not more that 10 digits
    n = len(arr)
    for i in range(0, n):
        index = math.floor(arr[i]/digit) % 10  # value of current digit
        c[index] += 1
    for i in range(1, 10):
        c[i] = c[i] + c[i-1]

    i = n-1
    output_array = [0] * n
    while i >= 0:
        index = math.floor(arr[i]/digit) % 10
        output_array[c[index] - 1] = arr[i]
        c[index] -= 1
        i -= 1

    for j in range(0, len(arr)):
        arr[j] = output_array[j]


def main():
    element_sort = int(input("Enter amount that you want to sort: "))
    bucket_list = []
    for i in range(element_sort):
        rand = round(random.uniform(0, 1), 3)
        bucket_list.append(rand)
    bucket_start = time.time()
    bucket_sort(bucket_list)
    bucket_end = time.time()
    bucket_time = bucket_end - bucket_start

    radix_list = randint(1, 100, element_sort)
    #print('radix', radix_list)
    radix_start = time.time()
    radix_sort(radix_list)
    radix_end = time.time()
    radix_time = radix_end - radix_start
    print('Bucket sort Timing: ', bucket_time)
    print('Radix sort Timing: ', radix_time)
    #print('radix', radix_list)


main()


