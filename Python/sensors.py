# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time
import argparse

parser = argparse.ArgumentParser(description='Sensor example')
parser.add_argument('sensor', type=str,
                    help='Specify sensor type')
parser.add_argument('value', type=int,
                    help='Specify sensor value')

args = parser.parse_args()
print(args.sensor)
print(args.value)

mqttc = mqtt.Client("sensors")
#mqttc.username_pw_set(openhabian, password=rest1sum3)
mqttc.connect("localhost", 1883)

if (args.sensor == 'temp'):
	mqttc.publish("myHome/temperatureSensor/room01", str(args.value))
if (args.sensor == 'light'):
	mqttc.publish("myHome/lightSensor/room01", str(args.value))
if (args.sensor == 'humidity'):
	mqttc.publish("myHome/humiditySensor/room01", str(args.value))
if (args.sensor == 'door'):
	mqttc.publish("myHome/doorSensor/room1", str(args.value))
if (args.sensor == 'window'):
	mqttc.publish("myHome/windowSensor/room1", str(args.value))