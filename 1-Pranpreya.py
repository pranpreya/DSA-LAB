# Assignment 1
# Insertion Sort and Merge Sort
# by: Pranpreya Samasutthi (st122602)

import math
from random import randint

random_list = []


# Insertion Sort
def insertion_sort(arr):
    # First index is 0, so Insertion sort begins with Index 1
    for j in range(1, len(arr), 1):
        key = arr[j]  # set key as second value
        i = j - 1  # set i for comparison
        while i >= 0 and arr[i] > key:  # Ascending order
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    print('\nAfter finishing Insertion sort: ')
    for inst in range(len(arr)):
        print(arr[inst], end=" ")


# Merge Sort
def merge_sort(arr_merge):
    if len(arr_merge) > 1:

        q = math.floor(len(arr_merge) / 2)  # ceiling function (floor or ceil is OK)
        # print('q: ', q)

        left_arr = arr_merge[:q]
        right_arr = arr_merge[q:]

        # recursive algorithm
        merge_sort(left_arr)  # Sorting the first half
        merge_sort(right_arr)  # Sorting the second half

        i = j = k = 0  # i controls Left, j controls Right, k controls A

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr_merge[k] = left_arr[i]  # copy A 1 to Left array
                i += 1
            else:
                arr_merge[k] = right_arr[j]  # copy A 2 to Right array
                j += 1
            k += 1

        # Check L and R array that have any existing value or not
        while i < len(left_arr):
            arr_merge[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr_merge[k] = right_arr[j]
            j += 1
            k += 1

        '''''''''
        for i in range(len(left_arr)):
            arr_merge[k] = left_arr[i]
            i += 1
            k += 1

        for j in range(len(right_arr)):
            arr_merge[k] = right_arr[j]
            j += 1
            k += 1
        '''''''''


def random():
    random_amount = int(input("Enter amount that you want to sort: "))
    print("Random numbers are: ")
    # Random number follow amount that user input
    for _ in range(random_amount):
        value = randint(0, 100)
        print(value, end=" ")
        random_list.append(value)


# Input Type of sort
sort = input("Enter 'I' for Insertion sort or 'M' for Merge: ")
if sort == 'I' or sort == 'i':
    random()
    insertion_sort(random_list)
elif sort == 'M' or sort == 'm':
    random()
    # p = 1
    # q = len(random_list)
    # merge_sort(random_list, p, q)
    merge_sort(random_list)
    print('\nAfter finishing Merge sort: ')
    for i in range(len(random_list)):
        print(random_list[i], end=" ")
else:
    print("Your input is incorrect, please try again.")
