from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

uri = "mongodb+srv://icyowl:moon997sun@cluster0.uqwy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client['test_db']
greet = db.greet
if not greet.count_documents({}):
    greet.insert_one({'name': 'alice'})

@app.route('/greet')
def index():
    cursor = greet.find()
    names = list(cursor)
    return render_template('hello.html', names=names)

@app.route('/greet/<name>')
def hello(name=None):
    greet.insert_one({'name': name})
    return redirect(url_for('index'))