from flask import Flask
import json
import requests
app = Flask(__name__)

@app.route("/")
def hello():
    url = 'https://revealer-test-1.azurewebsites.net'
    r = requests.get(url = url)
    data = r.text
    print(r.status_code)
    print(data)
    output = "Hello, World with {} & {} from {}!".format(r.text, r.status_code, url)
    return output
