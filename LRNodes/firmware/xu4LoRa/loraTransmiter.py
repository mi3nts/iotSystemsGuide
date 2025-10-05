
# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import itertools
import base64
from cgitb import strong
# import imp
# from this import d
import paho.mqtt.client as mqtt
import datetime 
from datetime import timedelta
import yaml
import collections
import json
import time 
import serial.tools.list_ports
from collections import OrderedDict
from glob import glob
from mintsXU4 import mintsDefinitions as mD
from mintsXU4 import mintsPoLo as mPL
from collections import OrderedDict
import struct
import numpy as np
import pynmea2
import shutil


import math
import sys
import time
import os
import smbus2

debug  = False 


loRaE5MiniPorts     = mD.loRaE5MiniPorts

appKey              = mD.appKey
macAddress          = mD.macAddress


if __name__ == "__main__":
    
    print()
    print("============ MINTS LoRa NODES ============")
    print()
    mPL.readingDeviceProperties(macAddress,loRaE5MiniPorts)
    
    e5MiniOnline,serE5Mini        = mPL.getPort(loRaE5MiniPorts,0,9600)


    while not mPL.loRaE5MiniJoin(e5MiniOnline,serE5Mini):
      print("Trying to connect")
      time.sleep(5)
    
    print("Connected to LoRa Network")

   
    while True:
        try:
            sensorDictionary =  OrderedDict([
                    ("temperature"  ,28.40), # check with arduino code
                    ("pressure"     ,98651.00),
                    ("humidity"     ,38.00),
                    ("altitude"     ,225.01)
                    ])
            # Make Sure these are float32
            sensorID = "BME280"
            port   = mPL.deriveSensorStats(sensorID)

            hexStr  = \
                    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) + \
                    np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) + \
                    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) + \
                    np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8) 
 
            print("HEX STRING: ")
            print(hexStr)
            time.sleep(20)   
                
            if hexStr is not None:
                mPL.sendCommand(serE5Mini ,'AT+PORT='+ str(port['portID']),2) 
                mPL.sendCommand(serE5Mini ,'AT+MSGHEX='+str(hexStr ),5)    

    

        except Exception as e:
            time.sleep(.5)
            print ("Error and type: %s - %s." % (e,type(e)))
            time.sleep(.5)
            print("Data Packet Not Sent")
            time.sleep(.5)


