
import datetime
import time
import RPi.GPIO as GPIO
try:
	from smbus import SmBus
except ImportError:
	from smbus import SMBus
from bme280 import BME280

# Initialise the BME280
print("initializing service script")
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

dataFile = open("/opt/data/weatherData.csv", "a")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# define global variables

temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()
wind_speed = 0.00000000000000000

def read_wind():
	global wind_speed
	last_state = 0;
	last_switch = 0;
	last_imp_time = 0;
	measure_duration = 10 #seconds
	impulses = 0
	measure_time= time.time()
 
	while True:
		if(time.time() - measure_time >= measure_duration):
			break;
		state = GPIO.input(8)
		if(state != last_state):
			last_state = state
			if(state==1):
				impulses +=1
		
	if(impulses	== 1.0):
		wind_speed = 0
	else:	
		wind_speed=0.0182648401826484*impulses+0.633789954337898 # in m/s
		
def read_instant_data():
	global temperature
	global pressure
	global humidity
	
	temperature = bme280.get_temperature()
	pressure = bme280.get_pressure()
	humidity = bme280.get_humidity()
	
	#print ("read temps " + str(temperature))

def write_data_to_file():
	global temperature
	global pressure
	global humidity
	global wind_speed
	
	dataFile.write("\n"+'{:05.2f},{:05.2f},{:05.2f},{},{},{:05.5f}'.format(temperature, pressure, humidity, datetime.datetime.now(), GPIO.input(19), wind_speed))
	#rint("wrote data")	
	
while True:
	read_wind()
	read_instant_data()
	write_data_to_file()
	print("measure cycle finished at " + str(datetime.datetime.now()))
	time.sleep(590)

