import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json

def calculate_EC(list):
        # list = [ [ "100", "0", "0", "0", "0" ], [ "100", "0", "0", "0", "0" ], ]
        # list = [[669.0, 14.722234000000002, 0.04946731506849315, 22.2, 1022.05, 60, 6.061036897532004, 0.0, 0.0, 86.00405101574992, 179.05031973637338, -0.004484289903609483, 0, -3], [1329.0, 13.333344, -0.011111120000000002, 22.18, 1022.05, 60, 15.537830167366359, -16.732960214814046, 0.0, 70.5470817562778, 179.0435541808656, 0.009781634828359606, 13, 0], [426.0, 13.333344, 0.0, 22.18, 1022.05, 60, 8.77546640762279, 0.0, 8.600027296931572, 70.5470817562778, 179.05014673107627, -0.004694818433914102, 0, -2], [2830.0, 11.388898000000001, -0.00977108542713568, 22.28, 1022.02, 60, 15.532468279476113, -15.43942437873162, 0.0, 51.452267060555364, 179.05157226363707, 0.0024734957109928467, 7, 0]]


        data =  {

                "Inputs": {

                        "input1":
                        {
                            "ColumnNames": ["distanceF", "speedF", "Acc", "Ambient", "pressure", "speedLimit", "crosswindF", "tailwindFP", "headwindF", "Drag", "Rolling_F", "angle_sin", "P_elv", "N_elv_old"],
                            "Values": list
                        },        },
                    "GlobalParameters": {
        }
            }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/8d2be10ae0e149558661c497500acdcb/services/83a33112ba5041ecb0b62dc139020d50/execute?api-version=2.0&details=true'
        api_key = '/G1adPLE+7SYWCyJjT90hdlOtctTEOGkL1aIwEp7R4pK7jKz75262jYn/auF1GaZAoHjNQL8/0gKnPLuvCQ6VQ==' # Replace this with the API key for the web service' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        try:

            response = urllib.request.urlopen(req)
            result = response.read()
            print(result)

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))








# # If you are using Python 3+, import urllib instead of urllib2
#
# import json
#
# data = {
#
#         "Inputs": {
#
#                 "input1":
#
#                 [
#
#                     {
#
#                             'Distance': "130",
#
#                             'Speed': "15",
#
#                             'Speed^2': "225",
#
#                             'SOC_Prev': "98",
#
#                             'Elevation_diff': "11",
#
#                     }
#
#                 ],
#
#         },
#
#     "GlobalParameters":  {
#
#     }
#
# }
#
# body = str.encode(json.dumps(data))
#
#
# url = 'https://ussouthcentral.services.azureml.net/workspaces/8d2be10ae0e149558661c497500acdcb/services/7adcb0c3be794dffb922e54b1c9f600c/execute?api-version=2.0&format=swagger'
#
# api_key = 'FAKHLyeVwWT3J28mI2MS+jQJ7Q57ZMUxZpMzI+7kuSh2OVrEKK5mSLgssMxQzFIdQ4Y9ZFSbnxxiMcZwMvQ4/A==' # Replace this with the API key for the web service
#
# headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
#
# req = urllib.request.Request(url, body, headers)
#
#
# try:
#
#     response = urllib.request.urlopen(req)
#     result = response.read()
#     print(result)
#
# except urllib.error.HTTPError as error:
#     print("The request failed with status code: " + str(error.code))
#
#
#
#     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
#
#     print(error.info())
#     print(json.loads(error.read().decode("utf8", 'ignore')))#
