import os
import pandas as pd
import numpy as np

def init_dataset():
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    url = "https://raw.githubusercontent.com/OmkarPathak/Playing-with-datasets/master/Email%20Spam%20Filtering/emails.csv"
    df = pd.read_csv(url) 
    return df.head()


def get_data():
    l = init_dataset()
    c = l['text']
    #l = ["Nick Day", "John Smith", "Katriona Lukas", "Sam Wintersmith", st.get_sender()]
    #l = [0,1,2,3,4,5,6,7]
    return c
