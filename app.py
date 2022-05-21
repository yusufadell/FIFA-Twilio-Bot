import os

import requests
from dateutil import parser, tz
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

urls = {'group': 'https://worldcup.sfg.io/teams/group_results',
        'country': 'https://worldcup.sfg.io/matches/country?fifa_code=',
        'today': 'https://worldcup.sfg.io/matches/today',
        'tomorrow': 'https://worldcup.sfg.io/matches/tomorrow'
        }

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
             'RUS', 'EGY', 'POR', 'MAR', 'URU', 'KSA', 'IRN', 'ESP',
             'DEN', 'AUS', 'FRA', 'PER', 'ARG', 'CRO', 'BRA', 'CRC',
             'NGA', 'ISL', 'SRB', 'SUI', 'BEL', 'TUN', 'GER', 'SWE']


app = Flask(__name__)

to_zone = tz.gettz('Africa/Cairo') # Set timezone to Cairo for better time display in SMS

#  / route acccepts POST requests
@app.route('/', methods=['POST'])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    # Get the message
    msg = request.values.get('Body', None)
    # Get the sender's number
    sender = request.values.get('From', None)
    # Check if the message is in the list of commands
    if msg in urls:
        # Get the data from the API
        r = requests.get(urls[msg])
        # Check if the API returned a 200 OK
        if r.status_code == 200:
            # Create a response
            resp.message(r.text)
        else:
            # Create a response
            resp.message("Sorry, we couldn't get the data")
    # Check if the message is a country
    elif msg in countries:
        # Get the data from the API
        r = requests.get(urls['country'] + msg)
        # Check if the API returned a 200 OK
        if r.status_code == 200:
            # Create a response
            resp.message(r.text)
        else:
            # Create a response
            resp.message("Sorry, we couldn't get the data")
    # Check if the message is a group
    elif msg == 'group':
        # Get the data from the API
        r = requests.get(urls['group'])
        # Check if the API returned a 200 OK
        if r.status_code == 200:
            # Create a response
            resp.message(r.text)
        else:
            # Create a response
            resp.message("Sorry, we couldn't get the data")
    # Check if the message is a date
    elif msg == 'today':
        # Get the data from the API
        r = requests.get(urls['today'])
        # Check if the API returned a 200 OK
        if r.status_code == 200:
            # Create a response
            resp.message(r.text)
        else:
            # Create a response
            resp.message("Sorry, we couldn't get the data")
    elif msg == 'tomorrow':
        # Get the data from the API
        r = requests.get(urls['tomorrow'])
        # Check if the API returned a 200 OK
        if r.status_code == 200:
            # Create a response
            resp.message(r.text)
        else:
            # Create a response
            resp.message("Sorry, we couldn't get the data")
            
if __name__ == "__main__":
    app.run(debug=True)    