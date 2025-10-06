# DC Rsyc Pipeline

A seperate pdf is provided with log in links and passwords. 


## EX 1
- Loginto our test node
- Open a new shell and naviagate into github repos folder
  ```
  su teamlary
  cd /home/teamlary/gitHubRepos/iotSystemsGuide/DCNodes/firmware/xu4Mqtt/
  ```

The DCNodes folder contains a typical codebase we use to operate DC Nodes on a SBC. At this point please inspect the [file](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/bme280Reader.py) named `bme280Reader.py`. This mimics an actual implementation of a climate sensor we use on live nodes.  

- Now you can run this file.
```
python3 bme280Reader.py
```
Check where the data is been saved. Whenever you want to add a new sensor to a unit use the function named `sensorFinisher` with the appropriate sensor dictionary. The current set of sensors and there respective sensor dictionaries can be found at this link. Make sure you match the ordering as well as the appropriatte units if you are using a previously used sensor. 

## Registering DC Nodes on the Rsync Pipeline

RSYNC basically works ssh keys. The data needs to end up at our IMD data server. Hence initially we need to add an ssh key to our node. 

- Add an SSH Key: `ssh-keygen`
- Copy the SSH Public Key
- Log in to IMD and paste the ssh Key in autherized keys.
  **Make sure you already have access to IMD.**
  ``` ssh mints@mintsdata.utdallas.edu -p 2222 ```
  - Add the node key to autherized keys file.
    ```
    cd .ssh
    vim authorized_keys
    ```
- Come back to the node and check weather the node has access to rsync.
  ``` ssh mints@mintsdata.utdallas.edu -p 2222 ```
- Sync your data into IMD
```rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw```
Also now check if the  recently synced data is available in IMD
- Now to sync the data each minute add the following line to the nodes crontab.
  ```* * * * * rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw```


  

  








