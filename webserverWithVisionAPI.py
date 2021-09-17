from flask import Flask, render_template, request, jsonify
import requests
import os
import ova_client
import json
import sys
import getCamerasFinland
import getCamerasAustralia
import time

PEOPLE_FOLDER = os.path.join('static')

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
    full_filename_no_result = os.path.join(app.config['UPLOAD_FOLDER'], 'no_results_loading.png')

    app.route('/')
    if os.path.isfile(full_filename):
        return render_template("home.html", user_image = full_filename)
    else:
        return render_template("home.html", user_image = full_filename_no_result)


@app.route('/stats')
def stats():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'predictions.json')
    full_filename_no_result = os.path.join(app.config['UPLOAD_FOLDER'], 'no_statics_loading.png')
    app.route('/stats')
    if os.path.isfile(full_filename):
        file_predi = open(full_filename,'r')
        jsonObj= json.load(file_predi)
        objectDetect =[]
        for obj in jsonObj:
            objectDetect.append(obj['label'])
        objectDetect_dict = {i:objectDetect.count(i) for i in objectDetect}
        temp=[]
        for the_key, the_value in objectDetect_dict.items():
            temp.append({"Object Name":the_key,"Count":the_value})
        columnNames = ["Object Name","Count"]
        if len(temp) > 0:
            return render_template('stats.html', records=temp, colnames=columnNames)
        else:
            return render_template("statsnofile.html", user_image = full_filename_no_result)
    else:
        return render_template("statsnofile.html", user_image = full_filename_no_result)




@app.route('/startwithurl', methods=["POST"])
def startwithurl():
    ova_client.detection(request.args.get('url') ,"True","True")
    return request.data


@app.route('/get_finland',methods=["GET","POST"])
def get_finland():

    try:
        url=""
        if(len(sys.argv)>1):
            url = "http://localhost:5000/startwithurl?url=" +getCamerasFinland.getCameras()[int(request.args.get('url_image'))]
        else:

            url = "http://serverWithVision:5000/startwithurl?url=" +getCamerasFinland.getCameras()[int(request.args.get('url_image'))]
        payload = ""
        headers = {}

        response = requests.request("post", url, headers=headers, data=payload)
        print(response)
        return jsonify({"result":"The image was succefully changed"})
    except Exception as e:
        print(e)
        return jsonify({"result":"Error in OpenVisionAPI."})


@app.route('/get_australia',methods=["GET","POST"])
def get_australia():
    print(request.args.get('url_image'))
    try:
        url=""
        if(len(sys.argv)>1):
            url = "http://localhost:5000/startwithurl?url=" +getCamerasAustralia.getCameras()[int(request.args.get('url_image'))]
        else:

            url = "http://serverWithVision:5000/startwithurl?url=" +getCamerasAustralia.getCameras()[int(request.args.get('url_image'))]
        payload = ""
        headers = {}

        response = requests.request("post", url, headers=headers, data=payload)
        print(response)
        return jsonify({"result":"The image was succefully changed"})
    except Exception as e:
        print(e)
        return jsonify({"result":"Error in OpenVisionAPI."})

@app.route('/get_url_custom',methods=["GET","POST"])
def get_url_custom():
    app.route('/get_url_custom')

    try:
        value = ova_client.detection(request.args.get('url_image') ,"True","True")
        return jsonify({"result":"The image was succefully changed"})
    except Exception as e:
        print(e)
        jsonify({"result":"Error in OpenVisionAPI. Incorrect URL?"})


@app.route('/changeimage',methods=["GET"])
def changeimage():
    app.route('/changeimage')
    return render_template("changeimage.html")


if __name__=="__main__":
    app.run(host="0.0.0.0")
