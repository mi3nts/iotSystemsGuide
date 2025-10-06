
# Registering Nodes withing the Air Quality Analysis Workflow

As you probably figured out we need to rergister the nodes inorder for the data to to end up on our influx DB.  To start off we need to add the new ID into this [file](https://github.com/mi3nts/AirQualityAnalysisWorkflows/blob/main/influxdb/nodered-docker/id_lookup.csv).
1. Add the following line at the endo of this [file](https://github.com/mi3nts/AirQualityAnalysisWorkflows/blob/main/influxdb/nodered-docker/id_lookup.csv). This can be done on git.
   ```abcdefg000001,Guide Node 00,Guide Node,C4,1,,,,,```
This line represents the following information
- Node ID: abcdefg000001
- Node Name: Guide Node 00
- Node Type: Guide Node
- Device In Use: C4
- Currently Active: 1 represents True.

Once this is added we need to update and reboot our cloud workflow.
2.  Log into mdash from your PC.
```
ssh jxw190004@mdash.circ.utdallas.edu
```
** Again you would need your ssh access** 

3. Navigate and update Air Quality Analysis Workflows
```
cd AirQualityAnalysisWorkflows/
git pull
```

4. Reboot the NodeRed Instance.
```
cd influxdb
podman container ls
```

At this point you will see some thing similat to this.

```
CONTAINER ID  IMAGE                            COMMAND  CREATED       STATUS           PORTS                                                                   NAMES
c3692f3ca93e  k8s.gcr.io/pause:3.2                      3 years ago   Up 3 years ago   0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  06360efbd5a9-infra
cc581152869a  localhost/mints-grafana:latest            4 months ago  Up 4 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_grafana_1
edd6ff8a8e49  localhost/mints-influxdb:latest  influxd  4 months ago  Up 4 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_influxdb_1
33bad6576ec5  localhost/mints-nodered:latest            2 months ago  Up 2 months ago  0.0.0.0:1880->1880/tcp, 0.0.0.0:3000->3000/tcp, 0.0.0.0:8086->8086/tcp  influxdb_nodered_1
```

From here you are making note of the node red Container ID (33bad6576ec5 in this example) and the stoping that service. **At no point you should delete the influx service.** 

To stop and remove the nodered service do the following 

```
podman stop 33bad6576ec5 
podman rm 33bad6576ec5
```

At this point we simply reboot the currently unavailable instances. 
```
podman-compose up --build -d 
```
5. Exit MDASH
```
exit
```

At this point rerun the bme280Reader.py on the test node and check for the data from the new sensor name is available. 



  
