import json
import paho.mqtt.client as mqtt
import base64
from picamera import PiCamera
from time import sleep
import RPi.GPIO as gpio

def send_file():
        broker_address=#broker address
        port =  #port number
        username = #username
        password = #password

        with open("image.png", "rb") as imageFile:
                stringb64 = base64.b64encode(imageFile.read())

        client = mqtt.Client("Raspberry Pi")
        client.username_pw_set(username, password)
        client.connect(broker_address,port,60)

