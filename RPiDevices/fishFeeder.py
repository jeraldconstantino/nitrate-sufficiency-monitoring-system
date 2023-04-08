# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setWarnings(False)

RELAY_PIN = 21
DELAY = 1

# GPIO.setup(RELAY_PIN, GPIO.OUT)
def feedNow():
    print("FEEDING NOW . . . ")
	# try:
	#     GPIO.output(RELAY_PIN, GPIO.HIGH)
	#     print("Relay 1 ON")
	#     GPIO.output(RELAY_PIN, GPIO.LOW)
	#     print("Relay 1 OFF")

    # finally:
	#     GPIO.cleanup()