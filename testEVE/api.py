# Create Eve object
import os
import sys
import json
import random
import requests
from flask import Flask, render_template, request

from eve import Eve

app = Eve()
app.config['DEBUG'] = True
app.config['TESTING'] = True

#Hello WORLD BABY!
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello World!'

# This route will accept a request containing JSON
# Then we'll convert that data into Python a structure
# and print it.
# Because we used a standard HTML form post to send the
# data, we need to get the JSON from request.form
# If on other hand the information was sent from an app,
# or even a python urllib2.Request we would need to use
# request.data to get the JSON string
@app.route('/request', methods=['POST'])
def jsonreq():
    # Get the JSON data sent from the form
    jsondata = request.get_json       #request.form['jsondata']
    # Convert the JSON data into a Python structure
    # data = json.loads(jsondata)
    return jsondata #can put html file here ## render_template('request.html', data=data, jsondata=jsondata)




########################################################################
##http://stackoverflow.com/questions/10434599/how-to-get-data-recieved-in-flask-request
########################################################################

@app.route('/signup', methods=['POST'])
def signup():
    headers = {'Content-Type': 'application/json'}
    data = request.get_json()   #todo, test with: request.args or request.form

    #do check with db, unique username?

    #we can post with json to MongoDB
    r = requests.post("http://localhost:5000/user", data=json.dumps(data), headers=headers)

    return r.json();    #json to create User Page (html)


@app.route('/login', methods=['POST'])
def login():
    headers = {'Content-Type': 'application/json'}
    data = request.get_json()   #input from paul, into data

    r = requests.post("http://localhost:5000/trylogin", data=data, headers=headers)

    return "Success!"


@app.route('/additem', methods=['POST'])
def additem():
    headers = {'Content-Type': 'application/json'}
    data = request.get_json()   #input from paul, into data

    lost_status = True
    data += lost_status  # somehow, or prob Paul do it already

    r = requests.post("http://localhost:5000/item", data=data, headers=headers)

    return "Success!"


@app.route('/searchItem', methods=['GET'])
def searchItem():
    headers = {'Content-Type': 'application/json'}
    data = request.get_json()   #input from paul, into data

    lost_status = False

    #todo : ranking algorithm here

    data += lost_status #somehow or prob Paul do it already

    r = requests.post("http://localhost:5000/item", data=data, headers=headers)

    return "Success!"



@app.route('/sendEmail/<id>', methods=['GET'])
def sendEmail():
    ##email api?
    return "Success!"


if __name__ == '__main__':
    app.run()

#curl -H "Content-Type:application/json" -X POST http://localhost:5000/user -d "{\"firstname\":\"jay\",\"lastname\":\"ray\",\"email":\"jayray\",\"password\":\"jaypwd\",\"rank\":1}"
