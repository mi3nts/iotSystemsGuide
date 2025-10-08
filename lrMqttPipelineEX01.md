# LR MQTT Pipeline

## Overview

This section walks through how **LoRa Nodes** are registered on **ChirpStack**.  
You’ll start with a test node, run a sensor script, and extract the LoRaWAN identifiers required to onboard the device to the network.

---

## Step 1 — Log In and Access the Test Node

1. **Log in** to the test node.  
2. **Open a new shell** and navigate to the firmware repository:

   ```bash
   su teamlary
   cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
   ```

The `LRNodes` directory contains the standard firmware used to operate **LoRa-enabled single-board computers (SBCs)** connected to LoRaWAN radios.  
Inspect [`loRaTransmitter.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/loRaTransmitter.py) — it demonstrates a basic LoRaWAN transmission implementation.

---

## Step 2 — Run the Test Sensor Script

Execute the script:

```bash
python3 loRaTransmitter.py
```

Note the **DevEUI** displayed — this uniquely identifies your LoRa radio.  
Record it in the [Device Registration Sheet](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624).  

Next, you’ll generate a **unique AppKey** (never reuse the default).

---

## Step 3 — Generate an AppKey

Run the key generator:

```bash
python3 keyGenerator.py
```

Copy the generated **AppKey** and add it to the *App Key* column for your node in the same [registration sheet](https://docs.google.com/spreadsheets/d/1U0VD041rJ3S-aX6ppIM6UB19qCoV30vYpKZ7y9Bi0ps/edit?gid=991573624#gid=991573624).  
This key will be used when registering the device on **ChirpStack**.

---

## Step 4 — Log in to ChirpStack

Visit the [MINTS ChirpStack server](http://lora-large-1.trecis.cloud:18083/#/login) and sign in using your provided credentials.  
After login, select the **UTD Organization**.  

<img width="1140" height="620" alt="image" src="https://github.com/user-attachments/assets/3f37c4e4-0c6a-4491-b57b-049726592844" />

---

## Step 5 — Access the MINTS Application

Navigate to the **MINTS Application** workspace within ChirpStack.  

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/742e8243-5596-44b3-ac85-3ecca848bc82" />
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c569c25b-eaf7-4597-846b-a6c4d936d747" />

---

## Step 6 — Create a New LoRaWAN Device

1. Click **“+ Create”**.  
2. Fill in the device details (from the Google Sheet):

   | Field | Example |
   |--------|----------|
   | **Device Name** | `Guide Node 00` |
   | **Description** | `LoRa test unit` |
   | **Device EUI** | (from script output) |
   | **Device Profile** | `MINTS LoRa Node` |

   Then click **Create Device**.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/0e4c6f49-0107-4c7f-bf03-7377c06842fc" />
<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/c362ca51-8ac5-4363-a467-ff764c63db30" />

3. Open the **Keys** tab and enter your **AppKey**, then select **Set Device Keys**.

<img width="4110" height="2394" alt="image" src="https://github.com/user-attachments/assets/a383fd7b-b7fd-444b-bea0-eb66b02bb83e" />

Your device is now registered on **ChirpStack**.

---

## Step 7 — Add the AppKey to Your Device

On your test node:

```bash
su teamlary
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/
```

Edit `keys.yaml` and update the `appKey` entry:

```yaml
appKey: 85BE2704E7B45DAD0E25B587CAE26389
```

---

## Step 8 — Run the Example Transmitter

Simulate a BME280 LoRaWAN node:

```bash
cd /home/teamlary/gitHubRepos/iotSystemsGuide/LRNodes/firmware/xu4LoRa/
python3 loRaTransmitter.py
```

Verify that the output now displays the correct **AppKey**.

---

## Step 9 — Confirm Transmission on ChirpStack

In **ChirpStack**, navigate to your device (under *UTD Organization → MINTS Application*).  

1. Open **LoRaWAN Frames**.  
2. Observe the latest uplink packets.  
   - Data from **FPort 21** corresponds to the **BME280** sensor.  

<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/fe3e73ba-b1f2-4048-a0af-0d4d95d0ec30" />
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/a8b8878f-282e-43b2-aacf-0adbffc6f974" />
<img width="1147" height="620" alt="image" src="https://github.com/user-attachments/assets/00c60d77-779e-4029-a422-9271bf6bfbf6" />

---

✅ **You’ve successfully registered and verified a LoRa Node on Chirpstack.**


