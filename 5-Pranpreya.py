# Assignment 5: Implement Heapsort and Quicksort accordingly.
# Pranpreya Samasutthi (st122602)


import math
from random import randint

random_list = []


def build_max_heap(arr):
    half_to_root = math.ceil(len(arr)/2)
    for i in range(half_to_root-1, -1, -1):
        max_heapify(arr, len(arr), i)


def max_heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[i]:
        largest = left
    else:
        largest = i  # largest = root (heap.size)
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:   # When root is not biggest number
        # exchange arr[i] with arr[largest]
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        max_heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        # exchange arr[0] with arr[i]
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        max_heapify(arr, i, 0)


def quicksort(arr, p, r):
    if p < r:
        x = partition(arr, p, r)
        quicksort(arr, p, x - 1)
        quicksort(arr, x + 1, r)


def partition(arr, p, r):
    x = arr[r]
    i = (p - 1)

    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp1 = arr[i + 1]
    arr[i+1] = arr[r]
    arr[r] = temp1
    return i + 1


def random():
    random_amount = int(input("Enter amount that you want to sort: "))
    print("Random numbers are: ")
    # Random number follow amount that user input
    for _ in range(random_amount):
        value = randint(-50, 50)
        print(value, end=" ")
        random_list.append(value)


def main():
    # Input Type of sort
    sort = input("Enter 'H' for Heapsort sort or 'Q' for Quicksort: ")
    if sort == 'H' or sort == 'h':
        random()
        heapsort(random_list)
        print('\nAfter finishing Heapsort: ')
        for i in range(len(random_list)):
            print(random_list[i], end=" ")
    elif sort == 'Q' or sort == 'q':
        random()
        quicksort(random_list, 0, len(random_list)-1)
        print('\nAfter finishing Quicksort: ')
        for i in range(len(random_list)):
            print(random_list[i], end=" ")
    else:
        print("Your input is incorrect, please try again.")


main()
