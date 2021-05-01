from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/search")
def search():
    return render_template('search.html')
