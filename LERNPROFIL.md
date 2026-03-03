# Lernprofil

## Letzte Session
- **Datum:** 2026-03-02
- **Thema:** Progress-Check — keine neue Lernsession
- **Zusammenfassung:** Kein neues Thema erarbeitet. Progress-Check aufgerufen, um Stand zu dokumentieren. Singleton Pattern als individuelles Interesse genannt (liegt außerhalb des aktuellen Curriculums).

## Vorherige Session (2026-02-28)
- **Thema:** Zahlenratespiel — while-Schleife, import random, input() mit int()
- **Zusammenfassung:** Aufgabe 04_zahlenratespiel eigenständig gebaut. Hat while-Schleife mit Boolean-Flag (`go_on`) als Abbruchbedingung eigenständig konstruiert. `import random` und `random.randint()` selbst recherchiert. Off-by-one-Fehler bei `randint(1, 101)` (inklusiv vs. exklusiv) und Zähler-Fehler eigenständig erkannt und behoben. Selbsteinschätzung while-Schleife: Sitzt.

## Beherrschte Konzepte
- while-Schleife: Grundprinzip verstanden (läuft solange Bedingung True ist)
- while-Schleife mit Abbruchbedingung: eigenständig in Zahlenratespiel umgesetzt mit Boolean-Flag, Selbsteinschätzung: Sitzt
- Endlosschleife: erkennt, dass fehlende Abbruchbedingung das Problem ist
- for-Schleife mit `range()`: Syntax verstanden, selbst geschrieben
- `range()`: 1 Parameter (0 bis n-1, genau n Elemente), 2 Parameter (start inkl., ende exkl.) — präzise erklärt
- Boolean als Typ: `True`/`False` als eigene Wertkategorie verstanden (nicht Zahl, nicht Text)
- Boolean-Variable als Zustandsspeicher: in Zahlenratespiel eigenständig eingesetzt (`go_on = True/False`)
- Modulo-Operator `%`: selbst angewendet zur Teilbarkeitsprüfung, in FizzBuzz sicher genutzt
- if/elif/else: Fallunterscheidung eigenständig aufgebaut, Reihenfolge der Bedingungen verstanden und begründet (Selbsteinschätzung: Sitzt)
- Truthy/Falsy: verstanden dass `0` falsy ist — hat Konsequenz für `i % 3` selbst erkannt
- `break` in for-Schleife: korrekt eingesetzt, Zweck verstanden (sofortiger Abbruch)
- `break` vs. `return`: break bricht nur ab, return gibt zusätzlich Wert zurück — selbst formuliert
- `return` außerhalb Funktion: weiß dass das ein SyntaxError ist und warum
- `import random`, `random.randint(a, b)`: selbst recherchiert, inklusiven Bereich verstanden
- `input()` mit `int()`-Konvertierung: eingesetzt, aber noch nicht sicher (siehe Wissenslücken)

## Schwierigkeiten / Wissenslücken
- `input()` mit Typkonvertierung: `int(input(...))` genutzt, aber fühlt sich noch unsicher an — Fehlerverhalten bei falscher Eingabe unbekannt
- Woher kommen Booleans? (z.B. dass `3 > 2` selbst `True` ergibt) — noch nicht thematisiert
- Boolean-Operatoren (`and`, `or`, `not`) — `and` in FizzBuzz genutzt, aber noch nicht explizit thematisiert
- `break` in while-Schleife: nicht eingesetzt — hat stattdessen Boolean-Flag genutzt; offen ob Übertrag gelingt
- `continue`: noch nicht thematisiert

## Nächste Lernziele
- `break` in while-Schleife ausprobieren — selbst herausfinden ob es gleich funktioniert wie Boolean-Flag
- `input()` und Typkonvertierung vertiefen — was passiert bei falscher Eingabe?

## Fortschritt im Curriculum
- Kontrollstrukturen: 3/5
- Funktionen: 0/3
- Datenstrukturen: 0/3

## Bearbeitete Aufgaben
- 03_fizzbuzz: gelöst (2026-02-28) — eigenständig, fehlerfrei
- 04_zahlenratespiel: gelöst (2026-02-28) — eigenständig, inkl. Fehlerkorrektur bei randint und Zähler

## Individuelle Lernziele
- **Singleton Pattern**: Interesse geäußert (2026-03-02) — Design Pattern, liegt außerhalb Python Grundlagen; kann nach Abschluss von Funktionen aufgegriffen werden

---
*Wird aktualisiert mit /progress*
