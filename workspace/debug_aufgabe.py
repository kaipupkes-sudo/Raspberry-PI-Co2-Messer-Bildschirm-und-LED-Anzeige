import RPi.GPIO as GPIO
import time

BUTTON_PIN = 21
LED_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(BUTTON_PIN):
            print("BUTTON PRESSED")
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
    print("unterbrechung durch user")

finally:
    GPIO.cleanup()