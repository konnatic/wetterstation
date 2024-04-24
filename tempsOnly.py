
import datetime
import time
import RPi.GPIO as GPIO
try:
	from smbus import SmBus
except ImportError:
	from smbus import SMBus
from bme280 import BME280

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

while True:
    print(str(bme280.get_temperature() - 5.6))
    time.sleep(1)

