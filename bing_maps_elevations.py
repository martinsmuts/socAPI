import urllib.request
import json
import pandas as pd

# xl = pd.ExcelFile('prepared_DWE.xlsx')
# df = xl.parse("Sheet1")
# df1 = pd.read_excel('prepared_DWE.xlsx', 'Sheet1')

# Your Bing Maps Key
bingMapsKey = "Au2clK8NIloAWk_SfDBo7__EY0Qg1t8WfIQLHBolVq-XNwlvAcwMLwJx3Ha_jnGY"

#Call Elevations API
def get_elevations(org):

    coordinatesList = org
    coordinatesListA = ''.join(map(str, coordinatesList))
    print(coordinatesListA)
    coordinatesListB = coordinatesListA.replace("][", ",")
    coordinatesListC = coordinatesListB.replace(" ", "")
    coordinatesListD = coordinatesListC.replace("[", "")
    coordinatesListE = coordinatesListD.replace("]", "")
    # print(coordinatesListE)

    url = 'http://dev.virtualearth.net/REST/v1/Elevation/List?points=' + coordinatesListE + '&key=' + bingMapsKey

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    #Get results
    r = response.read().decode(encoding="utf-8")
    result = json.loads(r)

    elevationsList = []

    #create list of elevations
    resultDict = result["resourceSets"][0]["resources"][0]["elevations"]
    elevationsList = resultDict

    return elevationsList



