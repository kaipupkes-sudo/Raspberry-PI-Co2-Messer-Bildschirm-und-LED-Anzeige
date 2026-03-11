---
name: initialize
description: Setzt den Lernfortschritt komplett zurück — LERNPROFIL.md und skill_tree.yaml werden auf den Ausgangszustand gesetzt.
allowed-tools: Read, Write, Edit, AskUserQuestion
---

# /initialize

## Zweck
Setzt den Lernfortschritt vollständig zurück — für einen Neustart mit einer neuen Lernenden-Person oder einem neuen Durchlauf.

**Was zurückgesetzt wird:**
- `LERNPROFIL.md` → leere Vorlage
- `skill_tree.yaml` → alle Bloom-Stufen auf `false`, alle `self_rating` auf `null`

**Was NICHT verändert wird:**
- `CURRICULUM.md` — Lerninhalte bleiben
- `aufgaben/` — Aufgaben bleiben
- `workspace/` — Dateien des Lernenden bleiben

---

## Ablauf

### Schritt 1 — Bestätigung einholen

**Frage explizit nach, bevor irgendetwas verändert wird:**

> „⚠️ Du bist dabei, den gesamten Lernfortschritt zurückzusetzen.
>
> Das löscht alle Einträge in LERNPROFIL.md und setzt den Skill Tree auf null.
> Diese Aktion kann nicht rückgängig gemacht werden.
>
> Wirklich fortfahren? (ja / nein)"

Nur bei eindeutigem **„ja"** weitermachen. Bei allem anderen abbrechen und bestätigen dass nichts verändert wurde.

---

### Schritt 2 — LERNPROFIL.md zurücksetzen

Schreibe die Datei mit dieser leeren Vorlage:

```markdown
# Lernprofil

## Letzte Session
- **Datum:** —
- **Thema:** —
- **Zusammenfassung:** —

## Beherrschte Konzepte

(noch keine)

## Schwierigkeiten / Wissenslücken

(noch keine dokumentiert)

## Nächste Lernziele

(noch nicht gesetzt)

## Fortschritt im Curriculum

(noch kein Fortschritt)

## Bearbeitete Aufgaben

(noch keine)

## Individuelle Lernziele

(noch keine)

---
*Wird aktualisiert mit /progress*
```

---

### Schritt 3 — skill_tree.yaml zurücksetzen

1. **Lies `skill_tree.yaml`** — übernehme die vorhandene Struktur (Topics, Skills, Bloom-Stufen)
2. **Setze für jeden Skill:**
   - `self_rating: null`
   - Jede Bloom-Stufe: `done: false`, `completed_at: null`
3. **Schreibe die aktualisierte Datei**

Die Struktur (Topics, Skill-IDs, Bloom-Stufen) bleibt identisch — nur die Fortschrittsdaten werden geleert.

---

### Schritt 4 — Abschluss

Gib eine kurze Bestätigung aus:

> „Lernfortschritt wurde zurückgesetzt.
> - LERNPROFIL.md: geleert
> - skill_tree.yaml: X Skills auf null gesetzt
>
> Bereit für einen Neustart."

---
*Teil des experimentellen Lernplattform-Settings*
