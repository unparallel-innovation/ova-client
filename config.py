import os
import sys


class Config:
    DETECTION_URL = os.getenv("DETECTION_URL", os.getenv('OVASERVER')+"/api/v1/detection")
    DETECTION_MODEL = os.getenv("DETECTION_MODEL", "yolov4")

    RESULT_DIR = os.getenv("RESULT_DIR", "static")

    URL_VISION = ""
    if(len(sys.argv)>1):
        URL_VISION="http://localhost:5000/startwithurl?url="
    else:
        URL_VISION="http://serverWithVision:5000/startwithurl?url="

config = Config()
