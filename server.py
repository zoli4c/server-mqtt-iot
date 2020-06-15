import paho.mqtt.client as mqtt
import time
import json
from random import *

brokerIP = "52.187.144.179"

#Callback function
def on_connect(client, usrdata, flags, rc):
    if rc==0:
        print("Connect Successfull!")
        # Subscribe topic "home/light"
        client.Subscribe("home/light")

def on_message(client, usrdata, msg):
    print (str(msg.payload))

#msg={ "device_id":"d5_1", "value":[str(temperature),str(humidity)]}

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(brokerIP,1883)

client.loop_forever()