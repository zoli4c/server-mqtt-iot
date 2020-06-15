import paho.mqtt.client as mqtt
import time
import json
from random import *
def on_connect(client, usrdata, flags, rc):
    if rc==0:
        print("connect ok")
client=mqtt.Client("python1")
client.on_connect=on_connect
client.connect("52.187.144.179",1883)
client.loop_start()
while 1:
    #send msg
    temperature=random()
    humidity=random()
    msg={ "device_id":"d5_1", "value":[str(temperature),str(humidity)]}
    y=json.dumps(msg)
    client.publish("home",y)
    time.sleep(5)
client.loop_stop()