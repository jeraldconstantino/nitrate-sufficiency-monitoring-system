# import RPi.GPIO as GPIO
# from time import sleep

def feedNow():
    pass
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)

    # RELAY_PIN = 20
    # STOP_SENSOR_PIN = 21
    # DELAY = 1

    # GPIO.setup(RELAY_PIN, GPIO.OUT)
    # GPIO.setup(STOP_SENSOR_PIN, GPIO.IN)

    # GPIO.output(RELAY_PIN, GPIO.LOW) 
    # try:
    #     GPIO.output(RELAY_PIN, GPIO.HIGH)
            
    #     while True:
    #         state = GPIO.input(STOP_SENSOR_PIN)
    #         print(state)
                
    #         if state == GPIO.HIGH:
    #             sleep(DELAY)
    #             GPIO.output(RELAY_PIN, GPIO.LOW)
    #             break
    # finally:
    #     GPIO.cleanup()
