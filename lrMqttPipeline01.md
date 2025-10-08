# LR MQTT Pipeline

## Overview

This section demonstrates how LoRa Nodes are initially registed on Chirpstack. We’ll start by exploring a test node setup, running a sensor script, and understanding how we can gain the necessary information you need from a LoRaWAN radio. 

---

## Step 1: Log In and Access the Test Node

1. **Log in** to the test node.
2. **Open a new shell** and navigate to the GitHub repository folder:

 ```bash
 su teamlary
 cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
 ```

The `LRNodes` directory contains a representative codebase for operating **LoRa (LR) Nodes** on single-board computers (SBCs) which are connected to LoRaWAN Radios.
Inspect the file [loraTransmitter.py](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/loRaTransmitter.py)— this script provides a basic implementation of a lorawan implimentation. 

---

## Step 2: Run the Test Sensor Script
Execute the script:

```bash
python3 loRaTransmitter.py
```

From the information it provides note down the Dev EUI we need to register this device. At this point please fill out [this document](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624) with the Device EUI you have. At this point you need to generate a Unique App Key. This can be done using this file. The App key you saw is the app key we have by default, and should never be used. 

---
## Step 3: Run Key Generator
Execute the script:

```bash
python3 keyGenerator.py
```
Using the key that you have fill out the App Key column for the newly created node on [this document](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624). Using this information we try to register the node on [chirpstack](http://lora-large-1.trecis.cloud:18083/#/login).

## Step 4: Log into Chirpstack
Using the provided UN and PW loginto the Mints [Chirpstack ](http://lora-large-1.trecis.cloud:18083/#/login) Log in. After  loging in pick out the UTD Organization.
<img width="1140" height="620" alt="image" src="https://github.com/user-attachments/assets/3f37c4e4-0c6a-4491-b57b-049726592844" />

## Step 5: Getting to the Mints Application
At this point navigate to the Mints Application. 
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/742e8243-5596-44b3-ac85-3ecca848bc82" />
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c569c25b-eaf7-4597-846b-a6c4d936d747" />

## Step 6: Create a new LoRaWAN Node on Chirpstack
Now we are ready to create a new node. Start by pressing the + Create button. 
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/0e4c6f49-0107-4c7f-bf03-7377c06842fc" />
Now fill in the appropriate information from the google sheet for the new node. 
- Device Name: Device Name
- Device Description: Device Description
- Device EUI: Device EUI
- Device Profile: Mints LoRa Node
And then click CREATE DEVICE
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c362ca51-8ac5-4363-a467-ff764c63db30" />

And finally tpe in the Aplication Key and click on set device keys.  
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/a383fd7b-b7fd-444b-bea0-eb66b02bb83e" />

Now we have registered the node in chirpstack. Now come back to the test node and add the generated key to the device. 

## Step 7: Add key into your device 
This can be done by navigating into the credentials folder and modyfying the file named `keys.yaml`. 
```
su teamlary
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/
``` 
On this file add the appropriate key
```
appKey: 85BE2704E7B45DAD0E25B587CAE26389 
```

## Step 8: Running the example file 

Here we are implimenting a mock LoRaWAN Node with a BME280.
```
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
python3 loRaTransmitter.py
```
Also check if the Application Key is now appropriate from the output. 


## Step 9: Confirming LoRaWAN Transmission on Chirpstack
At this point we can check to see if the data is been sent via lorawan through Chirpstack.

From chirpstack, navigate to the newly create sensor under the UTD organization and under the MINTS Application and then click on it. 


<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/fe3e73ba-b1f2-4048-a0af-0d4d95d0ec30" />

Now click on LORAWAN FRAMES
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/a8b8878f-282e-43b2-aacf-0adbffc6f974" />

You can now see the updated data packets from FPORT 21 which maps to the BME280. 
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/00c60d77-779e-4029-a422-9271bf6bfbf6" />

















