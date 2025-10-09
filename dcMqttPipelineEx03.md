# Registering New Sensors

Imagine a case where a brand new sensor is introduced into mints. Lets say this sensor is is called ISG001 and has the following feilds. 

``` python
ISG001 = OrderedDict([
    ("dateTime", str(dateTime)),
    ("temperature", None),
    ("pressure", None),
    ("humidity", None),
    ("feelsLike", None)
])
```
Initially check if this sensorID is already taken using this [file](https://github.com/mi3nts/iotSystemsGuide/blob/main/dcSensorIDs.py). 

1. Create a copy of `bme280reader.py` and name it `isg001Reader.py` on your node.
``` bash
cp bme280Reader.py isg001Reader.py
```
2.  At this point modify `isg001Reader.py` to have a sensor named ISG001 with the appropriate dictinary as suggested above and then run it.
``` bash
python3 isg001Reader.py
```
At this point check if a new sensor ID is visible on influx DB. 
>The sensor data wont be available on influx since the sensor itself is not yet registered in the workflow. The following explains how it can be done. 

3. At this point open the [node red ineterface](http://mdash.circ.utdallas.edu:1880/#flow/b44edfff80da0ecb) and navigate to the central node tab.
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/298f4bf6-98c9-4490-97fd-997dfcd2e537" />

4. Copy and paste a MQTT node + json node connection and paste  it on the silouette
<img width="2293" height="1328" alt="image" src="https://github.com/user-attachments/assets/f38c5b71-1a4c-491a-af6d-bd256465bda4" />

5. Double click on the duplicate MQTT node and then add the ID of the new sensor.
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/a1ff0287-72de-4737-86bf-7c07e39a1383" />

6. Link the new sensor to the  `parse for Mints Data function` and hit deploy.
<img width="2293" height="1328" alt="image" src="https://github.com/user-attachments/assets/7d38a86d-004b-42ea-926a-0a0be384b40d" />

7. Export the current node red instance.
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/72577695-9c23-4618-8496-1010fcb86ca4" />

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/d7e0084c-e3dd-4ac9-a9cb-cab9d072f20e" />
At this point make sure to select **all flows** and hit download. 

8. Upload the downloaded file @ the node red docker [folder](https://github.com/mi3nts/AirQualityAnalysisWorkflows/tree/main/influxdb/nodered-docker) of Air Quality Analysis Workflows.

Now we update the nodered docker as we did in EX02.


## Step 2: Log In to the Cloud Server

Access the **MDASH** server from your PC using SSH:

```bash
ssh jxw190004@mdash.circ.utdallas.edu
```

> ⚠️ You must already have SSH access configured to MDASH.

---

## Step 3: Update the Air Quality Analysis Workflow Repository

After logging in, navigate to the repository and pull the latest updates:

```bash
cd AirQualityAnalysisWorkflows/
git pull
```

---

## Step 4: Restart the Node-RED Instance

Navigate to the `influxdb` folder and list the running containers:

```bash
cd influxdb
podman container ls
```

You should see output similar to this:

```bash
CONTAINER ID  IMAGE                            COMMAND  CREATED       STATUS           PORTS                                                                   NAMES
c3692f3ca93e  k8s.gcr.io/pause:3.2                      3 years ago   Up 3 years ago   0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  06360efbd5a9-infra
cc581152869a  localhost/mints-grafana:latest            4 months ago  Up 4 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_grafana_1
edd6ff8a8e49  localhost/mints-influxdb:latest  influxd  4 months ago  Up 4 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_influxdb_1
33bad6576ec5  localhost/mints-nodered:latest            2 months ago  Up 2 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_nodered_1
```

Locate the **Node-RED container ID** (e.g., `33bad6576ec5`).  
Stop and remove only the Node-RED container — **do not remove the InfluxDB container**.

```bash
podman stop 33bad6576ec5
podman rm 33bad6576ec5
```

Now, rebuild and restart the unavailable containers:

```bash
podman-compose up --build -d
```

---

## Step 5: Exit MDASH

Once the workflow is rebuilt and running, exit the server:

```bash
exit
```

---

## Step 6: Verify Node Data

Finally, rerun the `isg001Reader.py` script on your test node and confirm that data from the new node name is appearing in InfluxDB.

> In the next section, Registering New Sensors, we’ll learn how to add brand-new sensors to the data pipeline.





