from flask import Flask, render_template
#from data_processing import get_stack
from data_set import get_data
from search_data import linear_search, binary_s
from sort_data import bubble_sort, conduct_merge_sort

app = Flask(__name__)

@app.route('/')
def home():
   # email_stack = get_stack()  
    csv = get_data()
    return render_template('home.html', result=csv)
 
@app.route('/queue')
def queue():
    return render_template('queue.html')


@app.route('/search')
def search():
    linear = linear_search()
    binary = binary_s()
    return render_template('search.html', linear=linear, binary=binary)

@app.route('/sort')
def sort():
    bubble = bubble_search()
    merge = conduct_merge_sort()
    return render_template('search.html', bubble=bubble, merge=merge)


if __name__ == '__main__':
    app.run(debug=True) 
