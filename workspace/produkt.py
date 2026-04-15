import RPi.GPIO as GPIO  # Raspberry Pi GPIO-Bibliothek importieren
import time  # Zeit-Bibliothek für sleep() importieren

GPIO.setmode(GPIO.BCM)  # BCM-Pinnummerierung verwenden (statt physische Pin-Nummern)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Pin 21 als Eingang mit Pull-Down-Widerstand konfigurieren
GPIO.setup(22, GPIO.OUT)  # Pin 22 als Ausgang konfigurieren

try:
    while True:  # Endlosschleife
        if GPIO.input(21):  # Prüfen ob Taster an Pin 21 gedrückt (HIGH)
            print("BUTTON PRESSED")  # Statusmeldung in der Konsole ausgeben
            GPIO.output(22, GPIO.HIGH)  # Pin 22 einschalten (z.B. LED an)
            time.sleep(3)  # 3 Sekunden warten
            GPIO.output(22, GPIO.LOW)  # Pin 22 ausschalten (z.B. LED aus)

except KeyboardInterrupt:  # Strg+C abfangen
    print("Programm beendet")  # Abschlussmeldung ausgeben

finally:
    GPIO.cleanup()  # GPIO-Pins zurücksetzen und Ressourcen freigeben