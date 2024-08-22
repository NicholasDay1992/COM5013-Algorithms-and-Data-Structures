from flask import Flask, render_template
#from data_processing import get_stack
from data_set import get_data
from search_data import init_data

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
    return_dict = init_data()
    return render_template('search.html', result=return_dict)

if __name__ == '__main__':
    app.run(debug=True) 
