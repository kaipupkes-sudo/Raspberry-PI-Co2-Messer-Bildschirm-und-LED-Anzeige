import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

input_GPIO = 21
output_GPIO = 22

GPIO.setup(input_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_GPIO, GPIO.OUT)

while True:
    if GPIO.input(input_GPIO):
        print("BUTTON PRESSED")
        GPIO.output(output_GPIO, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(output_GPIO, GPIO.LOW)