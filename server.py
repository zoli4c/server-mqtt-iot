import paho.mqtt.client as mqtt
import time
import json
from random import *

brokerIP = "localhost"

#Callback function
def on_connect(client, usrdata, flags, rc):
    print("Connect Successfull! Code: " + str(rc))
    # Subscribe topic "home/light"
    client.subscribe("home/light/#")

def on_message(client, usrdata, msg):
    print (str(msg.payload))

#msg={ "device_id":"d5_1", "value":[str(temperature),str(humidity)]}

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(brokerIP,1883)

client.loop_forever()
