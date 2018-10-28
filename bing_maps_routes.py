import urllib.request
import json

# Your Bing Maps Key
bingMapsKey = "Au2clK8NIloAWk_SfDBo7__EY0Qg1t8WfIQLHBolVq-XNwlvAcwMLwJx3Ha_jnGY"

# Get coordinates from Routes API
def get_coordinates(start, dest):

    url = 'http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=' + start +  '&wp.1=' + dest + '&optmz=distance&routeAttributes=routePath&key=' + bingMapsKey

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)

    # Parse JSON result
    itineraryItems1 = result["resourceSets"][0]["resources"][0]["routePath"]
    itineraryItems2 = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]



    #Create list of full route coordinates
    line = itineraryItems1['line']
    coordinates = line['coordinates']

    # Create list of main segment coordinates/ maneuver points at main roads only
    maneuverPointList = []
    for item in itineraryItems2:
          maneuverPointList.append(item["maneuverPoint"]["coordinates"])

    timeList = []
    for item in itineraryItems2:
        timeList.append(item["travelDuration"])

    # return(coordinates, maneuverPointList)
    return(maneuverPointList, timeList)

# destGeocoded = '-33.953343,25.580699'

#Call function to return both lists
# coordinatesResult, maneuverPointListResult  = get_coordinates(destGeocoded)

#print results
# print('Printing route coordinates list:', coordinatesResult)
# print('Printing route coordinates list:', maneuverPointListResult)


