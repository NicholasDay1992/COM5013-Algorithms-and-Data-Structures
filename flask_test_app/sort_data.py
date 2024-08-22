import os
import pandas as pd
import numpy as np
import time 
import random


def get_size():
    size = 5000000
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
    start_time = time.time()  # Start time


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
    init()
    sorted_arr = merge_sort(l)
    end_time = time.time()    # End time
    print(sorted_arr)

    execution_time = end_time - start_time  # Calculate the elapsed time
    print("Time taken to sort an unsorted array of", size, "elements took", execution_time, "seconds")
    print("Number of function calls:", call_count)
    #print("Sorted array:", sorted_arr)
    
    l = [size, value_sought, exists, call_count, execution_time]
    return l
    



def bubble_sort():


    #l = [size, value_sought, exists, call_count, execution_time]
    #return l
    return 5000
    




def init_data():
    size = get_size()
    call_count = 0 
    l = range(size)

    start_time = time.time()  # Start time

    for i in l: 
        print(i)
        call_count += 1  

    end_time = time.time()    # End time

    execution_time = end_time - start_time  # Calculate the elapsed time
    print("Time taken to read", size, "elements =", float(execution_time), "seconds")
    print("Number of function calls:", call_count)
    
    l = linear_search()
    
    #l = [size, call_count, execution_time]
    return l


def linear_search():
    size = get_size()
    call_count = 0 
    value_sought = get_value_sought()
    exists = False
    l = range(size)

    start_time = time.time()  # Start time

    for i in l: 
        print(i)
        if(i == value_sought):
            exists = True
            call_count += 1
            print(exists)  
            break
        else:
            call_count += 1  

    end_time = time.time()    # End time

    execution_time = end_time - start_time  # Calculate the elapsed time
    print("Time taken to find", value_sought, "in ", size, "elements =", float(execution_time), "seconds")
    print("Number of function calls:", call_count)
    
    l = [size, value_sought, exists, call_count, execution_time]
    return l

def binary_s():
    size = get_size()
    call_count = 0 
    #value_sought = get_value_sought()
    exists = False
    
    l = range(size)

    start_time = time.time()  # Start time
    binary_search(l, value_sought)
    
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2
        call_count += 1

        # Check if the target is at the middle
        if l[mid] == value_sought:
            exists = True
            call_count += 1
            break
            #return mid
        # If the target is smaller, ignore the right half
        elif l[mid] > value_sought:
            right = mid - 1
            call_count += 1
        # If the target is larger, ignore the left half
        else:
            left = mid + 1
            call_count += 1

    # If the target is not present in the array
    #return -1
    

    end_time = time.time()    # End time

    execution_time = end_time - start_time  # Calculate the elapsed time
    print("Time taken to find", value_sought, "in ", size, "elements =", float(execution_time), "seconds")
    print("Number of function calls:", call_count)
    
    l = [size, value_sought, exists, call_count, float(execution_time)]
    return l


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        #call_count += 1

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        # If the target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1
        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    # If the target is not present in the array
    return -1