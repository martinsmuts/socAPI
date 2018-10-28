import urllib.request
import json
import numpy as np
import math
# Your Bing Maps Key
bingMapsKey = "Au2clK8NIloAWk_SfDBo7__EY0Qg1t8WfIQLHBolVq-XNwlvAcwMLwJx3Ha_jnGY"

distList = []

#Get distances from DIstance Matrix
def get_distance(org, dest):

    url = 'https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=' + org + '&destinations=' + dest + '&travelMode=driving&key=' + bingMapsKey
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    #Get results
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)

    # create list of distances
    resultDict = result["resourceSets"][0]["resources"][0]["results"]

    #find corresponding distance in list that match index number (origin and end start for each pair)
    for item in resultDict:
       destinationIndex = item.pop('destinationIndex')
       originIndex = item.pop('originIndex')

       if originIndex == destinationIndex:
           travelDistance = item.pop('travelDistance')
           distList.append(travelDistance)

    return(distList)


#-------------------------------------------------------
# Split list of coordinates in chunks to ensure less than 50 coordinates per request
def split_coordinates(coordinates):
    splitNumber = 0
    coordinatesList = coordinates
    range = len(coordinates)
    #print original list
    # print(range)
    if range <= 50:
        splitNumber = 1
    else:
        splitNumber = math.ceil(range / 50)

    #split list into chunks and print new list with chunks
    listChunks = np.array_split(coordinatesList,splitNumber)
    print(listChunks)

    #strip listChunk to each seperate chunk
    #send each chunk during new loop as a string to Distance matrix
    thisRange = splitNumber
    distanceList = []
    x = 0
    while x < thisRange:
        #get origin for each cunk
        currentChunk = listChunks[x][0:-1]
        currentChunkStr = ''.join(map(str, currentChunk))
        print('printing current chunk string:')
        print(currentChunkStr)
        currentChunkStrA = currentChunkStr.replace("][", ";")
        currentChunkStrB = currentChunkStrA.replace("]", "")
        currentChunkStrC = currentChunkStrB.replace("  ", ",")
        currentChunkStrD = currentChunkStrC.replace("[", "")
        currentChunkStrE = currentChunkStrD.replace(" ", "")
        currentChunkStrF = currentChunkStrE.replace(",;", ";")
        currentChunkStrG = currentChunkStrF.replace(",,", ",")
        print('String Chunks origin---------', x)
        print(currentChunkStrG)
        orgin = currentChunkStrG

        currentChunkDest = listChunks[x][1:]
        currentChunkDestStr = ''.join(map(str, currentChunkDest))
        currentChunkDestStrA = currentChunkDestStr.replace("][", ";")
        currentChunkDestStrB = currentChunkDestStrA.replace("]", "")
        currentChunkDestStrC = currentChunkDestStrB.replace("  ", ",")
        currentChunkDestStrD = currentChunkDestStrC.replace("[", "")
        currentChunkDestStrE = currentChunkDestStrD.replace(" ", "")
        currentChunkDestStrF = currentChunkDestStrE.replace(",;", ";")
        currentChunkDestStrG = currentChunkDestStrF.replace(",,", ",")
        print('String Chunks destination---------', x)
        print(currentChunkDestStrG)
        destt = currentChunkDestStrG

        get_distance(orgin, destt)
        x = x + 1

    return distList









