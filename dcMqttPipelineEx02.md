# Registering Nodes within the Air Quality Analysis Workflow

To ensure data from a new node is correctly stored in the InfluxDB, the node must first be **registered** in the workflow. This involves adding its information to the node lookup table and then updating and restarting the workflow environment.

---

## Step 1: Add the Node to the Lookup Table

Each node in the Air Quality Analysis Workflow is registered in the [`id_lookup.csv`](https://github.com/mi3nts/AirQualityAnalysisWorkflows/blob/main/influxdb/nodered-docker/id_lookup.csv) file.  
To register a new node, open this file in the GitHub repository and append a new line with the node’s details:

```csv
abcdefg000001,Guide Node 00,Guide Node,C4,1,,,,,
```

**Field meanings:**
- **Node ID:** `abcdefg000001`  
- **Node Name:** `Guide Node 00`  
- **Node Type:** `Guide Node`  
- **Device in Use:** `C4`  
- **Currently Active:** `1` (where `1 = True`, `0 = False`)

Once this entry is added and committed, proceed to update the cloud workflow.

---

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

Finally, rerun the `bme280Reader.py` script on your test node and confirm that data from the new node name is appearing in InfluxDB.

In the next section, Registering New Sensors, we’ll learn how to add brand-new sensors to the data pipeline.

