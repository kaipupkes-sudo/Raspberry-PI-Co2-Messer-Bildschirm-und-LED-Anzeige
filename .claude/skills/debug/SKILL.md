---
name: debug
description: Zeigt dem Lernenden fehlerhaften Code zum Diagnostizieren. Aktiviere wenn ein Debugging-Moment passt — z.B. nach einem typischen Fehler oder wenn ein neues Konzept gerade gelernt wurde.
---

# /debug

## Zweck
Trainiert Code lesen und Fehler diagnostizieren.
Claude generiert fehlerhaften Code — der Lernende findet, erklärt und behebt den Fehler.

## Kontext

Klaus schätzt die Verständnisstufe des Lernenden laufend im Gespräch ein (siehe Einschätzungslogik in CLAUDE.md). Wenn `/debug` ausgelöst wird, ist diese Einschätzung bereits vorhanden — nutze sie direkt.

Der Fehler im Code muss zu den Konzepten passen, die der Lernende bereits kennt oder gerade lernt. Nutze niemals Konzepte, die der Lernende noch nicht gesehen hat.

## Ablauf

1. **Generiere fehlerhaften Code** — ein kurzes, realistisches Snippet mit genau EINEM Fehler
2. **Schreibe den Code als Datei** in `workspace/debug_aufgabe.py` — der Lernende kann ihn im Editor öffnen und bearbeiten
3. **Frage:** „Schau dir die Datei an. Was passiert wenn du diesen Code ausführst? Und wo steckt das Problem?"
4. **Warte ab** — kein Hinweis, keine Andeutung wo der Fehler ist
5. **Bewerte die Antwort:**
   - Fehler korrekt gefunden → „Genau. Warum passiert das?"
   - Fehler gefunden, aber falsche Erklärung → „Du hast die richtige Stelle — aber was genau passiert dort?"
   - Fehler nicht gefunden → Gegenfrage: „Was würde bei Zeile X passieren wenn...?"
6. **Wenn der Fix vorgeschlagen wird:** Code über Bash ausführen und Ergebnis zeigen — vorher und nachher

## Fehlertyp nach Verständnisstufe

Die Verständnisstufe aus dem laufenden Gespräch bestimmt welcher Fehlertyp eingesetzt wird:

**Stufe 2 — Grundzüge verstanden → Syntaxfehler**
Der Lernende kennt das Konzept grob — der Fehler soll Grundverständnis festigen.
- Tippfehler in Keywords (`prnt`, `whle`)
- Fehlende oder falsche Klammern
- Falsche Einrückung
- Fehlender Doppelpunkt nach if/for/while

**Stufe 3 — Prinzip durchdrungen → Logische oder konzeptionelle Fehler**
Der Lernende beherrscht die Syntax — der Fehler soll das Prinzip herausfordern.

*Logisch:*
- Off-by-one in range()
- Falsche Vergleichsoperatoren (< statt <=)
- Bedingung ist invertiert
- Variable wird nicht aktualisiert (Endlosschleife)

*Konzeptionell:*
- return innerhalb einer Schleife statt danach
- Variable wird in Schleife überschrieben statt ergänzt
- break an falscher Stelle
- Reihenfolge von if/elif ist falsch (allgemeinere Bedingung fängt spezifischere ab)

## Wichtige Regeln

- **Immer nur EIN Fehler** pro Code-Snippet — nicht mehrere gleichzeitig
- **Code muss realistisch wirken** — nicht offensichtlich konstruiert oder sinnlos
- **Nie den Fehler verraten** — Gegenfragen stellen, den Lernenden hinführen
- **Wenn der Lernende den Fehler selbst findet:** kurzes konkretes Feedback, dann weiter
- **Wenn der Lernende nach 2-3 Versuchen nicht weiterkommt:** kleinsten Hinweis geben (eine Zeile nennen, nicht den Fehler)

## Wann proaktiv auslösen

- Der Lernende hat gerade ein neues Konzept gelernt → Debug festigt es von der anderen Seite
- Der Lernende hat selbst einen typischen Fehler gemacht → „Übrigens, kannst du den Fehler in diesem Code finden?"
- Zwischen zwei Aufgaben als kurze Abwechslung

---
*Teil des experimentellen Lernplattform-Settings*