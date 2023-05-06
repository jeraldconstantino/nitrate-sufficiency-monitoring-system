# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BCM)
# GPIO.setWarnings(False)

# RELAY_PIN = 20
# STOP_SENSOR_PIN = 21
# DELAY = 1

# GPIO.setup(RELAY_PIN, GPIO.OUT)
# GPIO.setup(STOP_SENSOR_PIN, GPIO.IN)

def feedNow():
    print("feeding . . .")
	# try:
	# 	GPIO.output(RELAY_PIN, GPIO.LOW)

	# 	while True:
	# 		state = GPIO.input(STOP_SENSOR_PIN)
	# 		if state == GPIO.HIGH:
	# 			sleep(DELAY)
	# 			GPIO.output(RELAY_PIN, GPIO.HIGH)
	# 			break

	# finally:
	# 	GPIO.cleanup()