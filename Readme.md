In this repository it will be available a way to analyse an image and then identify the objects in there using the [OpenVisionAPI](https://openvisionapi.com). After that analyses it will be available multiple URL endpoint allowing the user to view stats, view an image with the objects identified in top the original image and choose another image to analysis from 3 different sources. <br>
To have a real traffic image we resort to some API already on the internet like [this from Australia](https://opendata.transport.nsw.gov.au/node/340/exploreapi) and [this from Finlandia](https://www.digitraffic.fi/en/road-traffic/#swagger-api-descriptions). It was developed a script to collect all the url images that various API sends. Then it will be necessary to choose the camera that user want to use, because the APIs has multiple cameras across all Australia and Finlandia.<br>
In this example we are using an existing OpenVisionAPI server, which can be consulted [here](https://github.com/openvisionapi/ova-server) the code open source. It is also needed a OpenVisionAPI client, which is already included in this repository, available [here](https://github.com/openvisionapi/ova-client), which will send the image pretending to be analysed to the server mentioned.<br>
It was used a webserver to facilitate the interactions and this webserver was based on [Flask](https://flask.palletsprojects.com/en/2.0.x/). Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
Flask offers suggestions, but doesn't enforce any dependencies or project layout. It is up to the developer to choose the tools and libraries they want to use. There are many extensions provided by the community that make adding new functionality easy.<br>



## 🚀 Getting Started
To use this you need to have previously an api key from https://opendata.transport.nsw.gov.au/node/340/exploreapi
After having that, you will be able to use this bundle and analyse what kind of objects were detected in the provided image.


There are two types of deployment. Standalone, to be run in a machine or through Docker.


# Standalone
### Prerequisites
```
$ make setup
```
### Usage
```
$ source .venv/bin/activate
$ python3 webserverWithVisionAPI.py  API_AUSTRALIA
```

# DOCKER
### Prerequisites
Build and deploy the image to an external Docker registry (DockerRegistryUrl_OpenVisionAPIWithWebserver). Please update the file according to the desired Docker registry URL.

```
$ chmod +x buildAndDeploy.sh
$ ./buildAndDeploy.sh
```


### USAGE
Create a docker-compose.yml with the information bellow and then use 'docker-compose up' to run.
```
version: '3.1'

services:
  serverWithVision:
    image: DockerRegistryUrl_OpenVisionAPIWithWebserver:TAG
    ports:
      - "5000:5000"
    environment:
      - api=API_IMAGE_AU
```



Run it locally

```
$ docker run -p 5000:5000  NAME
```
The NAME should contains the name of the image plus the tag. This details must be set in the buildAndDeploy script.

# Endpoints available
After running it, in both deploy options you will have several endpoints available:
- http://EXTERNAL_IP:5000 -> Contains the image with the objects identified in top of the original image
- http://EXTERNAL_IP:5000/stats -> Contains a table representing the objects identified.
- http://EXTERNAL_IP:5000/startwithurl?url=URL.jpg -> POST endpoint to be used to upload the image to be analysed by OpenVisionAPI. After the analysis the results in the previous pages will be updated.
- http://EXTERNAL_IP:5000/changeimage -> Contains a ui interface to change in real time the camera to be analysed. There is approximately 135 cameras to be consulted in Australia API and 774 in Finland API. You will also have the opportunity to send and image by URL.


## ✍️  Author
Unparallel Innovation
