# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time
import argparse

parser = argparse.ArgumentParser(description='Enable Debug Mode in Modules.')
parser.add_argument('board', type=int,
                    help='Specify the board to enable debug mode')
parser.add_argument('debug', type=int,
                    help='Enable debug mode')

args = parser.parse_args()
print(args.debug)
print(args.board)

mqttc = mqtt.Client("debugMode")
#mqttc.username_pw_set(openhabian, password=rest1sum3)
mqttc.connect("192.168.1.136", 1883)

if (args.board == 1):
	mqttc.publish("myHome/board/room01/debug", str(args.debug))
if (args.board == 2):
	mqttc.publish("myHome/board/room02/debug", str(args.debug))
if (args.board == 3):
	mqttc.publish("myHome/board/room03/debug", str(args.debug))
