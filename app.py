from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

uri = "mongodb+srv://icyowl:moon997sun@cluster0.uqwy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    message = ''
    try:
        client.admin.command('ping')
        message = 'You successfully connected to MongoDB!'
    except Exception as e:
        message = e
    return render_template('hello.html', name=name, message=message)
