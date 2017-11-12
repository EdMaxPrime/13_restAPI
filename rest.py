#import useful libraries
from flask import Flask, render_template
import urllib2
from xml.dom.minidom import parseString


#make the flask object
app = Flask(__name__)


#bind to a route
@app.route('/')
def home_route():
    request = urllib2.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?q=newnations")
    xml_string = request.read()
    dom = parseString(xml_string)
    list_of_nations = getText(dom, ["NEWNATIONS"]).split(",")[:10]
    dom.unlink()
    nations = []
    for item in list_of_nations:
        nations.append(getNationData(item))
    #return str(dom.nodeType) + " " + str(dom.DOCUMENT_NODE) + " " + str(dom.ELEMENT_NODE)
    return render_template("table.html", categories=["Flag", "Name", "Full Name", "Motto", "Category", "Civil Rights", "Economic Freedom", "Political Freedom", "Region", "Population", "Tax Rate", "National Animal", "Major Industry", "Government Priority"], nations=nations)

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

def getNationData(nation):
    request = urllib2.urlopen("https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation)
    xml_string = request.read()
    dom = parseString(xml_string)
    d = {}
    d["Name"] = getText(dom, ["NAME"])
    d["Full Name"] = getText(dom, ["FULLNAME"])
    d["Motto"] = getText(dom, ["MOTTO"])
    d["Category"] = getText(dom, ["CATEGORY"])
    d["Civil Rights"] = getText(dom, ["FREEDOM", "CIVILRIGHTS"])
    d["Economic Freedom"] = getText(dom, ["FREEDOM", "ECONOMY"])
    d["Political Freedom"] = getText(dom, ["FREEDOM", "POLITICALFREEDOM"])
    d["Region"] = getText(dom, ["REGION"])
    d["Population"] = getText(dom, ["POPULATION"])
    d["Flag"] = getText(dom, ["FLAG"])
    d["Tax Rate"] = getText(dom, ["TAX"])
    d["National Animal"] = getText(dom, ["ANIMAL"])
    d["Major Industry"] = getText(dom, ["MAJORINDUSTRY"])
    d["Government Priority"] = getText(dom, ["GOVTPRIORITY"])
    d["Leader"] = getText(dom, ["LEADER"])
    d["Capital"] = getText(dom, ["CAPITAL"])
    #d[""] = getText(dom, [""])
    dom.unlink()
    return d

#start the Flask server
if __name__ == "__main__":
    app.debug = True
    app.run()