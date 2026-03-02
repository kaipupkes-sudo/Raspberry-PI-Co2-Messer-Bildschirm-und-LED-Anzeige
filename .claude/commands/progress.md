---
name: progress
description: Dokumentiert den Lernstand nach einer Session. Aktiviere wenn der Lernende /progress aufruft oder eine Session abgeschlossen wird.
allowed-tools: Read, Write, Edit
---


# /progress

## Zweck
Dokumentiere den Lernstand nach einer Session in `LERNPROFIL.md` und gleiche ihn mit `CURRICULUM.md` ab.
Wird explizit vom Lernenden aufgerufen — ein bewusster Abschluss der Session.

## Ablauf

1. **Lies die aktuelle `LERNPROFIL.md`** — was war bisher dokumentiert?
2. **Lies `CURRICULUM.md`** — welche Kompetenzen sind definiert?
3. **Schau die Session durch** — was wurde besprochen, was hat funktioniert, wo gab es Schwierigkeiten?
4. **Stelle dem Lernenden zwei kurze Fragen:**
   - „Was hast du heute verstanden, das vorher unklar war?"
   - „Was ist noch offen oder fühlt sich unsicher an?"
5. **Aktualisiere `LERNPROFIL.md`** mit den Antworten und deiner eigenen Einschätzung:
   - Letzte Session (Datum, Thema, Zusammenfassung)
   - Beherrschte Konzepte (ergänzen)
   - Schwierigkeiten / Wissenslücken (aktualisieren)
   - Nächste Lernziele (1–2 konkrete)
   - **Fortschritt im Curriculum** — Zähler pro Themenblock aktualisieren
   - **Bearbeitete Aufgaben** — wenn Aufgaben aus `aufgaben/` bearbeitet wurden, Status dokumentieren
   - **Individuelle Lernziele** — frage ob der Lernende eigene Ziele hat, die nicht im Curriculum stehen
6. **Aktualisiere `CURRICULUM.md`** — setze Checkboxen (`- [x]`) für Kompetenzen, die der Lernende nachweislich beherrscht

7. **Aktualisiere `skilltree.html`** — regeneriere den JSON-Datenblock basierend auf dem neuen Stand von `CURRICULUM.md`:

   **Parsing-Regeln für CURRICULUM.md:**
   - `### N. TopicName` → Themenblock (`type: "topic"`)
   - `- [x] Text` (keine Einrückung) → Kompetenz, `status: "done"`
   - `- [ ] Text` (keine Einrückung) → Kompetenz, `status: "open"`
   - `  - [x] Text` (2-Leerzeichen-Einrückung) → Unterkompetenz der vorherigen Hauptkompetenz, `status: "done"`
   - `  - [ ] Text` (2-Leerzeichen-Einrückung) → Unterkompetenz, `status: "open"`

   **Kürze die Kompetenztexte** für den Skill Tree — entferne "Kann ", "Versteht ", trailing phrases wie " zur Iteration nutzen". Behalte den Kernbegriff (z.B. "for-Schleife mit range()", "return vs. print").

   **JSON-Struktur:**
   ```json
   {
     "name": "Python Grundlagen",
     "type": "root",
     "children": [
       {
         "name": "Themenblock",
         "type": "topic",
         "children": [
           {
             "name": "Kurzname der Kompetenz",
             "type": "skill",
             "status": "done",
             "children": [
               { "name": "Unterkompetenz", "type": "skill", "status": "open" }
             ]
           }
         ]
       }
     ]
   }
   ```

   **Ersetze** in `skilltree.html` den JSON-Inhalt zwischen den Kommentaren:
   `<!-- CURRICULUM DATA — wird von /progress aktualisiert -->` und `<!-- END CURRICULUM DATA -->`
   (schreibe dabei den öffnenden `<script type="application/json" id="curriculum-data">` und schließenden `</script>`-Tag mit neu).

## Curriculum-Abgleich mit Selbsteinschätzung

Eine Kompetenz wird nur abgehakt, wenn **zwei Bedingungen** erfüllt sind:

1. **Du** bewertest die Kompetenz als selbstständig angewendet
2. **Der Lernende** schätzt sich selbst als "Sitzt" ein

### Selbsteinschätzung erfragen

Für jede Kompetenz, die du als beherrscht einschätzt, frage den Lernenden:

> „Du hast heute [Kompetenz] eigenständig eingesetzt. Wie sicher fühlst du dich damit?"
> - **Unsicher** — „Ich bräuchte nochmal Hilfe"
> - **Geht so** — „Ich könnte es, aber müsste nachdenken"
> - **Sitzt** — „Das kann ich"

### Auswertung

| Du sagst | Lernender sagt | Ergebnis |
|---|---|---|
| Beherrscht | Sitzt | Kompetenz abhaken |
| Beherrscht | Geht so | Offen lassen — nächste Session vertiefen |
| Beherrscht | Unsicher | Offen lassen — Diskrepanz notieren, gezielt nachfragen |
| Nicht beherrscht | Sitzt | Nachfragen — „Kannst du mir erklären, wie...?" |

### Dokumentation

- **Begründe jede Abhakung kurz** im LERNPROFIL.md (z.B. "for-Schleife: eigenständig in Aufgabe 01 eingesetzt, Selbsteinschätzung: Sitzt")
- Dokumentiere auch die Selbsteinschätzung bei Kompetenzen, die noch offen bleiben
- Der Abgleich gibt dem Lernenden (und der Lehrperson) einen Überblick, wo er im Gesamtbild steht

## Schreibprinzipien

- Konkret und knapp — keine langen Texte
- Ehrlich: Wenn etwas noch nicht sitzt, steht es unter Wissenslücken — nicht unter beherrschten Konzepten
- Kumulativ: Bestehende Einträge werden ergänzt, nicht überschrieben — außer etwas hat sich eindeutig verbessert
- Datum immer aktualisieren

---
*Teil des experimentellen Lernplattform-Settings*
