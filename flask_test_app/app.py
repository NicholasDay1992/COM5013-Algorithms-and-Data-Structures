from flask import Flask, render_template
#from flask_test_app.data_processing import get_stack
from flask_test_app.data_set import get_data

app = Flask(__name__)

@app.route('/')
def home():
   # email_stack = get_stack()  
    csv = get_data()
    return render_template('home.html', result=csv)
 
@app.route('/queue')
def about():
    return render_template('queue.html')

''' 
@app.route('/stack')
def about():
    return render_template('stack.html')
'''

if __name__ == '__main__':
    app.run(debug=True) 
