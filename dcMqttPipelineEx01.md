# DC MQTT Pipeline

## Overview

This section demonstrates how **Node-RED**, **Grafana**, and **InfluxDB** integrate within the **Direct-Connect (DC) Node** data pipeline.  
We’ll start by exploring a test node setup, running a sensor script, and understanding how MQTT communication fits into the overall workflow.

---

## Step 1: Log In and Access the Test Node

1. **Log in** to the test node.
2. **Open a new shell** and navigate to the GitHub repository folder:

   ```bash
   su teamlary
   cd /home/teamlary/gitHubRepos/iotSystemsGuide/DCNodes/firmware/xu4Mqtt/
   ```

The `DCNodes` directory contains a representative codebase for operating **Direct-Connect (DC) Nodes** on single-board computers (SBCs).

Inspect the file [`bme280Reader.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/bme280Reader.py) — this script provides a basic implementation of a **climate sensor** (BME280) used in live deployments.

---

## Step 2: Run the Test Sensor Script

Execute the script:

```bash
python3 bme280Reader.py
```

Then, log in to InfluxDB to verify if recent data (from the last 5 minutes) is available.

---

## Step 3: Check Data in InfluxDB

1. Visit: [http://mdash.circ.utdallas.edu:8086/](http://mdash.circ.utdallas.edu:8086/)
2. Log in using your credentials.
3. Navigate to the **`sharedAirDFW`** bucket.
4. Filter by:
   - **Node Name**
   - **Sensor ID**

You can identify the correct node name using the [`id_lookup.csv`](https://github.com/mi3nts/AirQualityAnalysisWorkflows/blob/main/influxdb/nodered-docker/id_lookup.csv) file.

<p align="center">
  <img width="574" height="312" alt="Influx Dashboard 1" src="https://github.com/user-attachments/assets/52e26555-5284-46bf-b153-a0914a6beb9e" />
  <img width="571" height="278" alt="Influx Dashboard 2" src="https://github.com/user-attachments/assets/56dcbe13-a586-4c3d-b169-54d126b9520a" />
  <img width="574" height="310" alt="Influx Dashboard 3" src="https://github.com/user-attachments/assets/6d897a1a-62cd-456f-89d8-527a959d35e6" />
</p>

> ⚠️ Since MQTT is not yet activated on the node, you will **not** see any live data at this stage.

---

## Step 4: Enable MQTT on the Node

Open the **`mintsSensorReader`** file and **uncomment** the final two lines in the `sensorFinisher()` function, then rerun `bme280Reader.py`.

```python
def sensorFinisher(dateTime, sensorName, sensorDictionary):
    print("-----------------------------------")
    print("-------- Sensor Finisher ----------")
    print(sensorName)
    writePath = getWritePath(sensorName, dateTime)
    exists = directoryCheck(writePath)
    writeCSV2(writePath, sensorDictionary, exists)
    print(writePath)

    if(latestOn):
       mL.writeJSONLatest(sensorDictionary, sensorName)
    if(mqttOn):
       mL.writeMQTTLatest(sensorDictionary, sensorName)
```

Once MQTT is enabled, you should begin seeing live data arriving from the node.  
However, this will only work if the node is already registered in the workflow. Next, we’ll simulate a scenario where the node is brand new.

---

## Step 5: Simulate a New Node Registration

To simulate adding a new node, open [`mintsDefinitions.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/mintsXU4/mintsDefinitions.py) and comment out **line 30** as shown below:

```python
# nodeID = findMacAddress()
nodeID = "a0b1c2d3e4f5g6"
```

Then rerun:

```bash
python3 bme280Reader.py
```

Check again in InfluxDB for data under this **new node ID**.

> You’ll notice no data appears — this is expected.  
> The node hasn’t yet been registered in the system.  
> The following section describes how to register new nodes so their data is accepted by the InfluxDB workflow.
