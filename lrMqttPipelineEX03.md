# Understanding LoRaWAN Sensor Data

At this stage, we look at how we send out **raw sensor data** through a LoRaWAN radio.  
Please **inspect the file [`loraTransmitter.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/loRaTransmitter.py)** carefully and try to understand how it works.  

When working with LoRa nodes, sensor fields must be converted into **bytes (or bits)** before being transmitted.  
As you saw earlier, each `sensorID` is mapped to an **FPort** field, and these mappings are defined in the [portIDs.yml](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/portIDs.yml) file.  

For example, you can clearly see that the **BME280** sensor is mapped to **FPort 21**.

---

# Understanding LoRaWAN Raw Data Transmission

## Overview

This section explains how sensor data is prepared and transmitted as raw bytes in the **LoRaWAN** communication process.  
Since LoRa cannot directly send text or dictionary data, values are converted to **binary (byte)** format before being sent.

---

## ⚙️ 1. Mapping Sensors to FPorts

Each **sensor type (sensorID)** is assigned a unique **FPort** number.  
This mapping is defined in the [portIDs.yml](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/portIDs.yml) file.

So when the sensorID is `"BME280"`, it will transmit on **FPort 21**.  
This tells **ChirpStack** or the application server which decoder to use for that packet.

Example code:
```python
sensorID = "BME280"
port = mPL.deriveSensorStats(sensorID)
```

This line retrieves the correct FPort for the BME280 sensor. The Current Set of LoRaWAN Sensor and Port IDs are given [here](https://github.com/mi3nts/iotSystemsGuide/blob/main/lrSensorAndPortIDs.py).

---

## 🌡️ 2. Creating the Sensor Data Dictionary

Each sensor produces readings that are stored as key-value pairs.  
For example, a **BME280** provides four values:

```python
sensorDictionary = OrderedDict([
    ("temperature", 28.40),
    ("pressure", 98651.00),
    ("humidity", 38.00),
    ("altitude", 225.01)
])
```

⚠️ **Important:** The **order of fields must remain exactly the same** between transmission and decoding.  
LoRaWAN packets are position-based — the receiving end decodes values in the same sequence they were encoded.

---

## 💾 3. Converting Data to Bytes and Hex Strings

LoRaWAN transmits **binary data**, not human-readable text.  
Each float value must be converted into bytes and then to hexadecimal strings for transmission.

### Step 1 — Convert to Bytes

Each floating-point value is converted into **4 raw bytes** using NumPy’s `tobytes()` method:
```python
byteData = np.float32(sensorDictionary["temperature"]).tobytes()
```

Example:
```
b'\xcd\xcc\x8cA'
```
Each `\x..` represents one byte in hexadecimal form.

### Step 2 — Convert Bytes to Hexadecimal String

The bytes are then converted into a **hex string** using `.hex()`:
```python
hexData = byteData.hex()
```

Example output:
```
cdcc8c41
```

This hex string represents the same 4 bytes in a compact, printable format.  
Each pair of hex characters (e.g., `cd`, `cc`, `8c`, `41`) equals one byte.

### Step 3 — Combine and Pad Hex Strings

To ensure consistent byte lengths, `.zfill(8)` is applied.  
Then, all fields are concatenated — **in the same order** — to form a **16-byte payload**:

```python
hexStr  =     np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8)
```

Example output:
```
HEX STRING:
cdcccc41 00e0c07a 0000b241 0000e343
```

This hexadecimal string is the final **LoRa payload**.

---

## 📡 4. Sending via LoRa

The hex payload is sent out through the **LoRa transmitter** using the mapped **FPort (e.g., 21)**.  
The **gateway** receives it and forwards it to **ChirpStack**, which decodes it using the same field order and mapping logic.

---







