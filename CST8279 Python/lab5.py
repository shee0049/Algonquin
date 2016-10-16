import pycurl
import xml.etree.ElementTree as bus
import webbrowser
from StringIO import StringIO

def getOCData(stop, route):
   url = "appID=3875e418&apiKey=ea5f5d83fd97bc2d2b311c745cf3585b" + "&stopNo=" + stop + "&routeNo=" + route + "&format=xml"
   c = pycurl.Curl()
   c.setopt(pycurl.POST, True )
   c.setopt(pycurl.POSTFIELDS, url)
   c.setopt(pycurl.URL, 'https://api.octranspo1.com/v1.2/GetNextTripsForStop')
   c.setopt(pycurl.SSL_VERIFYHOST,0)
   c.setopt(pycurl.SSL_VERIFYPEER,0)
   buffer = StringIO()
   c.setopt(c.WRITEDATA, buffer)
   c.perform()
   return buffer

def doIt():
   stopNo = raw_input("Enter in a stop: ")
   routeNo = raw_input("Enter in a route: ")
   lst = []
   doc = bus.fromstring(getOCData(stopNo, routeNo).getvalue().decode('utf-8'))
   
   for b in doc.findall('.//{http://tempuri.org/}Trip'):
        lat = b.findtext('{http://tempuri.org/}Latitude')
        lon = b.findtext('{http://tempuri.org/}Longitude')
        start = b.findtext('{http://tempuri.org/}TripStartTime')
        print tuple((lat,lon,start))
        lst .append(tuple((lat,lon,start))) 
        url = 'https://www.google.ca/maps/place/' + lat + ',' + lon
        webbrowser.open_new(url)
if __name__ == '__main__':
    doIt()