"""This is a simple Flask server"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    """This is the index page"""
    return { "message": "Hello World" }
