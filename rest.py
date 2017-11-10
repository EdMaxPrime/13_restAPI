#import useful libraries
from flask import Flask, render_template
import urllib2
import json


#make the flask object
app = Flask(__name__)


#bind to a route
@app.route('/')
def home_route():
    return render_template("index.html")


#start the Flask server
if __name__ == "__main__":
    app.debug = True
    app.run()