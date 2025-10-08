# LR MQTT Pipeline

## Overview

This section demonstrates how LoRa Nodes are initially registered on ChirpStack. We’ll start by exploring a test node setup, running a sensor script, and understanding how to retrieve essential identifiers from a LoRaWAN radio.

---

## Step 1: Log In and Access the Test Node

1. **Log in** to the test node.  
2. **Open a new shell** and navigate to the GitHub repository folder:

```bash
su teamlary
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
```

The `LRNodes` directory contains a representative codebase for operating **LoRa (LR) Nodes** on single-board computers (SBCs) that are connected to LoRaWAN radios.  
Inspect the file [loRaTransmitter.py](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/loRaTransmitter.py)—this script provides a basic implementation of a LoRaWAN transmission.

---

## Step 2: Run the Test Sensor Script

Execute the script:

```bash
python3 loRaTransmitter.py
```

From the information it provides, note down the **DevEUI** we need to register this device.  
Then, fill out [this document](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624) with the **Device EUI**.  
Next, you’ll need to generate a unique **AppKey**. The default key shown by the script should never be reused.

---

## Step 3: Run Key Generator

Execute the script:

```bash
python3 keyGenerator.py
```

Copy the generated **AppKey** and add it to the *App Key* column for the corresponding device entry in [this document](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624).  
We’ll now use this information to register the node on [ChirpStack](http://lora-large-1.trecis.cloud:18083/#/login).

---

## Step 4: Log into ChirpStack

Using the provided credentials, log in to the [MINTS ChirpStack server](http://lora-large-1.trecis.cloud:18083/#/login).  
After logging in, select the **UTD Organization**.

<img width="1140" height="620" alt="image" src="https://github.com/user-attachments/assets/3f37c4e4-0c6a-4491-b57b-049726592844" />

---

## Step 5: Getting to the MINTS Application

Navigate to the **MINTS Application**.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/742e8243-5596-44b3-ac85-3ecca848bc82" />
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c569c25b-eaf7-4597-846b-a6c4d936d747" />

---

## Step 6: Create a New LoRaWAN Node on ChirpStack

Click **+ Create** to add a new device.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/0e4c6f49-0107-4c7f-bf03-7377c06842fc" />

Fill in the device details using the information from the Google Sheet:

- **Device Name:** Device Name  
- **Device Description:** Device Description  
- **Device EUI:** Device EUI  
- **Device Profile:** Mints LoRa Node  

Click **Create Device**.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c362ca51-8ac5-4363-a467-ff764c63db30" />

Finally, enter the **AppKey** and click **Set Device Keys**.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/a383fd7b-b7fd-444b-bea0-eb66b02bb83e" />

Now the node is registered on ChirpStack. Return to the test node and add the generated key to the device.

---

## Step 7: Add the AppKey to Your Device

On the node, navigate to the credentials directory and modify the file `keys.yaml`:

```bash
su teamlary
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/
```

Update the file as follows:

```yaml
appKey: 85BE2704E7B45DAD0E25B587CAE26389
```

---

## Step 8: Run the Example File

Here we simulate a mock LoRaWAN node with a BME280 sensor.

```bash
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
python3 loRaTransmitter.py
```

Check that the **AppKey** in the output matches the updated one.

---

## Step 9: Confirm LoRaWAN Transmission on ChirpStack

To verify that data is being transmitted via LoRaWAN, return to ChirpStack.

1. Navigate to the newly created device under **UTD Organization → MINTS Application**.  
2. Click on the device name to open its details.

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/fe3e73ba-b1f2-4048-a0af-0d4d95d0ec30" />

Now click on **LoRaWAN Frames**.

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/a8b8878f-282e-43b2-aacf-0adbffc6f974" />

You should now see updated packets — for example, data from **FPort 21** corresponds to the **BME280** sensor.

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/00c60d77-779e-4029-a422-9271bf6bfbf6" />

---

✅ **You have successfully registered and verified a LoRa Node within the MINTS LoRaWAN MQTT Pipeline.**
