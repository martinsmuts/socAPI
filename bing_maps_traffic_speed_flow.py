import urllib.request
import json
from functools import partial
from multiprocessing.pool import Pool
from queue import Queue

import pandas as pd
import threading
import time
from multiprocessing import Process

# Your Bing Maps Key
bingMapsKey = "Au2clK8NIloAWk_SfDBo7__EY0Qg1t8WfIQLHBolVq-XNwlvAcwMLwJx3Ha_jnGY"

# input information
liveList = []
current_queue = Queue()
old_speed = 40
atleast_one = False

def get_speed_flow(coordinate):
    print("Processing: " + str(coordinate))
    order = 1
    global old_speed
    global current_queue
    #global liveList
    global atleast_one
    try:
        url = 'https://atlas.microsoft.com/traffic/flow/segment/json?subscription-key=L7sRNM4EL_PzFRmUv4sFPEw1dMNFirhfXkcC8oLzvsU&api-version=1.0&style=absolute&zoom=12&query=' + coordinate + '&=KMPH'
        request = urllib.request.Request(url)

        response = urllib.request.urlopen(request)
        r = response.read().decode(encoding="utf-8")
        result = json.loads(r)

        # itineraryItems = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
        itineraryItems = result["flowSegmentData"]
        currentSpeed = itineraryItems['currentSpeed']

        # print(currentSpeed)
        old_speed = currentSpeed

        liveList.append([currentSpeed])
        return [coordinate,currentSpeed]

    except:
        liveList.append([old_speed])
        return [coordinate,old_speed]

    atleast_one = True
    print("Done: " + coordinate)

currentSpeedList = []

def results_print():
    print(liveList)

def get_live_data():
    global liveList

    return liveList

def get_speeds_from_maps(coordinates):
    old_speed = 40
    df1 = coordinates
    df = pd.DataFrame({'col':df1})
    counter = 0

    temp_array = []

    #p = Pool(5)

    for (idx, row) in df.iterrows():
        coordinateStr = str(row.col)
        coordinateStrA = coordinateStr.replace("]", "")
        coordinateStrB = coordinateStrA.replace("[", "")
        coordinateStrC = coordinateStrB.replace(" ", "")

        temp_array.append(coordinateStrC)
        counter += 1

    global liveList
    p = Pool(5)
    result = p.map(get_speed_flow,temp_array)
    liveList = result
    print('printing speed results:')
    results_print()
    #print(result)

    return result
    #return(currentSpeedList)
