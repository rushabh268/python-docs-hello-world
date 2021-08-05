from flask import Flask
import json
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    url = 'https://revealer-test-1.azurewebsites.net'
    r = requests.get(url = url)
    data = r.json()
    print data
    return "Hello, World!"
