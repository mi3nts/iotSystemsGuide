# Understanding LoRaWAN Raw Data Transmission

## Overview

This section explains how sensor data is prepared and transmitted as raw bytes in the **LoRaWAN** communication process. Since LoRa cannot directly send text or dictionary data, values are converted to **binary (byte)** format before being sent.

---

## ⚙️ 1. Mapping Sensors to FPorts

Each **sensor type (sensorID)** is assigned a unique **FPort** number.  
This mapping is defined in the [portIDs.yml](https://github.com/mi3nts/iotSystemsGuide/blob/main/LRNodes/firmware/xu4LoRa/mintsXU4/credentials/portIDs.yml) file.

Example mapping:
```yaml
BME280: 21
```

So when the sensorID is `"BME280"`, it will transmit on **FPort 21**. This tells **ChirpStack** or the application server which decoder to use for that packet.

Example code:
```python
sensorID = "BME280"
port = mPL.deriveSensorStats(sensorID)
```

This line retrieves the correct FPort for the BME280 sensor.

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

All values are stored as **float32** to ensure consistent 4-byte encoding.

---

## 💾 3. Converting Data to Bytes

LoRaWAN requires binary data transmission.  
Each float value is converted into bytes using **NumPy**:

```python
hexStr  =     np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +     np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8)

```

### Explanation
- `np.float32(...).tobytes()` → converts a float to 4 raw bytes.  
- `.hex()` → turns those bytes into hexadecimal form.  
- `.zfill(8)` → ensures every value is 8 hex characters (4 bytes).  
- Concatenating them produces a continuous **16-byte payload** (4 floats × 4 bytes each).

Example output:
```
HEX STRING:
cdcccc41 00e0c07a 0000b241 0000e343
```

This hexadecimal string is the final **LoRa payload**.

---

## 📡 4. Sending via LoRa

The hex payload is sent out through the **LoRa transmitter** using the mapped **FPort (e.g., 21)**.  
The **gateway** receives it and forwards it to **ChirpStack**, which then decodes it using the same mapping logic.

---
