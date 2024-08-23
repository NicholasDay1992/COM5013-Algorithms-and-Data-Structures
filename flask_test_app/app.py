from flask import Flask, render_template, g
#from data_processing import get_stack
from data_set import get_data
from search_data import linear_search, binary_s
from sort_data import bubble_sort, conduct_merge_sort
from Amazon_dataset import get_amazon_data, linear_search_amazon_data
import sqlite3

app = Flask(__name__)

DATABASE = 'amazon.db'

# Function to connect to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Query the database
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


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
    
    amazon_db = query_db('SELECT * FROM amazon')
    
    user_dict = {
        "name": "John Doe",
        "age": 30,
        "occupation": "Software Engineer",
        "location": "New York"
    }
    
    return render_template('search.html', linear=linear, binary=binary, 
                           amazon=amazon, amazon_db = amazon_db, 
                           user_dict = user_dict, results_list = results_list)


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
