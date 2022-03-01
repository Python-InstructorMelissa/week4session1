from flask import Flask, render_template  # Imports from the package flask the class of Flask
from data.data import data


app = Flask(__name__) # Creates 1 instance of the class of Flask and calling it app


@app.route('/')
def index():
    # print("the returned data: ", data)
    return render_template('index.html', datas=data)

@app.route('/welcome/')
def welcomeClass():
    return "Welcome Class to Week 4"











if __name__=='__main__':  # This function once we turn on the SERVER (not the shell) allows our application to stay alive
    app.run(debug=True) # debug = True is important while in development