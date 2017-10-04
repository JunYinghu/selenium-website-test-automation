import json
import urllib2


def printResult(data):
    theJSON = json.loads(data)
    if 'title' in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    count = theJSON["metadata"]["count"]
    #print event count
    print str(count) + " events recorded"
    #prient each event , the place
    for i in theJSON ["features"]:
        print i["properties"]["place"]
    #print each event that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"]>=4.0:
            print "-------------------"
            print "%2.1f" % i["properties"]["mag"],i["properties"]["place"]

    #print each event where at least 1 person reported feeling something
    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports !=None) & (feltReports>0):

            print "%2.1f" %i["properties"]["mag"],i["properties"]["place"],"reported"


def main():
    webUrl = urllib2.urlopen("http://joemarini.com")
    # get resource code
    print "resource code" + str(webUrl.getcode())

    # get html code
    data = webUrl.read()
    print data
    with open("samplehtml.html","w") as samplehtml:
        samplehtml.write(data)

    # test jason
    #https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    print urldata

    webUrl = urllib2.urlopen(urldata)
    print webUrl.getcode()
    if (webUrl.getcode() == 200):
        data = webUrl.read()
        print (data)
        printResult(data)
    else:
        print "receive an error: " + str(webUrl.getcode())

if __name__ == '__main__':
    main()
