import requests
import json
import sys
import os

def getCameras():


    url = "https://tie.digitraffic.fi/api/v1/data/camera-data"

    payload = ""
    headers = {}


    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)

    camArray = []
    cameraUrl = [a_dict['cameraPresets'][0]['imageUrl'] for a_dict in jsonResponse['cameraStations']]
    return cameraUrl

if __name__ == "__main__":
    print(getCameras())
