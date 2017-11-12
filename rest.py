#import useful libraries
from flask import Flask, render_template
import urllib2
from xml.dom.minidom import parseString


#make the flask object
app = Flask(__name__)


#bind to a route
@app.route('/')
def home_route():
    request = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=cQud53en8RollBuMSxaEGZ6Foydigx51KDWmgTKr")
    xml_string = request.read()
    return ""

def getText(element, listOfTags):
    if len(listOfTags) == 0:
        text = ""
        for node in element.childNodes:
            if node.nodeType == node.TEXT_NODE:
                text += node.data
        return text
    else:
        children = element.getElementsByTagName(listOfTags[0])
        return getText(children[0], listOfTags[1:])

#start the Flask server
if __name__ == "__main__":
    app.debug = True
    app.run()