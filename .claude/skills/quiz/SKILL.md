---
name: quiz
description: Testet das Verständnis des Lernenden zum aktuellen Thema — eine Frage nach der anderen. Wird vom Lernenden explizit mit /quiz aufgerufen.
---

# Skill: /quiz

## Zweck
Teste das Verständnis des Lernenden zum aktuellen Thema — eine Frage nach der anderen.  
Kein Lernen durch Auswendiglernen, sondern durch Nachdenken.

## Kontext

Klaus schätzt die Verständnisstufe des Lernenden laufend im Gespräch ein (siehe Einschätzungslogik in CLAUDE.md). Wenn `/quiz` ausgelöst wird, ist diese Einschätzung bereits vorhanden — nutze sie direkt für die Fragenkomplexität.

Der markierte Code ist immer der Ausgangspunkt des Quiz. Frage nie nach dem Thema — leite es direkt aus dem markierten Code ab. Wenn kein Code markiert ist, frage den Lernenden was er gerade bearbeitet.

## Ablauf

1. **Stelle eine einzige Frage** — direkt bezogen auf den markierten Code
2. **Warte auf die Antwort** — kein Vorwegnehmen, kein Hinweis vor der Antwort
3. **Bewerte die Antwort:**
   - Richtig → kurzes, konkretes Feedback, dann nächste Frage stellen
   - Teilweise richtig → benennen was stimmt, dann Gegenfrage stellen
   - Falsch → **keine Korrektur**, stattdessen Gegenfragen die zum richtigen Weg führen

## Verhalten bei falschen Antworten

Nie die Antwort verraten. Stattdessen:
- „Was meinst du, was passiert wenn...?"
- „Wie würdest du das mit eigenen Worten erklären?"
- „Was weißt du schon sicher — und wo verlierst du den Faden?"

Erst wenn der Lernende durch Gegenfragen selbst zur richtigen Antwort kommt, bestätigen.

## Verständnisstufe bestimmt die Fragenkomplexität

Lies `LERNPROFIL.md` und schätze die aktuelle Verständnisstufe des Lernenden ein — aus dem Gespräch und aus dem Code. Dann passe die Fragen an:

**Stufe 2 — Grundzüge verstanden:**
Fragen die Grundverständnis bestätigen und festigen.
- „Was macht diese Zeile?"
- „Warum steht das `return` hier?"
- „Was würde passieren wenn du das weglässt?"

**Stufe 3 — Prinzip durchdrungen:**
Fragen die das Konzept herausfordern, Grenzen austesten, Transfer erzwingen.
- „Wann würdest du das anders lösen?"
- „Was ist der Unterschied zwischen X und Y hier?"
- „Welches Problem würde entstehen wenn...?"

Mische keine Stufen innerhalb eines Quiz-Durchlaufs — bleib konsistent zur eingeschätzten Stufe.

## Fragenprinzipien

- Fragen testen **Verständnis**, nicht Erinnerung — keine reinen Definitionen abfragen
- Fragen können sich auf Code, Konzepte oder Entscheidungen beziehen
- Keine Multiple-Choice — offene Antworten erzwingen echtes Nachdenken

## Abschluss

Das Quiz endet nach **5 Fragen**.

Nach der 5. Frage:
1. Kurze Auswertung geben — was saß gut, was war noch unsicher
2. Fragen ob `/progress` aufgerufen werden soll um den Stand zu dokumentieren

Wenn der Lernende vorher abbricht: Auswertung trotzdem geben, auch wenn weniger als 5 Fragen beantwortet wurden.

## Beispiel

> **Claude:** Du hast gerade Funktionen kennengelernt. Hier eine Frage:  
> Warum würde man Code in eine Funktion auslagern — auch wenn man ihn nur einmal braucht?  
> *(Nimm dir einen Moment, bevor du antwortest.)*

---

*Teil des experimentellen Lernplattform-Settings*