import sys
import json
import requests
import ast

#----------------------------------------------------------------------------------------------------------------------
API_key = 'Au2clK8NIloAWk_SfDBo7__EY0Qg1t8WfIQLHBolVq-XNwlvAcwMLwJx3Ha_jnGY'#enter bing Maps API key

oldSpeedLimit = 40

# main_api = url % (coordinates)

def snapToRoads(coordinates):
    main_api = 'https://dev.virtualearth.net/REST/v1/Routes/SnapToRoad?points=' + str(coordinates[0]) + "," + str(coordinates[1]) + '&includeTruckSpeedLimit=true&IncludeSpeedLimit=true&speedUnit=KPH&travelMode=driving&key=' + API_key
    json_data = str(requests.get(main_api).json())
    a = json_data.replace("'", '"')
    b = json.loads(a)
    try:
        return(b["resourceSets"][0]["resources"][0]["snappedPoints"][0]["speedLimit"])
    except Exception:
        return(1)


speedLimitList = []

list = [[-33.955481, 25.617293], [-33.91469, 25.61142], [-33.80138, 25.65565], [-33.79609, 25.65877], [-33.812118, 25.651559]]

def prepare_speedLimits(list):
    for x in range(len(list)):
        # lat = str(list[x][0])
        # long = str(list[x][1])
        coordinates = list[x]
        # coordinates = (lat + "," + long)
        # print(coordinates)
        # try:
        speedLimit = snapToRoads(coordinates)
        if speedLimit != 1:
            speedLimitList.append(speedLimit)
            oldSpeedLimit = speedLimit
            print( 'speed limit:', speedLimit)
        else:
            speedLimitList.append(oldSpeedLimit)
            print('using old speed limit:', oldSpeedLimit)

    return(speedLimitList)







# lat = str(-34.00277917)
# long = str(25.67121917)




