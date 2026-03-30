---
ausbildungsberuf: Fachinformatiker Systemintegration
lehrjahr: 1
lernfeld: LF 7 — Cyberphysische Systeme
zeitraum: 3 Wochen Blockunterricht
programmiersprache: Python
hardware: Raspberry Pi, Sensoren, Aktoren
version: 0.1
---

# Rahmenhandlung — IIoT Erweiterungsauftrag

## Ausgangssituation

Euer Ausbildungsbetrieb erhält einen Auftrag von einem Hersteller für industrielle IoT-Lösungen (IIoT). Das Unternehmen vertreibt einen Minicomputer (Raspberry Pi), der auf Knopfdruck eine LED zum Leuchten bringt — ein erstes Produkt, das als Basis für komplexere Systeme gedacht war.

Das Problem: Der verantwortliche Chefentwickler hat das Unternehmen mitten im Entwicklungsprozess verlassen. Der hinterlassene Code ist eine einzige, unkommentierte Datei — schwer lesbar, nicht wartbar, nicht erweiterbar. Niemand beim Hersteller kann den Code noch nachvollziehen.

Euer Betrieb soll das Produkt retten und ausbauen.

## Auftrag

Am Ende des Projekts soll aus dem einfachen LED-Schalter ein vollwertiger **CO₂- und Raumklima-Monitor** entstehen, der:

- die **Luftqualität** (CO₂), **Temperatur** und **Luftfeuchtigkeit** misst
- den Zustand über **farbige LEDs** signalisiert (grün / gelb / rot je nach Messwert)
- bei kritischen Werten einen **Buzzer** als Alarm auslöst (zusätzlich zur roten LED)
- bei zu hoher Temperatur oder Feuchtigkeit eine **HTTP-Benachrichtigung** sendet
- Temperatur, Luftqualität und Luftfeuchtigkeit auf einem **Display** ausgeben

Der Hersteller stellt außerdem explizit die Anforderung: **Claude Code soll als KI-Assistent aktiv in den Entwicklungsprozess eingebunden werden** — zur Code-Analyse, zum Verständnis unbekannter Konzepte und zur Unterstützung bei der Umsetzung.

Dein Ausbilder nutzt diesen Auftrag als Lernchance: Er begleitet dich Schritt für Schritt in die Welt der Sensorik und Aktorik und gibt dir dafür Meilensteine an die Hand, die dir als Orientierung dienen, die auch in der Curriculum.md hinterlegt sind.


### Anforderungen des Herstellers im Detail

**Refactoring des Bestandscodes**
- Den bestehenden Code analysieren und verstehen
- Funktionen objektorientiert umschreiben und in dedizierte Klassen auslagern
- Den gesamten Code kommentieren — Inline-Kommentare und Docstrings für alle Klassen und Methoden
- Grenzwerte (Schwellwerte für Alarm etc.) in einem Konfigurationsdictionary zusammenfassen statt hardcoden
- Fehlerbehandlung mit `try/except/finally` absichern — insbesondere bei Sensorzugriff und GPIO-Cleanup

**Erweiterung der Sensorik**
- CO₂-Sensor integrieren
- Temperatur- und Luftfeuchtigkeitssensor ergänzen

**Erweiterung der Aktorik**
- Buzzer als Alarm-Aktor implementieren (ersetzt die rote LED bei Grenzwertüberschreitung)
- HTTP-Benachrichtigung bei kritischer Temperatur oder Luftfeuchtigkeit
- OOP-Struktur, vollständige Kommentierung und Fehlerbehandlung

**Projektdokumentation**
- Alle verwendeten externen Pakete in einer `requirements.txt` dokumentieren
- Alle Schnittstellen kommentieren
- Quelltextkonventionen einhalten


---


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

### 2a — Digitalen Sensor integrieren
- Einen digitalen Sensor (z.B. Bewegungsmelder, Reed-Kontakt) anschließen
- Zustand im Programm auslesen und mit if/else darauf reagieren

### 2b — Analogen Sensor integrieren
- Einen analogen Sensor (z.B. CO₂, Temperatur, Feuchte) über I²C oder SPI auslesen
- Rohwerte in sinnvolle Messwerte umrechnen

### 2c — Mehrere Sensoren kombinieren
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

### 3a — Buzzer als Alarm
- Buzzer anschließen und bei Grenzwertüberschreitung aktivieren
- Alarmlogik mit if/elif/else aufbauen

### 3b — Mehrere Aktoren steuern
- LED (grün/gelb/rot) und Buzzer gleichzeitig verwalten
- Zustandslogik strukturieren

### 3c — Relais mit externer Spannung
- Relais anschließen und über GPIO schalten
- Sicherheitsaspekte beachten (externe Spannung, Freilaufdiode)

### 3d — HTTP-Benachrichtigung
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

## Meilenstein 6 — Refactoring

**Ziel:** Den funktionierenden Code sauber, wartbar und objektorientiert umstrukturieren.

Das ist der Qualitätssprung: Von „es funktioniert" zu „jemand anderes kann es verstehen und weiterentwickeln".

**Unterpunkte:**

### 5a — Code in mehrere Dateien auslagern
- Sensorlogik, Aktorlogik und Hauptprogramm trennen
- Module importieren statt alles in eine Datei zu packen

### 5b — Kommentare und Docstrings
- Alle Funktionen und Klassen mit Docstrings versehen
- Nicht-offensichtliche Stellen mit Inline-Kommentaren erklären

### 5c — Code Smells beseitigen
- Doppelten Code identifizieren und zusammenfassen
- Magic Numbers durch benannte Konstanten oder Dictionary-Einträge ersetzen
- Funktionen die zu viel tun aufteilen

### 5d — Objektorientierte Umstrukturierung
- Sensor-Klassen erstellen (z.B. `CO2Sensor`, `DHT22Sensor`)
- Aktor-Klassen erstellen (z.B. `LEDController`, `Buzzer`)
- Hauptprogramm orchestriert nur noch Objekte

### 5e — Dokumentation
- `requirements.txt` pflegen
- README oder Übergabedokument erstellen

**Bezug zum Curriculum:**
- `4.1.1` Funktionen — sinnvolle Aufteilung
- `4.3.2` Docstrings — Methoden beschreiben
- `4.3.3` Inline-Kommentare — nicht-offensichtliche Stellen erklären
- `7.1.1` import — eigene Module einbinden
- `7.3.2` requirements.txt — Abhängigkeiten pflegen
- `9.1.1` Klasse definieren, Objekt erstellen
- `9.1.2` Attribute und Methoden
- `9.2.1` Vererbung — gemeinsame Basisklasse für Sensoren / Aktoren
- `9.3.1` Refactoring: prozedural → OOP

---

*Meilensteine spiegeln den Projektfortschritt — kein Meilenstein muss perfekt sein, bevor der nächste beginnt.*

---

# Curriculum — Python & Raspberry Pi Grundlagen

## Überblick

### Projektbeschreibung

[Wird von der Lehrkraft gepflegt — kurze Beschreibung des Projekts das die SuS über den Kurs hinweg entwickeln]

### Lernziele

Am Ende des Kurses können die Lernenden:

- Ein hardwarenahe Python-Programm eigenständig entwickeln und strukturieren
- Sensordaten einlesen, verarbeiten und auf Basis dieser Daten Aktoren ansteuern
- Kontrollstrukturen, Funktionen und Datenstrukturen situationsgerecht einsetzen
- Eigene Lösungsansätze begründen und mit alternativen Ansätzen vergleichen
- Code lesbar, wartbar und sinnvoll strukturiert schreiben
- Eigene Klassen definieren und bestehenden Code objektorientiert umstrukturieren

> **TODO:** Neues Lernziel ergänzt (OOP) — bitte prüfen ob das zur Lerngruppe passt

### Hinweise für die Lehrkraft

[Pädagogische Hinweise, Besonderheiten der Lerngruppe, Differenzierung]

## Themenblöcke

### 1 Kontrollstrukturen

#### 1.1 Entscheidungen

##### 1.1.1 if / elif / else

- **Erinnern** — Kennt die Syntax von if, elif und else und kann sie aufschreiben
- **Verstehen** — Erklärt den Unterschied zwischen if-elif und mehreren if-Blöcken hintereinander
- **Anwenden** — Setzt if/elif/else eigenständig zur Fallunterscheidung ein
- **Analysieren** — Begründet warum eine bestimmte Reihenfolge der Bedingungen notwendig ist
- **Bewerten** — Entscheidet ob elif oder ein neues if die bessere Wahl ist und begründet das

##### 1.1.2 Truthy / Falsy

- **Erinnern** — Nennt Beispiele für Truthy- und Falsy-Werte in Python (0, "", None, …)
- **Verstehen** — Erklärt warum `if x:` und `if x == True:` sich unterschiedlich verhalten können
- **Anwenden** — Nutzt Truthy/Falsy-Werte bewusst in Bedingungen statt explizite Vergleiche
- **Analysieren** — Erkennt Fehler die durch unbeabsichtigtes Truthy/Falsy-Verhalten entstehen

#### 1.2 Schleifen

##### 1.2.1 for-Schleife

- **Erinnern** — Kennt die Syntax einer for-Schleife mit range()
- **Verstehen** — Erklärt was range() mit einem, zwei und drei Parametern jeweils bewirkt
- **Anwenden** — Setzt for-Schleifen zur Iteration über Sequenzen und mit range() ein
- **Analysieren** — Erkennt off-by-one-Fehler und erklärt warum sie entstehen
- **Bewerten** — Entscheidet wann eine for-Schleife einer while-Schleife vorzuziehen ist

##### 1.2.2 while-Schleife

- **Erinnern** — Kennt die Syntax einer while-Schleife
- **Verstehen** — Erklärt warum eine fehlende Abbruchbedingung zu einer Endlosschleife führt
- **Anwenden** — Schreibt eine while-Schleife mit sinnvoller Abbruchbedingung
- **Anwenden** — Setzt eine Endlosschleife mit `while True` als bewusstes Pattern ein
- **Analysieren** — Vergleicht Boolean-Flag vs. break als zwei Wege eine while-Schleife zu beenden
- **Bewerten** — Entscheidet wann eine while-Schleife einer for-Schleife vorzuziehen ist

##### 1.2.3 break / continue / pass

- **Erinnern** — Kennt die Schlüsselwörter break, continue und pass und ihre Grundfunktion
- **Verstehen** — Erklärt den Unterschied zwischen break und continue an einem Beispiel
- **Anwenden** — Setzt break zum vorzeitigen Abbruch einer Schleife ein
- **Anwenden** — Nutzt continue um bestimmte Durchläufe gezielt zu überspringen
- **Analysieren** — Begründet warum break an falscher Stelle zu unerwartetem Verhalten führt
- **Bewerten** — Entscheidet ob break oder eine angepasste Schleifenbedingung die bessere Lösung ist

---

### 2 Hardware & GPIO — Grundlagen

> Früheinstieg: Gibt dem Kurs sofort einen greifbaren Kontext. Die SuS sehen direkt, wofür sie Python lernen.

#### 2.1 Digitale I/O

##### 2.1.1 GPIO-Pins: Input und Output

- **Erinnern** — Nennt den Unterschied zwischen Input- und Output-Pins und gibt je ein Beispiel
- **Verstehen** — Erklärt wie GPIO-Pins am Raspberry Pi über Python angesteuert werden (HIGH/LOW)
- **Anwenden** — Konfiguriert einen GPIO-Pin als Output und schaltet ihn per Python an und aus
- **Anwenden** — Konfiguriert einen GPIO-Pin als Input und liest seinen Zustand im Programm aus
- **Analysieren** — Erkennt warum eine fehlende oder falsche Pin-Konfiguration zu unerwartetem Verhalten führt
- **Bewerten** — Entscheidet welche Pins für welchen Einsatzzweck geeignet sind und begründet das

##### 2.1.2 LED ansteuern

- **Erinnern** — Kennt die korrekte Grundschaltung einer LED am GPIO-Pin (mit Vorwiderstand)
- **Verstehen** — Erklärt warum ein Vorwiderstand notwendig ist und was ohne ihn passiert
- **Anwenden** — Schreibt ein Python-Programm das eine LED ein- und ausschaltet
- **Anwenden** — Realisiert ein Blinkmuster mit `time.sleep()`
- **Analysieren** — Erklärt warum die LED ohne `sleep()` für das Auge nicht sichtbar blinkt
- **Bewerten** — Entscheidet zwischen HIGH/LOW-Logik je nach Schaltungsaufbau (aktiv-high vs. aktiv-low)

##### 2.1.3 Taster einlesen

- **Erinnern** — Kennt die Grundschaltung eines Tasters am GPIO-Pin
- **Verstehen** — Erklärt was Pull-up- und Pull-down-Widerstände bewirken und warum sie notwendig sind
- **Anwenden** — Liest den Zustand eines Tasters im Python-Programm aus und reagiert darauf mit if/else
- **Analysieren** — Erklärt den Unterschied zwischen gedrückt/losgelassen in HIGH/LOW-Logik bei Pull-up vs. Pull-down
- **Bewerten** — Wählt zwischen internem (Software-) und externem Pull-up/Pull-down je nach Anwendungsfall

##### 2.1.4 Buzzer ansteuern

- **Erinnern** — Kennt den Unterschied zwischen aktivem und passivem Buzzer und nennt je ein Einsatzbeispiel
- **Verstehen** — Erklärt warum ein aktiver Buzzer mit einem einfachen HIGH-Signal aktiviert wird, während ein passiver Buzzer ein PWM-Signal benötigt
- **Anwenden** — Schreibt ein Python-Programm das einen Buzzer bei Grenzwertüberschreitung aktiviert und danach wieder deaktiviert
- **Analysieren** — Begründet warum der Buzzer im `finally`-Block deaktiviert werden sollte um Dauerpiepen bei Programmabbruch zu verhindern
- **Bewerten** — Entscheidet wann ein Buzzer gegenüber einer LED als Alarm-Aktor geeigneter ist und begründet das

##### 2.1.5 Relais

- **Erinnern** — Kennt die Grundfunktion eines Relais und nennt Anwendungsbeispiele (z.B. externe Last mit höherer Spannung schalten)
- **Verstehen** — Erklärt warum ein Relais zur galvanischen Trennung zwischen Steuerkreis (GPIO) und Lastkreis (externe Spannung) eingesetzt wird
- **Anwenden** — Schließt ein Relaismodul korrekt an einen GPIO-Pin an und schaltet es über Python
- **Analysieren** — Begründet warum eine Freilaufdiode und die Einhaltung von Spannungs- und Stromgrenzen bei Relais sicherheitskritisch sind
- **Bewerten** — Entscheidet wann ein Relais gegenüber einer direkten GPIO-Schaltung notwendig ist

---

### 3 Daten & Variablen

#### 3.1 Variablen

##### 3.1.1 Zuweisung, Benennung, Konventionen

- **Erinnern** — Kennt die Syntax einer Variablenzuweisung in Python und nennt Regeln für gültige Bezeichner
- **Verstehen** — Erklärt warum sprechende Variablennamen die Lesbarkeit und Wartbarkeit verbessern
- **Anwenden** — Erstellt Variablen mit sinnvollen Namen nach Python-Konventionen (snake_case)
- **Analysieren** — Erkennt ungültige Bezeichner (z.B. Zahlen am Anfang, reservierte Wörter) und erklärt den Fehler
- **Bewerten** — Beurteilt ob ein Variablenname im gegebenen Kontext verständlich und konventionsgerecht ist

#### 3.2 Datentypen

##### 3.2.1 int, float, str, bool

- **Erinnern** — Nennt die vier grundlegenden Datentypen und je ein konkretes Beispiel
- **Verstehen** — Erklärt den Unterschied zwischen int und float und wann welcher Typ passend ist
- **Anwenden** — Erstellt Variablen der richtigen Typen für eine gegebene Aufgabenstellung
- **Analysieren** — Erkennt Typfehler (z.B. str + int) und erklärt warum Python sie nicht automatisch auflöst
- **Bewerten** — Wählt den passenden Datentyp für eine gegebene Anforderung und begründet die Wahl

#### 3.3 Typkonvertierung

##### 3.3.1 int(), str(), float()

- **Erinnern** — Kennt die Funktionen `int()`, `str()` und `float()` und ihre Grundfunktion
- **Verstehen** — Erklärt warum Typkonvertierung bei Nutzereingaben (input()) notwendig ist
- **Anwenden** — Konvertiert Eingabewerte korrekt in den benötigten Typ
- **Analysieren** — Erkennt wann eine Konvertierung scheitert (z.B. `int("abc")`) und erklärt den Fehler
- **Bewerten** — Entscheidet ob eine Konvertierung sicher durchgeführt werden kann oder abgesichert werden muss

#### 3.4 Operatoren

##### 3.4.1 Arithmetische Operatoren

- **Erinnern** — Kennt die arithmetischen Operatoren (`+`, `-`, `*`, `/`, `//`, `%`, `**`) und ihre Bedeutung
- **Verstehen** — Erklärt den Unterschied zwischen `/` (float-Division) und `//` (Ganzzahldivision)
- **Anwenden** — Setzt arithmetische Operatoren in Berechnungen korrekt ein
- **Analysieren** — Erkennt Rechenfehler durch falschen Operatoreinsatz (z.B. unbeabsichtigte Ganzzahldivision)
- **Bewerten** — Wählt den passenden Operator für eine mathematische Anforderung und begründet die Wahl

##### 3.4.2 Vergleichsoperatoren

- **Erinnern** — Kennt die Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`) und ihre Bedeutung
- **Verstehen** — Erklärt warum `==` (Vergleich) und `=` (Zuweisung) sich grundlegend unterscheiden
- **Anwenden** — Nutzt Vergleichsoperatoren in Bedingungen korrekt und versteht den bool-Rückgabewert
- **Analysieren** — Erkennt Bugs die durch Verwechslung von `=` und `==` entstehen

##### 3.4.3 Logische Operatoren

- **Erinnern** — Kennt die logischen Operatoren `and`, `or`, `not` und ihre Grundbedeutung
- **Verstehen** — Erklärt die Wahrheitstabellen von `and` und `or` in eigenen Worten an Beispielen
- **Anwenden** — Verknüpft mehrere Bedingungen mit `and` / `or` korrekt in einer Bedingung
- **Analysieren** — Erkennt logische Fehler in zusammengesetzten Bedingungen und begründet das erwartete Verhalten
- **Bewerten** — Entscheidet ob eine komplexe Bedingung mit `not` oder Umstrukturierung vereinfacht werden kann

---

### 4 Funktionen

#### 4.1 Grundlagen

##### 4.1.1 Definition mit def, Parameter, Rückgabewert

- **Erinnern** — Kennt die Syntax einer Funktionsdefinition mit `def`, Parametern und `return`
- **Verstehen** — Erklärt warum Funktionen Code wiederverwendbar, testbar und lesbar machen
- **Anwenden** — Schreibt eine eigene Funktion mit Parametern und Rückgabewert für eine konkrete Aufgabe
- **Analysieren** — Erkennt Funktionen die zu viel auf einmal tun und erklärt warum das problematisch ist
- **Bewerten** — Entscheidet ob ein Codeabschnitt in eine eigene Funktion ausgelagert werden sollte und begründet das

##### 4.1.2 return vs. print

- **Erinnern** — Kennt den syntaktischen Unterschied zwischen `return` und `print`
- **Verstehen** — Erklärt warum eine Funktion die nur druckt keinen nutzbaren Rückgabewert hat (`None`)
- **Anwenden** — Schreibt Funktionen die Werte zurückgeben statt sie direkt auszudrucken
- **Analysieren** — Erkennt Bugs die entstehen wenn `return` mit `print` verwechselt wird (z.B. `None`-Fehler)

#### 4.2 Scope

##### 4.2.1 Lokal vs. global

- **Erinnern** — Nennt den Unterschied zwischen lokalem und globalem Scope an einem Beispiel
- **Verstehen** — Erklärt warum lokale Variablen außerhalb ihrer Funktion nicht sichtbar sind
- **Anwenden** — Schreibt Funktionen die lokale Variablen verwenden ohne globale unbeabsichtigt zu verändern
- **Analysieren** — Erkennt `NameError`-Fehler durch lokalen Scope und erklärt ihre Ursache
- **Bewerten** — Beurteilt wann globale Variablen vermieden werden sollten und begründet das mit Wartbarkeit

#### 4.3 Erweiterte Konzepte

##### 4.3.1 Standardargumente & Keyword-Argumente

- **Erinnern** — Kennt die Syntax für Standardargumente (`def f(x=0)`) und Keyword-Argumente beim Aufruf
- **Verstehen** — Erklärt wann Standardargumente sinnvoll sind und was passiert wenn sie weggelassen werden
- **Anwenden** — Definiert Funktionen mit Standardargumenten und ruft sie mit Keyword-Argumenten auf
- **Analysieren** — Erkennt warum Standardargumente immer nach Pflichtargumenten stehen müssen

##### 4.3.2 Docstrings

- **Erinnern** — Kennt die Syntax eines Docstrings (dreifache Anführungszeichen direkt nach `def`)
- **Verstehen** — Erklärt warum Docstrings für die Wartbarkeit und Zusammenarbeit wichtig sind
- **Anwenden** — Schreibt Docstrings für eigene Funktionen die Zweck, Parameter und Rückgabewert beschreiben
- **Bewerten** — Beurteilt ob ein vorhandener Docstring ausreichend und korrekt ist

##### 4.3.3 Inline-Kommentare

- **Erinnern** — Kennt die Syntax eines Inline-Kommentars in Python (`#`) und weiß an welcher Stelle er im Code steht
- **Verstehen** — Erklärt den Unterschied zwischen einem Docstring (was eine Funktion tut) und einem Inline-Kommentar (warum eine konkrete Zeile oder ein Abschnitt so umgesetzt ist)
- **Anwenden** — Ergänzt sinnvolle Inline-Kommentare in bestehendem Code an nicht selbsterklärenden Stellen (z.B. GPIO-Cleanup, Grenzwertprüfung)
- **Bewerten** — Beurteilt ob ein Kommentar das „Warum" erklärt oder nur das „Was" wiederholt — und entscheidet ob er damit hilfreich oder überflüssig ist

---

### 5 Datenstrukturen

#### 5.1 Listen

##### 5.1.1 Erstellen, Indexzugriff, Slicing

- **Erinnern** — Kennt die Syntax zum Erstellen einer Liste und den Zugriff per Index
- **Verstehen** — Erklärt warum Indizes in Python bei 0 beginnen und was negative Indizes bedeuten
- **Anwenden** — Erstellt Listen, greift per positivem und negativem Index zu und nutzt Slicing für Teillisten
- **Analysieren** — Erkennt `IndexError` und erklärt in welcher Situation er auftritt
- **Bewerten** — Entscheidet ob Slicing oder eine Schleife für eine gegebene Aufgabe besser geeignet ist

##### 5.1.2 Methoden: append, remove, pop, sort

- **Erinnern** — Kennt die Methoden `append()`, `remove()`, `pop()` und `sort()` und ihre Grundfunktion
- **Verstehen** — Erklärt den Unterschied zwischen `remove()` (nach Wert suchen) und `pop()` (nach Index)
- **Anwenden** — Setzt die Methoden korrekt ein um eine Liste zu verändern
- **Analysieren** — Erkennt was passiert wenn `remove()` einen nicht vorhandenen Wert löschen soll

##### 5.1.3 Iteration über Listen

- **Erinnern** — Kennt die Syntax einer for-Schleife die direkt über eine Liste iteriert
- **Verstehen** — Erklärt den Unterschied zwischen Iteration über Werte und Iteration über Indizes mit `enumerate()`
- **Anwenden** — Iteriert über eine Liste und verarbeitet jeden Wert
- **Anwenden** — Nutzt `enumerate()` um gleichzeitig Index und Wert zu erhalten
- **Analysieren** — Erkennt warum das Verändern einer Liste während der Iteration zu Fehlern führen kann

##### 5.1.4 List Comprehensions

- **Erinnern** — Kennt die Grundsyntax einer List Comprehension (`[ausdruck for element in liste]`)
- **Verstehen** — Erklärt wie eine List Comprehension einer gleichwertigen for-Schleife entspricht
- **Anwenden** — Schreibt einfache List Comprehensions zur Transformation von Listen
- **Bewerten** — Entscheidet wann eine List Comprehension lesbarer ist als eine for-Schleife

#### 5.2 Dictionaries

##### 5.2.1 Schlüssel-Wert-Paare, Zugriff, Einfügen, Löschen

- **Erinnern** — Kennt die Syntax zum Erstellen eines Dictionaries und den Zugriff per Schlüssel
- **Verstehen** — Erklärt warum Dictionaries Schlüssel-Wert-Paare nutzen statt numerischer Indizes
- **Anwenden** — Erstellt Dictionaries, liest Werte aus, fügt Einträge hinzu und löscht sie
- **Analysieren** — Erkennt `KeyError` und erklärt in welchen Situationen er auftritt
- **Bewerten** — Entscheidet ob `get()` oder direkter Schlüsselzugriff für einen Anwendungsfall besser ist

##### 5.2.2 Iteration über Keys/Values

- **Erinnern** — Kennt die Methoden `keys()`, `values()` und `items()`
- **Verstehen** — Erklärt den Unterschied zwischen Iteration über Keys, Values und Items
- **Anwenden** — Iteriert über ein Dictionary mit `items()` und verarbeitet Schlüssel und Wert
- **Analysieren** — Erklärt warum die Reihenfolge in Dictionaries ab Python 3.7 deterministisch ist

##### 5.2.3 Verschachtelte Dictionaries

- **Erinnern** — Kennt die Syntax eines verschachtelten Dictionaries und kann es aufschreiben
- **Verstehen** — Erklärt wann verschachtelte Dictionaries sinnvoll sind und wann sie zu komplex werden
- **Anwenden** — Greift auf Werte in einem verschachtelten Dictionary korrekt zu
- **Analysieren** — Erkennt Zugriffsfehler bei falsch verschachtelten Strukturen und erklärt ihre Ursache

---

### 6 Fehlerbehandlung

#### 6.1 Grundlagen

##### 6.1.1 try, except, finally

- **Erinnern** — Kennt die Syntax von `try`, `except` und `finally`
- **Verstehen** — Erklärt wann `try/except` sinnvoll ist und was ohne es bei einem Fehler passiert
- **Anwenden** — Sichert fehleranfällige Codeabschnitte mit `try/except` ab
- **Analysieren** — Erkennt warum ein leerer `except`-Block (bare except) problematisch ist
- **Bewerten** — Entscheidet wann `finally` notwendig ist (z.B. GPIO-Cleanup) und wann es weggelassen werden kann

##### 6.1.2 Spezifische Exceptions

- **Erinnern** — Kennt häufige Exceptions: `ValueError`, `TypeError`, `IndexError`, `KeyError`
- **Verstehen** — Erklärt welche Exception in welcher Situation auftritt und warum
- **Anwenden** — Fängt spezifische Exceptions statt einem generischen `except` ab
- **Analysieren** — Liest Traceback-Meldungen und identifiziert Fehlertyp, -ort und -ursache
- **Bewerten** — Entscheidet welche Exceptions in einem bestimmten Kontext sinnvoll abgefangen werden sollten

##### 6.1.3 Eigene Fehlermeldungen

- **Erinnern** — Kennt die Möglichkeit im `except`-Block eine eigene Meldung auszugeben
- **Verstehen** — Erklärt warum aussagekräftige Fehlermeldungen die Fehlersuche erleichtern
- **Anwenden** — Schreibt eigene Fehlermeldungen die dem Nutzer hilfreiche Hinweise zur Ursache geben
- **Bewerten** — Beurteilt ob eine Fehlermeldung ausreichend informativ ist oder zu allgemein bleibt

---

### 7 Module & Bibliotheken
<!-- TODO: venvs mit dazu  -->
#### 7.1 Grundlagen

##### 7.1.1 import, from … import

- **Erinnern** — Kennt die Syntax von `import` und `from … import`
- **Verstehen** — Erklärt den Unterschied zwischen `import modul` und `from modul import funktion`
- **Anwenden** — Importiert Module und nutzt deren Funktionen korrekt im eigenen Programm
- **Analysieren** — Erkennt Namenskonflikte die durch `from … import *` entstehen können

#### 7.2 Standardbibliothek

##### 7.2.1 random, time, math, os

- **Erinnern** — Kennt die wichtigsten Funktionen von `random`, `time`, `math` und `os` und ihren Zweck
- **Verstehen** — Erklärt wozu jedes dieser Module eingesetzt wird und gibt je ein Anwendungsbeispiel
- **Anwenden** — Nutzt Funktionen aus diesen Modulen sinnvoll in eigenen Programmen
- **Analysieren** — Erkennt wann ein Standardmodul die bessere Lösung gegenüber selbst geschriebenem Code ist

#### 7.3 Externe Pakete

##### 7.3.1 pip und externe Pakete

- **Erinnern** — Kennt den Befehl `pip install` und weiß was PyPI ist
- **Verstehen** — Erklärt den Unterschied zwischen Standardbibliothek und extern installierten Paketen
- **Anwenden** — Installiert ein Paket mit pip und importiert es im eigenen Code
- **Analysieren** — Erkennt warum Abhängigkeiten in einem Projekt dokumentiert werden sollten (z.B. requirements.txt)

##### 7.3.2 requirements.txt

> **TODO:** Neu ergänzt — passt gut zum Projektabschluss und zur Übergabe an den Hersteller; prüfen ob der Zeitpunkt im Kurs gut gewählt ist

- **Erinnern** — Kennt das Format einer `requirements.txt` und weiß wozu sie dient
- **Verstehen** — Erklärt warum eine `requirements.txt` die Reproduzierbarkeit eines Projekts sicherstellt und was ohne sie bei der Weitergabe passieren kann
- **Anwenden** — Erstellt eine `requirements.txt` manuell oder mit `pip freeze > requirements.txt` und installiert Abhängigkeiten mit `pip install -r requirements.txt`
- **Analysieren** — Erkennt den Unterschied zwischen `pip freeze` (alle installierten Pakete) und einer manuell gepflegten `requirements.txt` (nur direkte Abhängigkeiten) und erklärt wann welche Variante sinnvoller ist
- **Bewerten** — Beurteilt ob eine gegebene `requirements.txt` vollständig und sinnvoll gepflegt ist

##### 7.3.3 Virtuelle Umgebungen (venv)

> **TODO:** Neu ergänzt — prüfen ob venvs im Kontext Raspberry Pi / Blockunterricht sinnvoll eingesetzt werden können (ggf. nur als Konzept einführen)

- **Erinnern** — Kennt den Befehl `python -m venv` und weiß wozu eine virtuelle Umgebung dient
- **Verstehen** — Erklärt warum venvs Paket-Konflikte zwischen Projekten verhindern und warum globale pip-Installationen problematisch sein können
- **Anwenden** — Erstellt eine virtuelle Umgebung, aktiviert sie und installiert darin Pakete
- **Analysieren** — Erkennt warum ein Paket das global installiert wurde in einer venv nicht verfügbar ist und umgekehrt
- **Bewerten** — Entscheidet wann eine virtuelle Umgebung sinnvoll ist und dokumentiert Abhängigkeiten korrekt in `requirements.txt`

##### 7.3.4 HTTP-Anfragen mit requests

- **Erinnern** — Kennt die Funktionen `requests.get()` und `requests.post()` und weiß wozu die `requests`-Bibliothek eingesetzt wird
- **Verstehen** — Erklärt was eine HTTP-Anfrage ist, was ein Statuscode bedeutet und wie `requests` den Versand gegenüber der Standardbibliothek vereinfacht
- **Anwenden** — Sendet eine HTTP-POST-Benachrichtigung mit `requests.post()` wenn ein Grenzwert überschritten wird
- **Analysieren** — Erkennt warum HTTP-Anfragen mit `try/except` abgesichert werden sollten (z.B. fehlende Netzwerkverbindung, Timeout)
- **Bewerten** — Entscheidet wann eine HTTP-Benachrichtigung gegenüber anderen Alarmarten (LED, Buzzer) sinnvoll ist und begründet das

---

### 8 Hardware & GPIO — Erweitert

> Setzt Grundlagen aus Block 2 sowie Funktionen, Datenstrukturen und Fehlerbehandlung voraus.

#### 8.1 Analoge Signale

##### 8.1.1 ADC: Analog-Digital-Wandlung

- **Erinnern** — Erklärt was ein ADC ist und warum der Raspberry Pi keinen eingebauten ADC hat
- **Verstehen** — Beschreibt das Prinzip der Analog-Digital-Wandlung (Auflösung in Bit, Wertebereich)
- **Anwenden** — Liest Analogwerte über einen MCP3008 per SPI aus und gibt sie im Programm aus
- **Analysieren** — Interpretiert Rohwerte des ADC und rechnet sie in physikalisch sinnvolle Größen um

##### 8.1.2 Sensorwerte einlesen und verarbeiten

- **Erinnern** — Nennt Beispiele für analoge Sensoren (Temperatur, Licht, Feuchtigkeit) und deren Signalart
- **Verstehen** — Erklärt wie Sensorkennlinien Rohwerte in reale Messwerte übersetzen
- **Anwenden** — Liest Sensorwerte aus, verarbeitet sie und gibt sie sinnvoll formatiert aus
- **Analysieren** — Erkennt Ausreißer oder unplausible Werte in Sensordaten und diskutiert mögliche Ursachen
- **Bewerten** — Entscheidet ob eine Mittelung oder Filterung der Sensorwerte für den Anwendungsfall sinnvoll ist

#### 8.2 Kommunikationsprotokolle

##### 8.2.1 I²C

- **Erinnern** — Kennt die grundlegenden Eigenschaften von I²C (2 Leitungen: SDA/SCL, Geräteadressen)
- **Verstehen** — Erklärt wie mehrere Geräte am selben I²C-Bus betrieben werden können
- **Anwenden** — Kommuniziert mit einem I²C-Gerät (z.B. Display oder Sensor) im Python-Programm
- **Analysieren** — Nutzt `i2cdetect` um Geräte am Bus zu identifizieren und Verbindungsprobleme zu diagnostizieren

##### 8.2.2 SPI

- **Erinnern** — Kennt die grundlegenden Eigenschaften von SPI (4 Leitungen: MOSI, MISO, SCLK, CS)
- **Verstehen** — Erklärt den Unterschied zwischen I²C und SPI hinsichtlich Geschwindigkeit und Verkabelungsaufwand
- **Anwenden** — Kommuniziert mit einem SPI-Gerät (z.B. MCP3008) im Python-Programm

##### 8.2.3 UART / Serial

- **Erinnern** — Kennt die grundlegenden Eigenschaften von UART (TX/RX, Baudrate, kein Takt)
- **Verstehen** — Erklärt wann serieller Datenaustausch über UART sinnvoll ist
- **Anwenden** — Sendet und empfängt Daten über UART im Python-Programm mit `pyserial`

##### 8.2.4 Display ansteuern

- **Erinnern** — Kennt typische Display-Typen im Raspberry-Pi-Umfeld (z.B. OLED, LCD) und ihre übliche Kommunikationsschnittstelle (I²C)
- **Verstehen** — Erklärt wie Messwerte strukturiert und lesbar auf einem Display ausgegeben werden können (Zeilenaufteilung, Einheiten)
- **Anwenden** — Gibt Sensorwerte (CO₂, Temperatur, Luftfeuchtigkeit) formatiert auf einem I²C-Display aus
- **Analysieren** — Erkennt warum die Aktualisierungsrate der Anzeige auf die Messrate abgestimmt sein sollte um unnötige Schreibzugriffe zu vermeiden
- **Bewerten** — Entscheidet welche Informationen auf dem Display sinnvoll angezeigt werden und wie sie übersichtlich angeordnet sind

#### 8.3 GPIO-Bibliotheken

##### 8.3.1 RPi.GPIO vs. gpiozero

- **Erinnern** — Kennt den konzeptionellen Unterschied zwischen `RPi.GPIO` und `gpiozero`
- **Verstehen** — Erklärt warum `gpiozero` für Einsteiger oft leichter zugänglich ist als `RPi.GPIO`
- **Anwenden** — Implementiert eine äquivalente Aufgabe (LED, Taster) sowohl mit `RPi.GPIO` als auch mit `gpiozero`
- **Bewerten** — Entscheidet für eine gegebene Aufgabe welche Bibliothek besser geeignet ist und begründet das

---

### 9 Objektorientierte Programmierung

> **TODO:** Gesamter Block neu — bitte Umfang, Tiefe und Reihenfolge im Team abstimmen

> Setzt Grundlagen aus Funktionen (Block 4) voraus. Ziel ist das Refactoring von prozeduralem Code in eine wartbare Klassenstruktur — direkt angebunden an das Projektprojekt.

#### 9.1 Klassen und Objekte

##### 9.1.1 Klasse definieren, Objekt erstellen

- **Erinnern** — Kennt die Syntax von `class`, `__init__` und `self` und kann sie aufschreiben
- **Verstehen** — Erklärt den Unterschied zwischen einer Klasse (Bauplan) und einem Objekt (Instanz) an einem konkreten Beispiel
- **Anwenden** — Definiert eine eigene Klasse mit Attributen und erstellt davon ein Objekt
- **Analysieren** — Erkennt warum `self` als erster Parameter jeder Methode notwendig ist
- **Bewerten** — Entscheidet welche Verantwortlichkeiten sinnvoll in eine eigene Klasse gehören

##### 9.1.2 Attribute und Methoden

- **Erinnern** — Unterscheidet zwischen Instanzattributen (gesetzt in `__init__`) und Methoden
- **Verstehen** — Erklärt warum Attribute im Objekt gespeichert werden statt als lokale Variablen
- **Anwenden** — Schreibt Methoden die auf Instanzattribute zugreifen und sie verändern
- **Analysieren** — Erkennt Fehler die entstehen wenn `self` vergessen oder falsch eingesetzt wird

#### 9.2 Vererbung

##### 9.2.1 Basisklasse und abgeleitete Klasse

- **Erinnern** — Kennt die Syntax der Vererbung (`class Kind(Eltern):`) und weiß was vererbt wird
- **Verstehen** — Erklärt wann Vererbung sinnvoll ist und wann sie zu unnötiger Komplexität führt
- **Anwenden** — Leitet eine Klasse von einer Basisklasse ab und ergänzt oder überschreibt Methoden
- **Analysieren** — Erkennt warum `super().__init__()` notwendig ist und was ohne es passiert
- **Bewerten** — Entscheidet ob Vererbung oder Komposition für einen Anwendungsfall besser geeignet ist

#### 9.3 OOP im Projektkontext

##### 9.3.1 Refactoring: prozedural → objektorientiert

- **Erinnern** — Kennt typische Anzeichen für prozeduralen Code der von OOP profitieren würde (z.B. viele Parameter, wiederkehrende Datenstrukturen)
- **Verstehen** — Erklärt wie eine Klasse Zustand (Attribute) und Verhalten (Methoden) zusammenfasst und warum das Wartbarkeit verbessert
- **Anwenden** — Überführt einen vorhandenen prozeduralen Codeabschnitt in eine Klasse mit sinnvoller Struktur
- **Analysieren** — Begründet die gewählte Klassenaufteilung und zeigt Alternativen auf
- **Bewerten** — Beurteilt ob eine gegebene Klasse das Single-Responsibility-Prinzip einhält und schlägt Verbesserungen vor