# Registering New Sensors

Imagine a case where a brand new sensor is introduced into mints. Lets say this sensor is is called ISG001 and has the following feilds similar to what we had in the Direct Connect Nodes. 

``` python
ISG001_payload = (
    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["feelsLike"]).tobytes().hex().zfill(8) +
)

```
Initially check if this sensorID is already taken using this [file](https://github.com/mi3nts/iotSystemsGuide/blob/main/lrSensorAndPortIDs.py). Now we assign a port to it. for this example lets pick port 201. You can modify the port IDs files appropriately.   

1. Create a copy of `bme280reader.py` and name it `isg001Reader.py` on your node.
``` bash
cp bme280Transmitter.py isg001Transmitter.py

2. At this point modify isg001Reader.py to have a sensor named ISG002 with the appropriate dictinary as suggested above and then run it.
```python3 isg001Transmitter.py```

At this point check if a new sensor ID is visible on influx DB. This sensor data wont be available on influx since the sensor itself is not yet registered in the workflow. The following explains how it can be done.

3. At this point open the node red ineterface and navigate to the LoRa Node to InfluxDB tab.Modify the LoRaSummaryWrite function and add the new Sensor ID with its portID

```201:"ISG001"```
