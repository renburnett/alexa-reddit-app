from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/reddit_reader")

#TODO: if website goes down from time to time, include try/except to avoid timeout

def get_headlines():
    url = 'https://www.reddit.com/r/worldnews/.json?limit=10'
    user_pass_dict = {  'user': 'USERNAME', 
                        'pass': 'PASS', 
                        'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Testing Alexa'})
    sess.post('https://www.reddit.com/api/login', data = user_pass_dict)
    time.sleep(1)
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    #inline foreach loop
    titles = [unidecode.unidecode(listing['data']['title']) for listing in data['data']['children']]
    titles = '... '.join([each for each in titles])
    return titles

print(get_headlines())

@app.route('/')
def homepage():
    return "Hello there"

@ask.launch
def start_skill():
    welcome_message = "Hello would you like the news?"
    return question(welcome_message)

@ask.intent("YesIntent")
def share_headlines():
    headlines = get_headlines()
    headlines_msg = "The current world news headlines are {}".format(headlines)
    return statement(headlines_msg)

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Okay no worries then... bye!'

if __name__ == 'main':
    app.run(debug=True)