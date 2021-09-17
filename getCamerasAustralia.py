import requests
import json
import sys
import os

def getCameras():


    url = "https://api.transport.nsw.gov.au/v1/live/cameras"

    payload = ""
    if(len(sys.argv)>1):
        headers = {"Authorization": "Bearer apikey " + sys.argv[1]}
    else:
        headers = {"Authorization": "Bearer apikey " + os.getenv('api')}

    response = requests.request("GET", url, headers=headers, data=payload)
    jsonResponse = json.loads(response.text)

    a_key = "href"
    cameraUrl = [a_dict['properties'][a_key] for a_dict in jsonResponse['features']]

    return cameraUrl

if __name__ == "__main__":
    getCameras()
