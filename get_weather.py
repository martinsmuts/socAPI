from multiprocessing.pool import Pool

from forecastiopy import *
from forecastio import *
from forecast_io import *
import pandas as pd

# martin.smuts@nmmu.ac.za
YOUR_APY_KEY = '650e0b1e91cd0b5f4daa76c98a78e469'

# fio = ForecastIO.ForecastIO(YOUR_APY_KEY, latitude=Lisbon[0], longitude=Lisbon[1], time='1529055720')
# current = FIOCurrently.FIOCurrently(fio)

# print('Temperature:', current.temperature)
# print("summary", current.summary)
# print("icon", current.icon)
# print("precipType",current.precipType)
# print("temperature",current.temperature)
# print("apparentTemperature",current.apparentTemperature)
# print("dewPoint",current.dewPoint)
# print("humidity",current.humidity)
# print("pressure",current.pressure)
# print("pressureError",current.pressureError)
# print("windSpeed",current.windSpeed)
# print('windBearing:', current.windBearing)
# print("cloudCover",current.cloudCover)
# print("uvIndex",current.uvIndex)
# print("visibility",current.visibility)


# # Determine every 1000m to get weather info
# #----------------------------------------------------------------------------------------------------------------------
listWeather = []

counter = 0
temperature = 0
summary = ''
icon = ""
# precipType = ""
apparentTemperature = 0
dewPoint = 0
humidity = 0
pressure = 0
# pressureError = 0
windSpeed = 0
windBearing = 0
cloudCover = 0
uvIndex = 0
visibility = 0


listtemperature = []
listsummary= []
listicon = []
# listprecipType= []
listapparentTemperature= []
listdewPoint= []
listhumidity= []
listpressure= []
# listpressureError= []
listwindSpeed= []
listwindBearing = []
listcloudCover= []
listuvIndex= []


# ---------------------------------------------------------
# convert time to unix
#
# import time
# from calendar import timegm
# # g = "2018/06/15  10:04:57 AM"
#
# def convert_time(dates):
#     # dateBefore = date.find(" AM")
#     dateBefore1 = dates
#     # print(dateBefore1)
#     utc_time = time.strptime(dateBefore1, "%Y-%m-%d %H:%M:%S")
#     epoch_time = timegm(utc_time)
#     # print(epoch_time)
#     return(epoch_time)


# --------------------------------------------------------------------------

def process_single(x):
    lat = x[0]
    long = x[1]

    import calendar
    import time
    ts = str(calendar.timegm(time.gmtime()))
    print(ts)

    fio = ForecastIO.ForecastIO(YOUR_APY_KEY, latitude=lat, longitude=long, time=ts)
    current = FIOCurrently.FIOCurrently(fio)
    print('calling API')

    temperature = current.temperature
    summary = current.summary
    icon = current.icon
    # precipType = current.precipType
    apparentTemperature = current.apparentTemperature
    dewPoint = current.dewPoint
    humidity = current.humidity
    pressure = current.pressure
    # pressureError = current.pressureError
    windSpeed = current.windSpeed
    windBearing = current.windBearing
    cloudCover = current.cloudCover
    uvIndex = current.uvIndex

    listtemperature.append(temperature)
    listsummary.append(summary)
    listicon.append(icon)
    # listprecipType.append(precipType)
    listapparentTemperature.append(apparentTemperature)
    listdewPoint.append(dewPoint)
    listhumidity.append(humidity)
    listpressure.append(pressure)
    # listpressureError.append(pressureError)
    listwindSpeed.append(windSpeed)
    listwindBearing.append(windBearing)
    listcloudCover.append(cloudCover)
    listuvIndex.append(uvIndex)

    return (windSpeed, windBearing, temperature, pressure)

# For each row in the column
def get_weather(x_list):
    p = Pool(5)
    result = p.map(process_single, x_list)

    listwindSpeed = []
    listwindBearing = []
    listtemperature = []
    listpressure = []

    for r in result:
        listwindSpeed.append(r[0])
        listwindBearing.append(r[1])
        listtemperature.append(r[2])
        listpressure.append(r[3])

    return (listwindSpeed, listwindBearing, listtemperature, listpressure)
    #for x in list:
    #
    #
    #         if currentRow == initial:
    #             initial = initial + 20
    #
    #         elif currentTripId != tripCursor:
    #          tripCursor = tripCursor + 1
    #          print(tripCursor)
    #
    #     else:
    #         listtemperature.append(temperature)
    #         listsummary.append(summary)
    #         listicon.append(icon)
    #         # listprecipType.append(precipType)
    #         listapparentTemperature.append(apparentTemperature)
    #         listdewPoint.append(dewPoint)
    #         listhumidity.append(humidity)
    #         listpressure.append(pressure)
    #         # listpressureError.append(pressureError)
    #         listwindSpeed.append(windSpeed)
    #         listwindBearing.append(windBearing)
    #         listcloudCover.append(cloudCover)
    #         listuvIndex.append(uvIndex)
    #
    # df['temperature'] = listtemperature
    # df['summary'] = listsummary
    # df['icon'] = listicon
    # # df['precipType'] = listprecipType
    # df['apparentTemperature'] = listapparentTemperature
    # df['dewPoint'] = listdewPoint
    # df['humidity'] = listhumidity
    # df['pressure'] = listpressure
    # # df['pressureError'] = listpressureError
    # df['windSpeed'] = listwindSpeed
    # df['windBearing'] = listwindBearing
    # df['cloudCover'] = listcloudCover
    # df['uvIndex'] = listuvIndex






