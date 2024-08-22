import os
import pandas as pd
import numpy as np
import time 
import random

def init_data():
    size = 5000
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
    size = 100000
    call_count = 0 
    value_sought = random.randint(0,size)
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

def binary_search():
    size = 100000
    call_count = 0 
    value_sought = random.randint(0,size)
    exists = False
    return size