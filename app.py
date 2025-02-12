from flask import Flask, render_template
from pymongo import MongoClient


app = Flask(__name__)

uri = "mongodb+srv://icyowl:moon997sun@cluster0.uqwy3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    res = None
    try:
        client.admin.command('ping')
        res = 'You successfully connected to MongoDB!'
    except Exception as e:
        res = e
    return render_template('hello.html', name=name, res=res)
