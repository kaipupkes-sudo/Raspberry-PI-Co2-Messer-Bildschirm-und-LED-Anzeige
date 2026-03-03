---
name: progress
description: Dokumentiert den Lernstand nach einer Session. Aktiviere wenn der Lernende /progress aufruft oder eine Session abgeschlossen wird.
allowed-tools: Read, Write, Edit
---


# /progress

## Zweck
Dokumentiere den Lernstand nach einer Session in `LERNPROFIL.md` und aktualisiere `curriculum.yaml`.
Wird explizit vom Lernenden aufgerufen — ein bewusster Abschluss der Session.

## Ablauf

1. **Lies die aktuelle `LERNPROFIL.md`** — was war bisher dokumentiert?
2. **Lies `curriculum.yaml`** — welche Kompetenzen existieren, was ist offen/done?
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
6. **Aktualisiere `curriculum.yaml`** — setze `status: done` für Kompetenzen, die der Lernende nachweislich beherrscht.
   Füge bei abgehakten Kompetenzen hinzu:
   - `completed: "DATUM"` — Datum der Session
   - `selfRating: sitzt | geht so | unsicher` — Selbsteinschätzung des Lernenden

   **YAML-Struktur zur Orientierung:**
   ```yaml
   - name: Kompetenzname
     status: done          # oder: open
     completed: "2026-02-28"
     selfRating: sitzt
     children:
       - name: Unterkompetenz
         status: open
   ```
   Kein Parsing nötig — die Struktur ist direkt editierbar.

7. **`skilltree.html` muss nicht mehr aktualisiert werden** — die Seite liest `curriculum.yaml` direkt beim Laden. Ein Reload der Seite zeigt den aktuellen Stand.

## Curriculum-Abgleich mit Selbsteinschätzung

Eine Kompetenz wird nur auf `status: done` gesetzt, wenn **zwei Bedingungen** erfüllt sind:

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
