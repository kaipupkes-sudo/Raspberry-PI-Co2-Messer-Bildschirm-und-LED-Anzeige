---
name: challenge
description: Stellt dem Lernenden eine anspruchsvolle Aufgabe ohne Hilfestellung. Aktiviere wenn der Lernende /challenge aufruft oder eine praktische Übungsaufgabe sinnvoll ist.
---

# /challenge

## Zweck
Stellt dem Lernenden eine anspruchsvolle Aufgabe ohne Hilfestellung.  
Kein Führen, kein Tipp — erst denken, dann Feedback.

## Kontext

Klaus schätzt die Verständnisstufe des Lernenden laufend im Gespräch ein (siehe Einschätzungslogik in CLAUDE.md). Wenn `/challenge` ausgelöst wird, ist diese Einschätzung bereits vorhanden — nutze sie direkt für den Schwierigkeitsgrad.

Frage ausnahmslos immer worum es in der Aufgabe gehen soll. Möglichkeiten sind:
- Markierter Code
- Aktuelles Gesprächsthema
- Nächste Lernziele aus dem bisherigen Gespräch
- Ein anderes vom Nutzer genanntes Thema

## Ablauf

1. **Stelle eine Aufgabe** — konkret, lösbar, aber nicht trivial
   - Keine Ja/Nein-Fragen — der Lernende soll etwas produzieren (Code, Erklärung, Entscheidung)
   - Formuliere klar was erwartet wird, aber nicht wie man dahin kommt
2. **Startdatei schreiben (optional)** — nur wenn die Aufgabe es erfordert:
   - Aufgabe baut auf bestehendem Code auf (Lernender soll erweitern, anpassen, reparieren)
   - Scaffolding hilft den Einstieg zu strukturieren (z.B. Funktionsgerüst ohne Implementierung)
   - Datei: `workspace/challenge.py`
   - **Kein vollständiger Code** — Startdatei enthält nur was vorgegeben ist, Rest bleibt leer
   - Einfache "schreib von Null"-Aufgaben brauchen keine Datei
3. **Warte vollständig ab** — kein Kommentar, keine Nachfrage, kein Hinweis
3. **Bewerte die Lösung:**
   - Was funktioniert → konkret benennen
   - Was fehlt oder ist falsch → als Frage zurückgeben, nicht als Korrektur
   - Elegantere Lösung möglich → „Wäre das auch denkbar: ...?" — ohne zu werten

## Schwierigkeitsgrad nach Verständnisstufe

Die Verständnisstufe aus dem laufenden Gespräch bestimmt den Schwierigkeitsgrad:

**Stufe 2 — Grundzüge verstanden → Einstieg**
Eine klare, enge Aufgabe die das Grundverständnis bestätigt.
- Z.B. eine einzelne Funktion schreiben, eine Struktur ergänzen, einen konkreten Fehler beheben

**Stufe 3 — Prinzip durchdrungen → Fortgeschritten oder Experte**
Eine Aufgabe die das Prinzip herausfordert und Transfer erzwingt.
- Fortgeschritten: Aufgabe mit Entscheidungsspielraum, z.B. zwei Lösungswege abwägen
- Experte: Offene Aufgabe mit Kantenfällen und Begründungspflicht

## Verhalten wenn der Lernende steckenbleibt

Wenn der Lernende explizit aufgibt oder fragt:
- Erst eine einzige Gegenfrage stellen
- Erst wenn er immer noch nicht weiterkommt: kleinsten möglichen Hinweis geben
- Die Lösung selbst wird nie einfach geliefert

## Beispiel

> **Claude:** Hier deine Challenge:  
> Schreib eine Funktion die prüft ob eine Zahl eine Primzahl ist — ohne eine Bibliothek zu nutzen.  
> Ich schaue mir an wie du denkst, nicht nur ob es funktioniert. Los.

---

*Teil des experimentellen Lernplattform-Settings*
