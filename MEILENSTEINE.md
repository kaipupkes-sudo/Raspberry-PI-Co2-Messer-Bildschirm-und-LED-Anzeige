# Meilensteine — IIoT Erweiterungsauftrag

> Diese Meilensteine dienen als **Orientierung**, nicht als Pflichtprogramm.
> Sie zeigen einen sinnvollen Weg durch das Projekt — von der ersten Hardware-Inbetriebnahme bis zum fertigen, sauber dokumentierten Produkt.
> Die Reihenfolge ist empfohlen, aber nicht zwingend.

---

## Meilenstein 1 — Raspberry Pi in Betrieb nehmen

**Ziel:** Den Raspberry Pi verkabeln und `produkt.py` erfolgreich ausführen.

Das ist der Einstieg ins Projekt. Ihr macht euch mit der Hardware vertraut und versteht, was der vorhandene Code tut — auch wenn er noch nicht perfekt ist.

**Schritte:**
- Raspberry Pi aufbauen und mit Strom versorgen
- LED und Taster anhand der in der `produkt.py` verwendeten Pins verkabeln.
- `produkt.py` ausführen und Verhalten beobachten
- Den Code lesen und verstehen: Was passiert Zeile für Zeile?

**Bezug zum Curriculum:**
- `2.1.1` GPIO-Pins: Input und Output
- `2.1.2` LED ansteuern
- `2.1.3` Taster einlesen
- `7.1.1` import — was importiert der Code und wozu?

---

## Meilenstein 2 — produkt.py verstehen und aufräumen

**Ziel:** Den vorhandenen Code analysieren, Probleme benennen und eine erste bereinigte Version erstellen.

Bevor etwas erweitert wird, muss man verstehen was da ist — und was daran problematisch ist. Das ist der erste echte Refactoring-Schritt.

**Unterpunkte:**

### 2a — Code lesen und Probleme benennen
- Was macht der Code Zeile für Zeile?
- Welche Stellen wirken unübersichtlich oder fehleranfällig?

### 2b — Imports ans richtige Ende
- `import`-Anweisungen gehören an den Anfang der Datei — nicht mittendrin
- Alle Imports zusammenfassen und an den Anfang stellen

### 2c — Hardcoding der Pins auslagern
- Pin-Nummern (`21`, `22`) als benannte Konstanten definieren statt direkt im Code
- Beispiel: `BUTTON_PIN = 21` — damit ist sofort klar was der Wert bedeutet

### 2d — Fehlerbehandlung einbauen
- Was passiert wenn die GPIO-Initialisierung fehlschlägt?
- `try/except` und `finally` für sauberes GPIO-Cleanup beim Programmabbruch

### 2e — Schnittstellenkommentare
- Kommentare ergänzen die erklären was der Code tut — nicht wie
- Jeder logische Abschnitt bekommt eine kurze Beschreibung

**Bezug zum Curriculum:**
- `1.2.2` while True — bewusstes Pattern verstehen
- `3.1.1` Zuweisung, Benennung, Konventionen — sprechende Konstantennamen
- `4.3.3` Inline-Kommentare — Schnittstellenkommentare ergänzen
- `6.1.1` try / except / finally — GPIO-Cleanup absichern
- `7.1.1` import — Imports strukturieren

---

## Meilenstein 3 — Sensorik erweitern

**Ziel:** Den Taster durch einen echten Sensor ersetzen und Messwerte verarbeiten.

Statt eines Knopfdrucks reagiert das System jetzt auf reale Umweltdaten.

**Unterpunkte:**

### 3a — Digitalen Sensor integrieren
- Einen digitalen Sensor (z.B. Bewegungsmelder, Reed-Kontakt) anschließen
- Zustand im Programm auslesen und mit if/else darauf reagieren

### 3b — Analogen Sensor integrieren
- Einen analogen Sensor (z.B. CO₂, Temperatur, Feuchte) über I²C oder SPI auslesen
- Rohwerte in sinnvolle Messwerte umrechnen

### 3c — Mehrere Sensoren kombinieren
- Mehr als einen Sensor gleichzeitig betreiben
- Messwerte strukturiert speichern (z.B. in einem Dictionary)

**Bezug zum Curriculum:**
- `1.1.1` if / elif / else — Fallunterscheidung nach Messwert
- `1.2.2` while-Schleife — Dauermessung im Loop
- `5.2.1` Dictionaries — Messwerte strukturiert ablegen
- `8.1.1` ADC — Analog-Digital-Wandlung
- `8.1.2` Sensorwerte einlesen und verarbeiten
- `8.2.1` I²C — Kommunikation mit Sensor
- `8.2.2` SPI — Alternative Kommunikation

---

## Meilenstein 4 — Aktorik erweitern

**Ziel:** Die LED durch sinnvollere Aktoren ersetzen und auf Sensorwerte reagieren.

Das System soll nicht mehr nur leuchten — es soll warnen, schalten, handeln.

**Unterpunkte:**

### 4a — Buzzer als Alarm
- Buzzer anschließen und bei Grenzwertüberschreitung aktivieren
- Alarmlogik mit if/elif/else aufbauen

### 4b — Mehrere Aktoren steuern
- LED (grün/gelb/rot) und Buzzer gleichzeitig verwalten
- Zustandslogik strukturieren

### 4c — Relais mit externer Spannung
- Relais anschließen und über GPIO schalten
- Sicherheitsaspekte beachten (externe Spannung, Freilaufdiode)

### 4d — HTTP-Benachrichtigung
- Bei kritischem Messwert eine HTTP-Nachricht senden
- `requests`-Bibliothek installieren und einsetzen

**Bezug zum Curriculum:**
- `1.1.1` if / elif / else — Aktorsteuerung nach Zustand
- `2.1.1` GPIO Output — Aktor ansteuern
- `2.1.4` Buzzer ansteuern — Alarm-Aktor implementieren
- `2.1.5` Relais — externe Last schalten
- `6.1.1` try / except / finally — Fehler bei HTTP-Request abfangen
- `7.3.1` pip — externes Paket `requests` installieren
- `7.3.4` HTTP-Anfragen mit requests — Benachrichtigung bei Grenzwertüberschreitung senden

---

## Meilenstein 5 — Fertiges Produkt

**Ziel:** Alle Anforderungen der Rahmenhandlung umsetzen — CO₂-Monitor mit LED, Buzzer und HTTP-Alarm.

Das ist die funktionale Vollständigkeit: Alles läuft, alles reagiert korrekt auf Messwerte.

**Schritte:**
- CO₂, Temperatur und Feuchte werden gemessen
- LEDs zeigen Ampelfarben je nach Luftqualität
- Buzzer schlägt Alarm bei kritischen Werten
- HTTP-Benachrichtigung bei Temperatur- oder Feuchteüberschreitung
- Grenzwerte sind konfigurierbar (kein Hardcoding)
- Fehlerbehandlung ist überall vorhanden

**Bezug zum Curriculum:**
- `1.1.1` if / elif / else — Ampellogik
- `1.2.2` while True — Dauerbetrieb
- `5.2.1` Dictionaries — Konfiguration der Grenzwerte
- `6.1.1` try / except / finally — robuste Fehlerbehandlung
- `7.3.1` pip — Abhängigkeiten installieren
- `7.3.2` requirements.txt — Abhängigkeiten dokumentieren
- `7.3.3` venv — Abhängigkeiten sauber isolieren
- `8.1.2` Sensorwerte verarbeiten
- `8.2.4` Display ansteuern — Messwerte ausgeben

---

*Meilensteine spiegeln den Projektfortschritt — kein Meilenstein muss perfekt sein, bevor der nächste beginnt.*
