# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

flagCmd = True
status = "0"
mqttc = mqtt.Client("control3")
#mqttc.username_pw_set(openhabian, password=rest1sum3)
mqttc.connect("192.168.1.136", 1883)
while True:
	mqttc.publish("myHome/lamp01/room03", status)
	time.sleep(0.1)
	mqttc.publish("myHome/lamp02/room03", status)
	time.sleep(0.1)
	mqttc.publish("myHome/lamp03/room03", status)
	time.sleep(0.1)
	#mqttc.loop(2) #timeout = 2s
	if (flagCmd == True):
		status = "1"
	else:
		status = "0"
	if (flagCmd == True):
		flagCmd = False
	else:
		flagCmd = True
	time.sleep(3)