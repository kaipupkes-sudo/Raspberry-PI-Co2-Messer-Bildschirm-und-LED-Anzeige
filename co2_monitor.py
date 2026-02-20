#!/usr/bin/env python3
import mh_z19
import time
import RPi.GPIO as GPIO

# GPIO-Pins für LEDs
GREEN_LED = 17
YELLOW_LED = 27
RED_LED = 22

RESET = '\033[0m'
CLEAR = '\033[2J\033[H'

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.setup(RED_LED, GPIO.OUT)
    # Alle LEDs initial aus
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(YELLOW_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)

def control_leds(ppm, blink_state):
    """Steuert LEDs basierend auf CO2-Wert"""
    if ppm < 1000:
        GPIO.output(GREEN_LED, GPIO.HIGH)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        GPIO.output(RED_LED, GPIO.LOW)
    elif ppm < 2000:
        GPIO.output(GREEN_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.HIGH)
        GPIO.output(RED_LED, GPIO.LOW)
    else:
        GPIO.output(GREEN_LED, GPIO.LOW)
        GPIO.output(YELLOW_LED, GPIO.LOW)
        GPIO.output(RED_LED, blink_state)

def get_color(ppm):
    if ppm < 1000:
        return '\033[42m\033[30m'   # Grün
    elif ppm < 2000:
        return '\033[43m\033[30m'   # Gelb
    else:
        return '\033[41m\033[37m'   # Rot

def display(co2, temp):
    color = get_color(co2)
    print(CLEAR)
    print("=" * 40)
    print("      CO2-Monitor (MH-Z19B)")
    print("=" * 40)
    print(f"  Temperatur:  {temp} °C")
    print()
    print(f"  CO2:  {color} {co2} ppm {RESET}")
    print()

    if co2 >= 2000:
        print(f'\033[41m\033[37m  ⚠  Bitte sofort lüften!  ⚠  {RESET}')
    elif co2 >= 1000:
        print("  Luft wird schlechter – lüften empfohlen")
    else:
        print("  Luftqualität: gut")

    print("=" * 40)
    print(f"  Letzte Messung: {time.strftime('%H:%M:%S')}")
    print("=" * 40)

def main():
    print("Starte CO2-Monitor... (Strg+C zum Beenden)")
    setup_gpio()
    time.sleep(1)
    
    co2 = None
    temp = None
    blink_state = GPIO.HIGH
    last_blink = time.time()
    last_read = time.time()

    try:
        while True:
            # Sensor nur alle 5 Sekunden auslesen
            if time.time() - last_read > 5:
                data = mh_z19.read_all()
                co2 = data.get('co2')
                temp = data.get('temperature', '–')
                last_read = time.time()
                
                if co2 is not None:
                    display(co2, temp)
                else:
                    print("Lesefehler – warte auf nächste Messung...")
            
            # LED-Steuerung jede Iteration aktualisieren
            if co2 is not None:
                # Blink-Logik für rote LED
                if co2 >= 2000 and time.time() - last_blink > 0.5:
                    blink_state = GPIO.LOW if blink_state == GPIO.HIGH else GPIO.HIGH
                    last_blink = time.time()
                
                control_leds(co2, blink_state)
            
            time.sleep(0.1)  # Schnelle LED-Reaktion
            
    except KeyboardInterrupt:
        print(f"\n{RESET}Monitor beendet.")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
