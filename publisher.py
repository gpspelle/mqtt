import sys

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
sys.argv = sys.argv[1:]
client.publish("temp/random", sys.argv[0])
client.disconnect()


