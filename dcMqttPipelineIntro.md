# DC MQTT Pipeline


## Air Quality Analysis Workflows Precurser
At this point we look at how Nodered, Grafana, and Influx DB interfaces work togeather. 

1. **Log in** to the test node.  
2. **Open a new shell** and navigate to the GitHub repository folder:
   ```bash
   su teamlary
   cd /home/teamlary/gitHubRepos/iotSystemsGuide/DCNodes/firmware/xu4Mqtt/
   ```

The `DCNodes` folder contains a typical codebase used to operate **Direct-Connect (DC) Nodes** on a single-board computer (SBC).  
At this point, inspect the file [`bme280Reader.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/bme280Reader.py), which demonstrates a sample implementation of a **climate sensor** used in our live nodes.

3. **Run the file:**
   ```bash
   python3 bme280Reader.py
   ```
4. Log into influx DB and check if data from the test node is available for the past 5 minutes.
   - Visit http://mdash.circ.utdallas.edu:8086/ and login
   - Navigate into sharedAirDFW Bucket
   - Filter by Node Name and Sensor ID to check if the Data is available.
   - You can figure out the Node Name Using this [file](https://github.com/mi3nts/AirQualityAnalysisWorkflows/blob/main/influxdb/nodered-docker/id_lookup.csv).
<img width="574" height="312" alt="Screenshot 2025-10-06 at 2 32 20 PM" src="https://github.com/user-attachments/assets/52e26555-5284-46bf-b153-a0914a6beb9e" /> 
<img width="571" height="278" alt="screenshot-mdash-circ-utdallas-edu-8086-2025-10-06-14-39-12" src="https://github.com/user-attachments/assets/56dcbe13-a586-4c3d-b169-54d126b9520a" /> 
<img width="574" height="310" alt="image" src="https://github.com/user-attachments/assets/6d897a1a-62cd-456f-89d8-527a959d35e6" />

Since Mqtt is not activiated on our node you wont see any data. Lets check how you can activate MQTT

5. On the Mints Sensor Reader file uncomment the last two lines and check rerun `bme280Reader.py`
```
def sensorFinisher(dateTime,sensorName,sensorDictionary):
    print("-----------------------------------")
    print("-------- Sensor Finisher ----------")
    print(sensorName)
    writePath = getWritePath(sensorName,dateTime)
    exists = directoryCheck(writePath)
    writeCSV2(writePath,sensorDictionary,exists)
    print(writePath)

    if(latestOn):
       mL.writeJSONLatest(sensorDictionary,sensorName)
    if(mqttOn):
       mL.writeMQTTLatest(sensorDictionary,sensorName)   
```
At this point you should be able to see data coming in from the node.  However this would not worked if this node  was a brand new node. Lets simulate a situation where we are trying to register a brand new node. 

6. Comment line 30 on the [mintsDefinitions.py](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/mintsXU4/mintsDefinitions.py) file and add inthe following line below.
```
# nodeID                = findMacAddress()
nodeID = "a0b1c2d3e4f5g6"
```
And then run `python3 bme280Reader.py` following up with a check in influx for the data from the new ID. As evident you wont see any data from the you wont see any data from the new ID.

This file describes how new nodes can be registered. 







