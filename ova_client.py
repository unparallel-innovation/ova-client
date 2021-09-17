#!/usr/bin/env python3

import json
from pathlib import Path

import click
import requests
from pygments import formatters, highlight, lexers

from config import config
from validators import validate_image
from visualize import visualize_image_predictions
from PIL import Image
import urllib.request
from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False



def detection(image, save, visualize):
    if (is_url(image)):
        urllib.request.urlretrieve(image,"result.jpg")
        img = Image.open("result.jpg")
        image = "result.jpg"

    mimetype = validate_image(image)

    url = config.DETECTION_URL
    files = {"image": (image, open(image, "rb"), mimetype)}
    body = {"model": config.DETECTION_MODEL}

    try:
        response = requests.post(url=url, files=files, data=body)
        response.raise_for_status()
    except Exception as e:
        raise SystemExit(e)

    predictions = response.json()["predictions"]

    if not visualize:
        output = json.dumps(predictions, indent=4, sort_keys=True)
        print(highlight(output, lexers.JsonLexer(), formatters.TerminalFormatter()))
        return

    result_dir = config.RESULT_DIR
    Path(result_dir).mkdir(parents=True, exist_ok=True)
    path = Path(f"{result_dir}/predictions.json")


    with open(path, 'w') as outfile:
        json.dump(predictions, outfile)
    outfile.close()

    img = visualize_image_predictions(image, predictions)

    if save:
        result_dir = config.RESULT_DIR
        Path(result_dir).mkdir(parents=True, exist_ok=True)
        path = Path(f"{result_dir}/{Path(image).name}")
        img.save(path)
    else:
        img.show()
