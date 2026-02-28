# Aufgabe: Zahlenratespiel

## Kompetenz
- Kontrollstrukturen > Kann while-Schleife mit Abbruchbedingung schreiben
- Kontrollstrukturen > Kann if/elif/else zur Fallunterscheidung einsetzen
- Kontrollstrukturen > Kann break und continue gezielt einsetzen
- Funktionen > Kann eigene Funktionen mit Parametern definieren

## Typ
Projekt

## Beschreibung
Baue ein Zahlenratespiel: Der Computer denkt sich eine Zufallszahl zwischen 1 und 100 aus. Der Spieler rät, und bekommt als Feedback "zu hoch", "zu niedrig" oder "richtig!". Das Spiel zählt die Versuche und gibt am Ende aus, wie viele Versuche gebraucht wurden.

Erweiterungen (optional, wenn Grundversion steht):
- Maximale Anzahl Versuche einbauen
- Mehrere Runden spielen können ("Nochmal? j/n")
- Schwierigkeitsgrade (Zahlenbereich ändern)

## Hinweise für Claude
<!-- Nicht dem Lernenden zeigen -->
- `import random` und `random.randint(1, 100)` muss erklärt werden — Lernender kennt Module noch nicht
- Gute Gelegenheit, Funktionen einzuführen: "Wie könntest du das Spiel als Funktion verpacken?"
- Erweiterungen nur vorschlagen wenn Grundversion sauber funktioniert
- Typischer Fehler: Endlosschleife weil break fehlt oder Bedingung falsch
- Bei "Nochmal?"-Erweiterung: while True mit break als Pattern einführen
