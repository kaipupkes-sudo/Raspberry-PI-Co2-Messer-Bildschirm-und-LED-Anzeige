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

## Anforderungen des Herstellers im Detail

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
