import os
import pandas as pd
import numpy as np
import time 
import random


def get_size():
    size = 500000
    return size

''' 
def get_value_sought():
    global value_sought # declared global so this function only needs to be called once
    value_sought = random.randint(0,get_size())
    return value_sought
'''
def init():
    global call_count 
    call_count = 0 
    
    start_time = 0
    end_time = 0
    
    size = get_size()

    # Generate a list of random numbers between 0 and size-1 (4999)
    l = random.sample(range(size), size)
    print("values:", l)
    print("size:", len(l))
    return l 
    #start_time = time.time()  # Start time


def merge_sort(arr):
    global call_count 
    call_count += 1  # Increment the counter on each function call
    
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

def conduct_merge_sort():
    l = init()
    size = get_size()
    start_time = 0
    end_time = 0
    start_time = time.time()  # Start time
    
    sorted_arr = merge_sort(l)
    
    end_time = time.time()    # End time
    print(sorted_arr)

    execution_time = end_time - start_time  # Calculate the elapsed time
    print("Time taken to sort an unsorted array of", size, "elements took", execution_time, "seconds")
    print("Number of function calls:", call_count)
    #print("Sorted array:", sorted_arr)
    
    l = [size, call_count, execution_time]
    return l
    



def bubble_sort():


    #l = [size, value_sought, exists, call_count, execution_time]
    #return l
    return 5000
    