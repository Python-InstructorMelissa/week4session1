from flask import Flask, render_template
from data.data import *
# from data.data import user
# from data.data import book

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to class"

@app.route('/html/')
def html():
    return render_template('index.html')

@app.route('/data/')
def dataDisplay():
    print("print users: ", user)
    print("print books: ", book)
    return render_template('data.html', user=user, book=book)

@app.route('/user/<int:user_id>/view/')
def viewUser(user_id):
    return render_template('viewUser.html', user=user[user_id-1])
# this works because we have our data file set up in numerical order (like the database will be) but since we aren't connected to an actual database we had to do it this way vs the typical way


if __name__=="__main__":
    app.run(debug=True)