from flask import Flask, render_template # Imports from the env package flask the class of Flask
from data.image import images
from data.movie import movies

app = Flask(__name__) # Creates 1 instance of the class of flask and giving it the name of app



# print('Hey class')
@app.route('/')
def index():
    # print('the data from movie file: ', movies)
    return render_template('index.html')

@app.route('/welcome/')
def welcome():
    return "Welcome Class to week 4, Whats cooking folks?"

@app.route('/movies/')
def theMovies():
    print('111111 the data from movie file: ', movies)
    print('222222 print just 1st index: ', movies[0])
    print('333333 print 1st index title: ', movies[0]['fullTitle'])
    return render_template('movies.html', theMovies=movies)

@app.route('/images/')
def theImages():
    # print('the data from image file: ', images)
    # print("print id=1: ", images[0])
    # print('print bugs name :', images[0]['name'])
    return render_template('images.html', theImages=images) #theImages = what we will use on the html to reference the data images =  what it is called on the python side




if __name__=='__main__': # This function once we turn on the SERVER (not the shell) allows our application to stay alive
    app.run(debug=True) # debug = True is important while in development