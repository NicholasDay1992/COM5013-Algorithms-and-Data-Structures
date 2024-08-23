import os
import pandas as pd
import numpy as np

def init_dataset():
    url = "https://raw.githubusercontent.com/riteshc6/amazon_scraper/master/downloads/Computers%20%26%20Accessories.csv"
    df = pd.read_csv(url) 
    return df


def get_amazon_data():
    l = init_dataset()
    c = l['Product']
    #l = ["Nick Day", "John Smith", "Katriona Lukas", "Sam Wintersmith", st.get_sender()]
    #l = [0,1,2,3,4,5,6,7]
    return c


def linear_search_amazon_data():
    l = get_amazon_data()
    #c = l['Product']
    
    search_str = "San"
    
    #results_list = []
    
    # Subset of words containing the letter 'a'
    results_list = [word for word in l if search_str in word]
    
    return results_list
    #return l
    