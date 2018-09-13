# MQTT-Raspberry-Pi 

Send images from raspberry pi using MQTT.

### Prerequisites

You will need a raspberry pi running raspbian, a rpi camera module.
For mqtt we will be using paho-mqtt, which can be installed by:-

```
pip install paho-mqtt
```
Note: The above scripts are made for python 2.7, python 3 is your adventure!

## Running the scripts

First, run the client script by typing:
```
python mqtt_client.py
```
And then, on the raspberry pi: 
```
python mqtt_rpi.py
```
