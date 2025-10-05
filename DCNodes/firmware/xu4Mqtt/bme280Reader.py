#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import sys
from collections import OrderedDict
import time

sensorID     = "BME280"

def main():
    while True:
        try:
            dateTime = datetime.datetime.now()
            sensorDictionary =  OrderedDict([
                    ("dateTime"     , str(dateTime)), # always the same
                    ("temperature"  ,28.40), # check with arduino code
                    ("pressure"     ,98651.00),
                    ("humidity"     ,38.00),
                    ("altitude"     ,225.01)
                    ])

            mSR.sensorFinisher(dateTime,sensorID,sensorDictionary)
            time.sleep(10)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    print("Reading BME280 Data")
    main()    