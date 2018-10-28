import googlemaps
import urllib.request
import json

#using Google Maps webservice NOT BING MAPS

def geocode(destination):

    gmaps = googlemaps.Client(key='AIzaSyCiF10XWFrsziA0-g5_zEblnxRNNC_OMi8')
    geocodeResult = gmaps.geocode(destination)

    lat = geocodeResult[0]['geometry']['location']['lat']
    long = geocodeResult[0]['geometry']['location']['lng']

    destGeocoded = str(lat) + "," + str(long)

    return(destGeocoded)

# print(geocode('Baywest Mall Port Elizabeth'))
