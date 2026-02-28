---
name: progress
description: Dokumentiert den Lernstand nach einer Session. Aktiviere wenn der Lernende /progress aufruft oder eine Session abgeschlossen wird.
allowed-tools: Read, Write
---


# /progress

## Zweck
Dokumentiere den Lernstand nach einer Session in der `LERNPROFIL.md`.
Wird explizit vom Lernenden aufgerufen — ein bewusster Abschluss der Session.

## Ablauf

1. **Lies die aktuelle `LERNPROFIL.md`** im Projektverzeichnis — was war bisher dokumentiert?
2. **Schau die Session durch** — was wurde besprochen, was hat funktioniert, wo gab es Schwierigkeiten?
3. **Stelle dem Lernenden zwei kurze Fragen:**
   - „Was hast du heute verstanden, das vorher unklar war?"
   - „Was ist noch offen oder fühlt sich unsicher an?"
4. **Aktualisiere `LERNPROFIL.md`** im Projektverzeichnis mit den Antworten und deiner eigenen Einschätzung
5. **Formuliere 1–2 konkrete Lernziele** für die nächste Session

## Schreibprinzipien

- Konkret und knapp — keine langen Texte
- Ehrlich: Wenn etwas noch nicht sitzt, steht es unter Wissenslücken — nicht unter beherrschten Konzepten
- Kumulativ: Bestehende Einträge werden ergänzt, nicht überschrieben — außer etwas hat sich eindeutig verbessert
- Datum immer aktualisieren

## Beispiel-Output (LERNPROFIL.md nach /progress)

```
## Letzte Session
- Datum: 2026-02-24
- Thema: for-Schleifen in Python
- Zusammenfassung: range() verstanden, hat selbst eine Schleife geschrieben die Zahlen ausgibt

## Beherrschte Konzepte
- Variablen und Zuweisung
- for-Schleifen mit range()

## Schwierigkeiten / Wissenslücken
- Unterschied while vs. for noch unklar
- Einrückung vergisst der Lernende manchmal

## Nächste Lernziele
- while-Schleifen einführen und mit for vergleichen
- Eine kleine Aufgabe lösen die beide Schleifentypen braucht
```

---
*Teil des experimentellen Lernplattform-Settings*
