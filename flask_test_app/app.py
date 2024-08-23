from flask import Flask, render_template
#from data_processing import get_stack
from data_set import get_data
from search_data import linear_search, binary_s
from sort_data import bubble_sort, conduct_merge_sort
from Amazon_dataset import get_amazon_data, linear_search_amazon_data

app = Flask(__name__)

@app.route('/')
def home():
   # email_stack = get_stack()  
    csv = get_data()
    return render_template('home.html', result=csv)

## 05 SEARCH

@app.route('/search')
def search():
    linear = linear_search()
    binary = binary_s()
    amazon = get_amazon_data()
    results_list = linear_search_amazon_data()
    
    user_dict = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Software Engineer",
        "location": "New York"
    }
    
    return render_template('search.html', linear=linear, binary=binary, amazon=amazon, user_dict = user_dict, results_list = results_list )


## 06 SORT

@app.route('/sort')
def sort():
    bubble = bubble_sort()
    merge = conduct_merge_sort()
    return render_template('sort.html', bubble=bubble, merge=merge)


## QUEUE

@app.route('/queue')
def queue():
    return render_template('queue.html')


if __name__ == '__main__':
    app.run(debug=True) 
