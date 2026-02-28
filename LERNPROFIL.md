# Lernprofil

## Letzte Session
- **Datum:** 2026-02-28
- **Thema:** `break`, Truthy/Falsy, Unterschied `break` vs. `return`
- **Zusammenfassung:** Challenge: erste Zahl 1–50 finden, die durch 3 und 7 teilbar ist. Hat `break` korrekt platziert, aber die Modulo-Bedingung falsch (dachte `i % 3` gibt `True` zurück wenn teilbar — selbst korrigiert als er verstanden hat, dass 0 falsy ist). Hat dann selbst erklärt: `break` bricht ab, `return` gibt zusätzlich einen Wert zurück. Kurzer Ausflug zu Funktionen: `return` außerhalb einer Funktion = SyntaxError.

## Beherrschte Konzepte
- while-Schleife: Grundprinzip verstanden (läuft solange Bedingung True ist)
- Endlosschleife: erkennt, dass fehlende Abbruchbedingung das Problem ist
- for-Schleife mit `range()`: Syntax verstanden, selbst geschrieben
- `range()`: 1 Parameter (0 bis n-1, genau n Elemente), 2 Parameter (start inkl., ende exkl.) — präzise erklärt
- Boolean als Typ: `True`/`False` als eigene Wertkategorie verstanden (nicht Zahl, nicht Text)
- Boolean-Variable als Zustandsspeicher: erkennt, dass zwei Zustände → Boolean sinnvoller als Zähler
- Modulo-Operator `%`: selbst angewendet zur Teilbarkeitsprüfung
- Truthy/Falsy: verstanden dass `0` falsy ist — hat Konsequenz für `i % 3` selbst erkannt
- `break` in for-Schleife: korrekt eingesetzt, Zweck verstanden (sofortiger Abbruch)
- `break` vs. `return`: break bricht nur ab, return gibt zusätzlich Wert zurück — selbst formuliert
- `return` außerhalb Funktion: weiß dass das ein SyntaxError ist und warum

## Schwierigkeiten / Wissenslücken
- Boolean in eigenem Code noch nicht eingesetzt — working solution nutzte Zähler
- Woher kommen Booleans? (z.B. dass `3 > 2` selbst `True` ergibt) — noch nicht thematisiert
- Boolean-Operatoren (`and`, `or`, `not`) — `and` heute genutzt, aber noch nicht explizit thematisiert
- `break` in while-Schleife: noch nicht gesehen — offen ob Übertrag gelingt

## Nächste Lernziele
- `break` in while-Schleife anwenden — selbst herausfinden ob es gleich funktioniert
- Boolean-Ausdrücke: Vergleiche als Quelle von `True`/`False` (z.B. `x > 5`, `name == "Ben"`)

---
*Wird aktualisiert mit /progress*
