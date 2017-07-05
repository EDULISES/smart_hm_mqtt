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
	bgr = '{0:02x}'.format(0xff)
	mqttc.publish("myHome/lampRgb01/room03", bgr)
	time.sleep(0.5)
	bgr = '{0:02x}'.format(0xff00)
	mqttc.publish("myHome/lampRgb01/room03", bgr)
	time.sleep(0.5)
	bgr = '{0:02x}'.format(0xff0000)
	mqttc.publish("myHome/lampRgb01/room03", bgr)
	time.sleep(0.5)
	bgr = '{0:02x}'.format(0)
	mqttc.publish("myHome/lampRgb01/room03", bgr)
	if (flagCmd == True):
		status = "1"
	else:
		status = "0"
	if (flagCmd == True):
		flagCmd = False
	else:
		flagCmd = True