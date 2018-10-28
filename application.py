from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/a",methods=['POST'])
def hello():
    return "Hello World!"

@app.route("/predict/<destination>/<origin>", methods=['POST'])
def predict(destination, origin):
    if request.method == 'POST':
        try:
            import geocoding
            import bing_maps_routes
            import bing_maps_distance_matrix
            import bing_maps_elevations
            import bing_maps_traffic_speed_flow
            import get_weather
            import get_heading
            import get_wind_type
            import get_drag
            import get_rolling_friction
            import get_speedLimits
            import get_acceleration
            import Azure_final

          
            #--------------------------------------------------------------------------------------------------
            #Module 1 - Geocoding Module

            # destGeocoded = geocoding.geocode('Fishaways - Sasol Summerstrand')
            destGeocoded = geocoding.geocode(destination)
            #--------------------------------------------------------------------------------------------------
            #Module 2 - Get Coordinates Module - coordinates for route to destination
            # this module can return two lists
            # coordinatesList provides more coordinates on route
            # maneuverPointList retruns list of each segment - use this list to reduce computational overhead
            #  coordinatesResult, maneuverPointListResult = bing_maps_routes.get_coordinates(destGeocoded) to get both lists

            # maneuverPointListResult = bing_maps_routes.get_coordinates( '-34.002053,25.670521', destGeocoded)
            maneuverPointListResult, durationList = bing_maps_routes.get_coordinates(origin,destGeocoded)

            print('printing maneuverPoints List coordinates------------')
            print(maneuverPointListResult)

            print('printing durations------------')
            print(durationList)

            # #--------------------------------------------------------------------------------------------------
            #Module 3 - Get Distances each segment on route to destination
            # Split list Coordinates in equal chunks smaller than 50

            distancesList = bing_maps_distance_matrix.split_coordinates(maneuverPointListResult)
            print('printing List of Distances------------')
            print(distancesList)
            print('total distance:',sum(distancesList))

            # #--------------------------------------------------------------------------------------------------
            # #Module 4 - Get elevations for each coordinate
            elevationList = bing_maps_elevations.get_elevations(maneuverPointListResult)
            print('printing elevations------------')
            print(elevationList)

            # #--------------------------------------------------------------------------------------------------
            # #Module 5 - Get Speeds
            # #Get speeds for list
            speedList = bing_maps_traffic_speed_flow.get_speeds_from_maps(maneuverPointListResult)
            print('Printing speed list from front----------')
            print(speedList)
            #
            # #--------------------------------------------------------------------------------------------------
            # #Module 6 - Get weather
            listwindSpeed, listwindBearing, listtemperature, listpressure = get_weather.get_weather(maneuverPointListResult)
            print('Weahter-----------')
            print("WindSpeed")
            print(listwindSpeed)
            print("Wind Bearing")
            print(listwindBearing)
            print("temperature")
            print(listtemperature)
            print('pressure')
            print(listpressure)
            # #--------------------------------------------------------------------------------------------------
            # #Module 7 - Get bearing
            bearingList = get_heading.prepare_heading_list(maneuverPointListResult)
            print('bearing')
            print(bearingList)

            ##Module 8 - Get windType
            crossWindList, tailWindList, headWindList = get_wind_type.prepare_wind_type(bearingList, listwindSpeed, listwindBearing)
            print("crosswind")
            print(crossWindList)
            print("tailwind")
            print(tailWindList)
            print("headwind")
            print(headWindList)

            # #--------------------------------------------------------------------------------------------------
            # #Module 9 - Get Drag
            dragList = get_drag.prepare_drag(listtemperature, listpressure, speedList)
            print("dragList")
            print(dragList)
            # #--------------------------------------------------------------------------------------------------
            # #Module 10 - Get Rolling Friction and calculate angle
            # return negative and positive elevation

            rollingfList, elvDiffList_Pos, elvDiffList_Neg, angleList = get_rolling_friction.get_elv_diff(elevationList, distancesList)
            print("rolling friction list")
            print(rollingfList)
            print("ELevation pos")
            print(elvDiffList_Pos)
            print("ELevation neg")
            print(elvDiffList_Neg)
            print("AngleList")
            print(angleList)

            #-----------------------------------------------------------------------------------------------
            # #Module 11 - Acceleration
            accList = get_acceleration.get_acceleration(speedList, durationList)
            print("accList")
            print(accList)

            #-----------------------------------------------------------------------------------------------
            # #Module 12 - SpeedLimits
            speedLimitList = get_speedLimits.prepare_speedLimits(maneuverPointListResult)
            print(speedLimitList)

            #-----------------------------------------------------------------------------------------------
            # #Module 13 -Print list lengths


            distancesListF = []
            speedList2 = []
            crossWindListM = []
            tailWindListM = []
            headWindListM = []

            speedList.pop(0)



            for x in range(len(speedList)):   #need to only get speeds not coordinates
                speed = speedList[x][1]
                speedF = speed * 0.277778
                speedList2.append(speedF)

            for x in range(len(distancesList)):
                distance = distancesList[x]
                distanceM = distance * 1000
                distancesListF.append(distanceM)

            for x in range(len(crossWindList)):
                crosswind = crossWindList[x]
                crossWindM = crosswind / 0.514444 #convert to meter per second
                crossWindListM.append(crossWindM)

            for x in range(len(tailWindList)):
                tailwind = tailWindList[x]
                tailWindM = tailwind / 0.514444 #convert to meter per second
                tailWindListM.append(tailWindM)

            for x in range(len(headWindList)):
                headwind = headWindList[x]
                headWindM = headwind / 0.514444 #convert to meter per second
                headWindListM.append(headWindM)

            speedLimitList.pop(0)
            dragList.pop(0)
            crossWindListM.pop(0)
            tailWindList.pop(0)
            headWindList.pop(0)
            listpressure.pop(0)
            listtemperature.pop(0)

            speedListF = speedList2
            speedLimitListF = speedLimitList
            dragListF = dragList
            crossWindListF  = crossWindListM
            headWindListF = headWindListM
            tailWindListF  = tailWindListM
            listpressureF = listpressure
            listtemperatureF = listtemperature

            #send to azure
            # speedLimitListF = speedLimitList.pop(0)
            # dragListF = dragList.pop(0)
            # crossWindListF = crossWindList.pop(0)
            # headWindListF = tailWindList.pop(0)
            # tailWindListF = headWindList.pop(0)
            # listpressureF = listpressure.pop(0)
            # listtemperatureF = listtemperature.pop(0)

            print('distance', len(distancesListF))
            print('acceleration',len(accList))
            print('speedF', len(speedListF))
            print('speedLimit',len(speedLimitListF))
            print('drag',len(dragListF))
            print('rolling',len(rollingfList))
            print('elv diff positive',len(elvDiffList_Pos))
            print('elv diff neg', len(elvDiffList_Neg))
            print('cross', len(crossWindListF))
            print('tail',len(tailWindListF))
            print('headwind',len(headWindListF))
            print('pressure',len(listpressureF))
            print('temp',len(listtemperatureF))
            print('angle', len(angleList))

        except ValueError:
            return jsonify("error")

        newlist = [distancesListF,
           speedListF,
           accList,
           listtemperatureF,
           listpressureF,
           speedLimitListF,
           crossWindListF,
           tailWindListF,
           headWindListF,
           dragListF,
           rollingfList,
           angleList,
           elvDiffList_Pos,
           elvDiffList_Neg]

        send_to_azure = [list(t) for t in zip(*newlist)]

        print(send_to_azure)

        from time import gmtime, strftime
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        print("CURRENT TIME:",time)
        Azure_final.calculate_EC(send_to_azure)

        return json.dumps({
            'distance': distancesList,
            'acceleration': accList,
            'speedF':speedListF,
            'speedLimit':speedLimitListF,
            'drag':dragListF,
            'rolling':rollingfList,
            'elv diff positive':elvDiffList_Pos,
            'elv diff neg':elvDiffList_Neg,
            'cross':crossWindListF,
            'tail':tailWindListF,
            'headwind':headWindListF,
            'pressure':listpressureF,
            'temp':listtemperatureF,
            'angle':angleList})

            # "coordinates" : maneuverPointListResult,
            #                "distances" : distancesList})
        return('success')

if __name__ == '__main__':
    app.run(debug=True)
