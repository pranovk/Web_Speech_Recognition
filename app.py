from random import random
import webbrowser
import requests
from flask import Flask, render_template, request, jsonify, url_for, redirect, Response

app = Flask(__name__)
FILE_PATH = "audios/audio.wav"
url = "http://45.77.13.19:5000/predict"

ButtonPressed = ""


@app.route("/word", methods=['POST', 'GET'])
def VoiceCommand():
    global word
    f = request.files['audio_data']
    print(f)
    with open('audios/audio.wav', 'wb') as audio:
        f.save(audio)
    print('file uploaded successfully')

    file = open(FILE_PATH, "rb")
    values = {"file": (FILE_PATH, file, "audio/wav")}
    response = requests.post(url, files=values)
    data = response.json()

    print("Predicted keyword: {}".format(data["keyword"]))
    word = format(data["keyword"])
    return word


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('home.html')


@app.route("/index", methods=['POST', 'GET'])
def single_product():
    return render_template('single-product.html')


@app.route("/cart", methods=['POST', 'GET'])
def cart():
    return render_template('cart.html')


@app.route("/checkout", methods=['POST', 'GET'])
def checkout():
    return render_template('checkout.html')


@app.route("/shipping-information", methods=['POST', 'GET'])
def shipping_information():
    return render_template('shipping-information.html')


word = ''

'''
@app.route("/word", methods=['POST', 'GET'])
def VoiceCommand():
    global word
    try:
        if request.method == "POST":

            f = request.files['audio_data']

            with open('audios/audio.wav', 'wb') as audio:
                f.save(audio)
            print('file uploaded successfully')

            file = open(FILE_PATH, "rb")
            values = {"file": (FILE_PATH, file, "audio/wav")}
            response = requests.post(url, files=values)
            data = response.json()

            print("Predicted keyword: {}".format(data["keyword"]))
            word = format(data["keyword"])
            print(word)
            return "success"

        else:
            print("false")
    except Exception as er:
        print(er)
    finally:

        return render_template('home.html', word=word)



'''
if __name__ == '__main__':
    app.run(debug=True)
