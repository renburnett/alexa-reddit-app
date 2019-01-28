from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

def get_headlines():
    pass

@app.route('/')
def homepage():
    return "Hello there"

@ask.launch
def start_skill():
    welcome_message = "Hello would you like the news?"


if __name__ == 'main':
    app.run(debug=True)