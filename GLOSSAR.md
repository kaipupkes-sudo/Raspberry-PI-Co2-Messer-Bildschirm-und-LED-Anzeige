# Glossar

> Wird automatisch gepflegt — neue Begriffe werden ergänzt wenn sie im Lernprozess fallen oder ein Lernender nach einer Erklärung fragt.

## 1 Grundlagen & Projektkontext

**IIoT** — Industrial Internet of Things. Bezeichnet vernetzte Geräte und Systeme in industriellen Umgebungen, die Daten erfassen, übertragen und verarbeiten — z.B. Sensoren in Fabriken oder Maschinen.

**Raspberry Pi** — Ein kleiner Einplatinencomputer, der sich gut für Hardware-nahe Projekte eignet. Er hat GPIO-Pins über die er mit Sensoren, LEDs, Motoren und anderen Bauteilen kommunizieren kann.

**GPIO** — General Purpose Input/Output. Die programmierbaren Ein-/Ausgabe-Pins am Raspberry Pi. Über sie können Signale gelesen (z.B. Taster) oder gesendet werden (z.B. LED ein-/ausschalten).

**Refactoring** — Das Umschreiben von bestehendem Code, um ihn lesbarer, wartbarer oder strukturierter zu machen — ohne das äußere Verhalten zu ändern. Der Code tut danach dasselbe, ist aber besser organisiert.

**CO₂-Monitor** — Ein Gerät, das den CO₂-Gehalt der Luft misst und ausgibt. Hohe CO₂-Werte deuten auf schlechte Luftqualität hin und können Alarm auslösen.

**BCM** — Broadcom-Nummerierung. Eine von zwei Möglichkeiten, GPIO-Pins am Raspberry Pi anzusprechen. BCM bezieht sich auf die Chip-interne Nummerierung des Broadcom-Prozessors — nicht auf die physische Position des Pins auf der Platine.

**DHT11** — Ein einfacher digitaler Sensor für Temperatur und Luftfeuchtigkeit. Kommuniziert über ein eigenes 1-Wire-Protokoll und wird in Python meist über eine externe Bibliothek angesprochen (z.B. `adafruit-dht`).

**I²C** — Inter-Integrated Circuit. Ein serielles Kommunikationsprotokoll für kurze Distanzen zwischen Mikrocontrollern und Sensoren/Aktoren. Nutzt zwei Leitungen: SDA (Daten) und SCL (Takt). Erlaubt mehrere Geräte auf demselben Bus.

**Pull-Down-Widerstand** — Ein Widerstand, der einen Eingangspin auf ein definiertes LOW-Signal zieht, wenn kein Signal anliegt. Verhindert undefinierte Zustände (sogenanntes „Floating") am Pin.

## 6 Fehlerbehandlung

**try / except / finally** — Konstrukt zur Fehlerbehandlung in Python. Code im `try`-Block wird ausgeführt. Tritt ein Fehler auf, springt Python in den passenden `except`-Block. `finally` wird immer ausgeführt — egal ob ein Fehler aufgetreten ist oder nicht. Gut geeignet um Ressourcen (z.B. GPIO-Pins) sauber freizugeben.

**KeyboardInterrupt** — Eine Ausnahme (Exception) die ausgelöst wird, wenn der Nutzer das Programm mit Strg+C abbricht. Kann mit `except KeyboardInterrupt:` abgefangen werden.

**GPIO.cleanup()** — Setzt alle GPIO-Pins auf ihren Ausgangszustand zurück und gibt die Ressourcen frei. Sollte immer am Ende eines Programms aufgerufen werden — idealerweise im `finally`-Block.

## 4 Kontrollstrukturen

**Endlosschleife** — Eine Schleife ohne Abbruchbedingung, die theoretisch für immer läuft. In Python typisch als `while True:`. Wird in Embedded-Systemen bewusst eingesetzt, damit ein Programm dauerhaft läuft — z.B. um ständig Sensoren abzufragen.

## 4 Codequalität & Dokumentation

**Inline-Kommentar** — Ein Kommentar der direkt hinter einer Codezeile steht. Erklärt was oder warum an dieser Stelle etwas passiert. Gute Kommentare erklären das *Warum*, nicht das offensichtliche *Was*.
