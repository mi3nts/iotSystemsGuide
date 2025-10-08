"""
sensorEncodingReference.py
------------------------------------------------------------
MINTS Sensor Encoding Reference
Each section shows how sensor data is encoded into a
hexadecimal string before transmission via LoRaWAN.

Each value is converted to bytes using:
    np.float32(value).tobytes().hex().zfill(8)

⚠️ The field order MUST remain the same between encoding and decoding.
------------------------------------------------------------
"""

import numpy as np


# ============================================================
# 🌈 AS7265X | Port ID: 51
# Fields: channelA410nm → channelL940nm (18 float32)
# ============================================================
AS7265X_payload = (
    np.float32(sensorDictionary["channelA410nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelB435nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelC460nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelD485nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelE510nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelF535nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelG560nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelH585nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelR610nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelI645nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelS680nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelJ705nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelT730nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelU760nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelV810nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelW860nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelK900nm"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["channelL940nm"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🌫️ BME280 | Port ID: 21
# Fields: temperature, pressure, humidity, dewPoint, altitude
# ============================================================
BME280_payload = (
    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["dewPoint"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🌫️ BME688CNR | Port ID: 25
# Fields: temperature, humidity, pressure, vocAqi, bvocEq, gasEst, co2Eq
# ============================================================
BME688CNR_payload = (
    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pressure"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["vocAqi"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["bvocEq"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["gasEst"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["co2Eq"]).tobytes().hex().zfill(8)
)


# ============================================================
# 📍 GPGGAPL | Port ID: 106
# Fields: hour, minute, second, latitude, longitude,
#          gpsQuality, numberOfSatellites,
#          horizontalDilution, altitude, undulation
# ============================================================
GPGGAPL_payload = (
    np.ubyte(sensorDictionary["hour"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["minute"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["second"]).tobytes().hex().zfill(2) +
    np.double(sensorDictionary["latitude"]).tobytes().hex().zfill(16) +
    np.double(sensorDictionary["longitude"]).tobytes().hex().zfill(16) +
    np.ubyte(sensorDictionary["gpsQuality"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["numberOfSatellites"]).tobytes().hex().zfill(2) +
    np.float32(sensorDictionary["horizontalDilution"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["altitude"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["undulation"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🛰️ GPRMCPL | Port ID: 107
# Fields: year, month, day, hour, minute, second,
#          latitude, longitude, speedOverGround
# ============================================================
GPRMCPL_payload = (
    np.uint16(sensorDictionary["year"]).tobytes().hex().zfill(4) +
    np.ubyte(sensorDictionary["month"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["day"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["hour"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["minute"]).tobytes().hex().zfill(2) +
    np.ubyte(sensorDictionary["second"]).tobytes().hex().zfill(2) +
    np.double(sensorDictionary["latitude"]).tobytes().hex().zfill(16) +
    np.double(sensorDictionary["longitude"]).tobytes().hex().zfill(16) +
    np.float32(sensorDictionary["speedOverGround"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🌪️ IPS7100 | Port ID: 15
# Fields: pc0_1, pc0_3, pc0_5, pc1_0, pc2_5, pc5_0, pc10_0,
#         pm0_1, pm0_3, pm0_5, pm1_0, pm2_5, pm5_0, pm10_0
# ============================================================
IPS7100_payload = (
    np.uint32(sensorDictionary["pc0_1"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc0_3"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc0_5"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc1_0"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc2_5"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc5_0"]).tobytes().hex().zfill(8) +
    np.uint32(sensorDictionary["pc10_0"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm0_1"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm0_3"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm0_5"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm1_0"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm2_5"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm5_0"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["pm10_0"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🌪️ IPS7100CNR | Port ID: 17
# Fields: same as IPS7100 (CANAAREE variant)
# ============================================================
IPS7100CNR_payload = IPS7100_payload


# ============================================================
# 🖥️ MacAD | Port ID: 8
# Fields: macAddress (12-character string)
# ============================================================
MacAD_payload = sensorDictionary["macAddress"].zfill(12)


# ============================================================
# 🧠 MBCLR001 | Port ID: 42
# Fields: numOfCalls, label, confidence
# ============================================================
MBCLR001_payload = (
    np.ubyte(sensorDictionary["numOfCalls"]).tobytes().hex().zfill(4) +
    np.uint16(sensorDictionary["label"]).tobytes().hex().zfill(4) +
    np.float32(sensorDictionary["confidence"]).tobytes().hex().zfill(8)
)


# ============================================================
# 🧠 MBCLR002 | Port ID: 43
# Fields: numOfCalls, lag0–lag7, label0–label7, confidence0–confidence7
# ============================================================
MBCLR002_payload = (
    np.ubyte(sensorDictionary["numOfCalls"]).tobytes().hex().zfill(2) +
    ''.join([
        np.uint16(sensorDictionary[f"lag{i}"]).tobytes().hex().zfill(4) +
        np.uint16(sensorDictionary[f"label{i}"]).tobytes().hex().zfill(4) +
        np.float32(sensorDictionary[f"confidence{i}"]).tobytes().hex().zfill(8)
        for i in range(8)
    ])
)


# ============================================================
# ⚙️ PM | Port ID: 2
# Fields: powerMode
# ============================================================
PM_payload = np.ubyte(sensorDictionary["powerMode"]).tobytes().hex().zfill(2)


# ============================================================
# ⚙️ PMPoLo | Port ID: 4
# Fields: powerMode
# ============================================================
PMPoLo_payload = np.ubyte(sensorDictionary["powerMode"]).tobytes().hex().zfill(2)


# ============================================================
# 🌧️ RG15 | Port ID: 61
# Fields: accumulation, eventAccumulation, totalAccumulation, rainPerInterval
# ============================================================
RG15_payload = (
    np.float32(sensorDictionary["accumulation"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["eventAccumulation"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["totalAccumulation"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["rainPerInterval"]).tobytes().hex().zfill(8)
)


# ============================================================
# 💨 SCD30 | Port ID: 33
# Fields: co2, temperature, humidity
# ============================================================
SCD30_payload = (
    np.float32(sensorDictionary["co2"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["temperature"]).tobytes().hex().zfill(8) +
    np.float32(sensorDictionary["humidity"]).tobytes().hex().zfill(8)
)
