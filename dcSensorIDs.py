from collections import OrderedDict

APDS9002 = OrderedDict([
    ("luminance", None),
    ("voltage", None),
    ("raw", None)
])

AS3935 = OrderedDict([
    ("source", None),
    ("energy", None),
    ("distance", None)
])

AS7262 = OrderedDict([
    ("temperature", None),
    ("violetPre", None),
    ("bluePre", None),
    ("greenPre", None),
    ("yellowPre", None),
    ("orangePre", None),
    ("redPre", None),
    ("violetCalibrated", None),
    ("blueCalibrated", None),
    ("greenCalibrated", None),
    ("yellowCalibrated", None),
    ("orangeCalibrated", None),
    ("redCalibrated", None)
])

BME280 = OrderedDict([
    ("temperature", None),
    ("pressure", None),
    ("humidity", None),
    ("altitude", None)
])

BME280V3 = OrderedDict([
    ("temperature", None),
    ("pressure", None),
    ("humidity", None),
    ("dewPoint", None),
    ("altitude", None)
])

BME680 = OrderedDict([
    ("temperature", None),
    ("pressure", None),
    ("humidity", None),
    ("gas", None)
])

BMP280 = OrderedDict([
    ("temperature", None),
    ("pressure", None)
])

BNO080 = OrderedDict([
    ("accelerationX", None),
    ("accelerationY", None),
    ("accelerationZ", None),
    ("linearAccelerationX", None),
    ("linearAccelerationY", None),
    ("linearAccelerationZ", None),
    ("angularVelocityX", None),
    ("angularVelocityY", None),
    ("angularVelocityZ", None),
    ("magneticFluxDensityX", None),
    ("magneticFluxDensityY", None),
    ("magneticFluxDensityZ", None),
    ("quaternionI", None),
    ("quaternionJ", None),
    ("quaternionK", None),
    ("quaternionReal", None),
    ("heading", None),
    ("steps", None),
    ("shake", None),
    ("mostLikelyIndex", None),
    ("mostLikelyConfidence", None),
    ("unknown", None),
    ("inVehicle", None),
    ("onBicycle", None),
    ("onFoot", None),
    ("still", None),
    ("tilting", None),
    ("walking", None),
    ("running", None),
    ("onStairs", None)
])

BNO080V2 = OrderedDict([
    ("accelerationX", None),
    ("accelerationY", None),
    ("accelerationZ", None),
    ("angularVelocityX", None),
    ("angularVelocityY", None),
    ("angularVelocityZ", None),
    ("quaternionI", None),
    ("quaternionJ", None),
    ("quaternionK", None),
    ("quaternionReal", None),
    ("heading", None)
])

CHT8305C = OrderedDict([
    ("temperature", None),
    ("humidity", None),
    ("dewPoint", None)
])

COZIRAEH2000 = OrderedDict([
    ("co2Recent", None),
    ("co2Filtered", None),
    ("temperature", None),
    ("humidity", None)
])

GL001 = OrderedDict([
    ("lightLevel", None)
])

GPSGPGGA = OrderedDict([
    ("timestamp", None),
    ("latitude", None),
    ("latitudeDirection", None),
    ("longitude", None),
    ("longitudeDirection", None),
    ("gpsQuality", None),
    ("numberOfSatellites", None),
    ("HorizontalDilution", None),
    ("altitude", None),
    ("altitudeUnits", None),
    ("undulation", None),
    ("undulationUnits", None),
    ("age", None),
    ("stationID", None)
])

GPSGPGGA2 = OrderedDict([
    ("timestamp", None),
    ("latitudeCoordinate", None),
    ("longitudeCoordinate", None),
    ("latitude", None),
    ("latitudeDirection", None),
    ("longitude", None),
    ("longitudeDirection", None),
    ("gpsQuality", None),
    ("numberOfSatellites", None),
    ("HorizontalDilution", None),
    ("altitude", None),
    ("altitudeUnits", None),
    ("undulation", None),
    ("undulationUnits", None),
    ("age", None),
    ("stationID", None)
])

GPSGPRMC = OrderedDict([
    ("timestamp", None),
    ("status", None),
    ("latitude", None),
    ("latitudeDirection", None),
    ("longitude", None),
    ("longitudeDirection", None),
    ("speedOverGround", None),
    ("trueCourse", None),
    ("dateStamp", None),
    ("magVariation", None),
    ("magVariationDirection", None)
])

GPSGPRMC2 = OrderedDict([
    ("timestamp", None),
    ("status", None),
    ("latitudeCoordinate", None),
    ("longitudeCoordinate", None),
    ("latitude", None),
    ("latitudeDirection", None),
    ("longitude", None),
    ("longitudeDirection", None),
    ("speedOverGround", None),
    ("trueCourse", None),
    ("dateStamp", None),
    ("magVariation", None),
    ("magVariationDirection", None)
])

GUV001 = OrderedDict([
    ("uvLevel", None)
])

HCHDT = OrderedDict([
    ("heading", None),
    ("HID", None),
    ("checkSum", None)
])

HM3301 = OrderedDict([
    ("pm1", None),
    ("pm2_5", None),
    ("pm10", None)
])

HTU21D = OrderedDict([
    ("temperature", None),
    ("humidity", None)
])

ICM20948 = OrderedDict([
    ("accelerationX", None),
    ("accelerationY", None),
    ("accelerationZ", None),
    ("angularVelocityX", None),
    ("angularVelocityY", None),
    ("angularVelocityZ", None),
    ("magneticFluxDensityX", None),
    ("magneticFluxDensityY", None),
    ("magneticFluxDensityZ", None)
])

INA219 = OrderedDict([
    ("shuntVoltage", None),
    ("busVoltage", None),
    ("currentMA", None),
    ("powerMW", None),
    ("loadVoltage", None)
])

IPS7100 = OrderedDict([
    ("pc0_1", None),
    ("pc0_3", None),
    ("pc0_5", None),
    ("pc1_0", None),
    ("pc2_5", None),
    ("pc5_0", None),
    ("pc10_0", None),
    ("pm0_1", None),
    ("pm0_3", None),
    ("pm0_5", None),
    ("pm1_0", None),
    ("pm2_5", None),
    ("pm5_0", None),
    ("pm10_0", None)
])

LIBRAD = OrderedDict([
    ("countPerMinute", None),
    ("radiationValue", None),
    ("timeSpent", None),
    ("LIBRADCount", None)
])

MGS001 = OrderedDict([
    ("nh3", None),
    ("co", None),
    ("no2", None),
    ("c3h8", None),
    ("c4h10", None),
    ("ch4", None),
    ("h2", None),
    ("c2h5oh", None)
])

OPCN2 = OrderedDict([
    ("valid", None),
    ("binCount0", None),
    ("binCount1", None),
    ("binCount2", None),
    ("binCount3", None),
    ("binCount4", None),
    ("binCount5", None),
    ("binCount6", None),
    ("binCount7", None),
    ("binCount8", None),
    ("binCount9", None),
    ("binCount10", None),
    ("binCount11", None),
    ("binCount12", None),
    ("binCount13", None),
    ("binCount14", None),
    ("binCount15", None),
    ("bin1TimeToCross", None),
    ("bin3TimeToCross", None),
    ("bin5TimeToCross", None),
    ("bin7TimeToCross", None),
    ("sampleFlowRate", None),
    ("temperatureOrPressure", None),
    ("samplingPeriod", None),
    ("checkSum", None),
    ("pm1", None),
    ("pm2_5", None),
    ("pm10", None)
])

OPCN3 = OrderedDict([
    ("valid", None),
    ("binCount0", None),
    ("binCount1", None),
    ("binCount2", None),
    ("binCount3", None),
    ("binCount4", None),
    ("binCount5", None),
    ("binCount6", None),
    ("binCount7", None),
    ("binCount8", None),
    ("binCount9", None),
    ("binCount10", None),
    ("binCount11", None),
    ("binCount12", None),
    ("binCount13", None),
    ("binCount14", None),
    ("binCount15", None),
    ("binCount16", None),
    ("binCount17", None),
    ("binCount18", None),
    ("binCount19", None),
    ("binCount20", None),
    ("binCount21", None),
    ("binCount22", None),
    ("binCount23", None),
    ("bin1TimeToCross", None),
    ("bin3TimeToCross", None),
    ("bin5TimeToCross", None),
    ("bin7TimeToCross", None),
    ("samplingPeriod", None),
    ("sampleFlowRate", None),
    ("temperature", None),
    ("humidity", None),
    ("pm1", None),
    ("pm2_5", None),
    ("pm10", None),
    ("rejectCountGlitch", None),
    ("rejectCountLongTOF", None),
    ("rejectCountRatio", None),
    ("rejectCountOutOfRange", None),
    ("fanRevCount", None),
    ("laserStatus", None),
    ("checkSum", None)
])

PPD42NS = OrderedDict([
    ("lowPulseOccupancy", None),
    ("concentration", None),
    ("ratio", None),
    ("timeSpent", None)
])

PPD42NSDuo = OrderedDict([
    ("sampleTimeSeconds", None),
    ("LPOPmMid", None),
    ("LPOPm10", None),
    ("ratioPmMid", None),
    ("ratioPm10", None),
    ("concentrationPmMid", None),
    ("concentrationPm2_5", None),
    ("concentrationPm10", None)
])

QLMRAD001 = OrderedDict([
    ("event", None)
])

RG15 = OrderedDict([
    ("accumulation", None),
    ("eventAccumulation", None),
    ("totalAccumulation", None),
    ("rainPerInterval", None)
])

SCD30 = OrderedDict([
    ("c02", None),
    ("temperature", None),
    ("humidity", None)
])

SCD30V2 = OrderedDict([
    ("co2", None),
    ("temperature", None),
    ("humidity", None)
])

SEN0232 = OrderedDict([
    ("rawAnalog", None),
    ("rawVoltage", None),
    ("dB", None)
])

SI114X = OrderedDict([
    ("visible", None),
    ("ir", None),
    ("uv", None),
    ("proximity1", None),
    ("proximity2", None),
    ("proximity3", None)
])

TMP117 = OrderedDict([
    ("temperature", None)
])

TMG3993 = OrderedDict([
    ("infraRed", None),
    ("red", None),
    ("green", None),
    ("blue", None),
    ("proximity", None)
])

TSL2591 = OrderedDict([
    ("luminosity", None),
    ("ir", None),
    ("full", None),
    ("visible", None),
    ("lux", None)
])

VEML6070 = OrderedDict([
    ("UVLightLevel", None)
])

VEML6075 = OrderedDict([
    ("rawUVA", None),
    ("rawUVB", None),
    ("visibleCompensation", None),
    ("irCompensation", None),
    ("uva", None),
    ("uvb", None),
    ("index", None)
])

WIMDA = OrderedDict([
    ("barrometricPressureMercury", None),
    ("BPMUnits", None),
    ("barrometricPressureBars", None),
    ("BPBUnits", None),
    ("airTemperature", None),
    ("ATUnits", None),
    ("waterTemperature", None),
    ("WTUnits", None),
    ("relativeHumidity", None),
    ("absoluteHumidity", None),
    ("dewPoint", None),
    ("DPUnits", None),
    ("windDirectionTrue", None),
    ("WDTUnits", None),
    ("windDirectionMagnetic", None),
    ("WDMUnits", None),
    ("windSpeedKnots", None),
    ("WSKUnits", None),
    ("windSpeedMetersPerSecond", None),
    ("WSMPSUnits", None),
    ("checkSum", None)
])

WIMWV = OrderedDict([
    ("windAngle", None),
    ("WAReference", None),
    ("windSpeed", None),
    ("WSUnits", None),
    ("status", None),
    ("checkSum", None)
])

YXXDR = OrderedDict([
    ("angularDisplacement", None),
    ("pitch", None),
    ("degrees", None),
    ("pitchOfVessel", None),
    ("angularDisplacement", None),
    ("roll", None),
    ("degrees2", None),
    ("rollOfvessel", None)
])
