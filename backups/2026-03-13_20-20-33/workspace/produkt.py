import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT)
import time
while True:
    if GPIO.input(21):
        print("BUTTON PRESSED")
        GPIO.output(22, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(22, GPIO.LOW)
