# 🆕 Registering New Sensors

When introducing a **new sensor** into the MINTS system, a few configuration steps are required to ensure the data is properly encoded, transmitted, decoded, and stored.  

In this example, we’ll add a new sensor named **ISG001**, which measures basic environmental parameters.

---

## ⚙️ Step 1: Define the Sensor Structure  

Let’s say your new sensor, **ISG001**, produces the following data fields:

```python
ISG001_payload = (
    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["feelsLike"]).tobytes().hex().zfill(8)
)
```

Each value is converted to bytes (`float32` → 4 bytes) and concatenated to form a hexadecimal payload string.

Before assigning this new sensor, check whether the **sensorID** already exists in  
[`lrSensorAndPortIDs.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/lrSensorAndPortIDs.py).  

If it’s not already defined, assign a **new port ID** (for example, `201`) and update the file accordingly.

---

## 🧱 Step 2: Create a Transmitter Script  

1. Duplicate the existing **BME280** transmitter as a starting point:  

   ```bash
   cp bme280Transmitter.py isg001Transmitter.py
   ```

2. Modify `isg001Transmitter.py` to use your new **ISG001** sensor definition (as shown above), and then run it:

   ```bash
   python3 isg001Transmitter.py
   ```
At this point, the new **sensorID** will not yet appear in **InfluxDB**, since it hasn’t been registered in the **Node-RED workflow** for decoding and data routing.
---

## 🧩 Step 3: Configure Node-RED  

Open the **Node-RED** interface and navigate to the **LoRa Node → InfluxDB** tab.  

<img width="2293" height="1328" alt="screenshot-mdash-circ-utdallas-edu-1880-2025-10-08-16-23-41" src="https://github.com/user-attachments/assets/ccb7663e-c33d-4d2b-9387-bd44d2b69b03" />

1. **Update the LoRaSummaryWrite function**  
   Add the new Sensor ID and Port ID mapping:  

   ```python
   201: "ISG001"
   ```

2. **Modify the sensorIDCheck switch node**  
   Double-click on it and add an entry for your new sensor.  

   <img width="2293" height="1328" alt="image" src="https://github.com/user-attachments/assets/e2050311-f2f5-4633-a3eb-5186635d543f" />

3. **Duplicate an existing “Unpack” function**  
   Copy one unpack node, paste it, rename it (e.g., `ISG001 Unpack V2`), and update its decoding logic for your fields.  

   <img width="2293" height="1328" alt="image" src="https://github.com/user-attachments/assets/cf835f88-4e17-414f-8115-1f4192b51cff" />

4. **Reconnect workflow links**  
   Link the new unpack node between:
   - The `sensorIDCheck` switch node → your `ISG001 Unpack V2`
   - Your `ISG001 Unpack` → `Set Device Name for MINTS Nodes`

   <img width="2293" height="1328" alt="image" src="https://github.com/user-attachments/assets/2e24c650-e8f3-4434-9806-dc79c006af78" />

5. **Deploy** the updated flow to apply the changes.

---

## 🗂️ Step 4: Export and Commit the Updated Node-RED Flow  

Export your current Node-RED instance to keep the configuration synced with the cloud version.  

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/72577695-9c23-4618-8496-1010fcb86ca4" />

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/d7e0084c-e3dd-4ac9-a9cb-cab9d072f20e" />

Select **All Flows** and click **Download**.  

Then upload the downloaded file to the Node-RED Docker folder in the  
[`AirQualityAnalysisWorkflows`](https://github.com/mi3nts/AirQualityAnalysisWorkflows/tree/main/influxdb/nodered-docker) repository.

---

## ☁️ Step 5: Update the Cloud Server (MDASH)

### Log in to MDASH via SSH

```bash
ssh jxw190004@mdash.circ.utdallas.edu
```

> ⚠️ Make sure you have SSH access configured.

---

### Pull the Latest Repository Updates  

```bash
cd AirQualityAnalysisWorkflows/
git pull
```

---

### Restart the Node-RED Container  

Go to the InfluxDB directory and list running containers:

```bash
cd influxdb
podman container ls
```

You’ll see output similar to:

```bash
CONTAINER ID  IMAGE                            COMMAND  STATUS           PORTS
33bad6576ec5  localhost/mints-nodered:latest            Up 2 months ago  0.0.0.0:1880->1880/tcp
```

Stop and remove the **Node-RED** container only (leave InfluxDB running):

```bash
podman stop 33bad6576ec5
podman rm 33bad6576ec5
```

Then rebuild and restart:

```bash
podman-compose up --build -d
```

---

### Exit the Server  

```bash
exit
```

---

## ✅ Step 6: Verify Data  

Finally, rerun your transmitter:

```bash
python3 isg001Transmitter.py
```

Confirm that the new **ISG001** sensor data is appearing correctly in **InfluxDB**.  

At this point, your new sensor is fully registered in the MINTS IoT workflow.  
