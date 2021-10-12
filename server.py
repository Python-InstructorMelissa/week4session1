from flask import Flask, render_template   # importing the module (in this case also a class) of Flask ## Now also added the ability to render templates
from data.data import *

app = Flask(__name__)  # giving our project/ application a name - we are calling it app

@app.route('/') # setting the landing page/base route for our application
def index():
    return render_template('index.html', parks=parks, animals=animals)

# @app.route('/welcome')
# def welcome(): # our first function to be run at this route
#     return "Welcome to Flask!"  # What we want to print to our page

# @app.route('/about')
# def about():
#     return "We are learning python and creating routes"

@app.route('/about')
def about():
    return render_template('about.html', parks=parks)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')





if __name__=="__main__":  #  making sure our instance matches
    app.run(debug=True) # setting debug to true allows us to keep the server running and still make changes app.run essentially starts our server

