from flask import Flask, render_template
from data_processing import get_stack  # Import your script
# First Flask App
app = Flask(__name__)

@app.route('/')
def home():
    email_stack = get_stack()  # Call the function from the script
    return render_template('home.html', result=email_stack)
 
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 
