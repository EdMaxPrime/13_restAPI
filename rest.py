#import useful libraries
from flask import Flask, render_template
import urllib2
import json


#make the flask object
app = Flask(__name__)


#bind to a route
@app.route('/')
def home_route():
    request = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=cQud53en8RollBuMSxaEGZ6Foydigx51KDWmgTKr")
    string = request.read()
    dictionary = json.loads(string)
    return render_template("index.html", p = dictionary)


#start the Flask server
if __name__ == "__main__":
    app.debug = True
    app.run()