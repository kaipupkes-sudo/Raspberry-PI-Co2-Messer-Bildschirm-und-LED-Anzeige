---
name: skill-tree
description: Generiert oder aktualisiert skill_tree.yaml aus CURRICULUM.md
allowed-tools: Read, Write, Edit
---

# /skill-tree

## Zweck
Parst `CURRICULUM.md` und generiert oder aktualisiert `skill_tree.yaml`.
Die Visualisierung `skilltree.html` liest die YAML automatisch beim Öffnen — kein weiterer Schritt nötig.

## Ablauf

1. **Lies `CURRICULUM.md`** — extrahiere Titel, Themenblöcke, Skills und Bloom-Stufen
2. **Prüfe ob `skill_tree.yaml` existiert**
   - Existiert sie **nicht** → **Init**: generiere die Datei neu, alle Bloom-Stufen auf `false`
   - Existiert sie → **Update**: merge neue Konzepte hinzu, bestehender Fortschritt bleibt erhalten
3. **Schreibe `skill_tree.yaml`**
4. **Gib eine kurze Zusammenfassung** aus (siehe unten)

---

## CURRICULUM.md — Parsing-Regeln

Die Struktur folgt diesem Muster:

```
### 1 Kontrollstrukturen          → Topic   (id: "1")
#### 1.1 Entscheidungen           → Gruppierung — wird ignoriert
##### 1.1.1 if / elif / else      → Skill    (id: "1.1.1")
- **Erinnern** — ...              → Bloom-Stufe
- **Verstehen** — ...             → Bloom-Stufe
```

**Bloom-Stufen** werden erkannt an den Schlüsselwörtern (Groß-/Kleinschreibung ignorieren):
`Erinnern`, `Verstehen`, `Anwenden`, `Analysieren`, `Bewerten`, `Erschaffen`

**Ignoriere** Abschnitte mit Platzhalter-Titeln (erkennbar an `[N]`, `[Platzhalter]`, `Platzhalter` im Titel).

Der **Titel des Kurses** steht im YAML-Frontmatter unter `title:` in CURRICULUM.md — oder alternativ in der ersten `# Überschrift`.

---

## skill_tree.yaml — Zielstruktur

```yaml
title: Python & Raspberry Pi Grundlagen
topics:
  - id: "1"
    name: Kontrollstrukturen
    skills:
      - id: "1.1.1"
        name: if/elif/else
        self_rating: null
        bloom:
          erinnern:
            done: false
            completed_at: null
          verstehen:
            done: false
            completed_at: null
          anwenden:
            done: false
            completed_at: null
          analysieren:
            done: false
            completed_at: null
          bewerten:
            done: false
            completed_at: null
```

- `self_rating`: `null` | `"sitzt"` | `"geht so"` | `"unsicher"`
- `completed_at`: `null` oder Datum im Format `"YYYY-MM-DD"`
- Bloom-Stufen nur aufnehmen, die im CURRICULUM.md tatsächlich definiert sind (manche Skills haben nur 4, andere alle 6)

---

## Update-Logik

Beim Update gilt:

| Situation | Aktion |
|---|---|
| ID in CURRICULUM.md, nicht in YAML | Hinzufügen — alle Bloom-Stufen auf `false` |
| ID in beiden vorhanden | **Nicht anfassen** — Fortschritt bleibt erhalten |
| ID in YAML, nicht mehr in CURRICULUM.md | Nicht löschen — Hinweis in der Zusammenfassung ausgeben |

---

## Abschluss-Zusammenfassung

Gib am Ende aus:
- Modus: Init oder Update
- Anzahl Topics und Skills gesamt
- Bei Update: X neu hinzugefügt, Y bereits vorhanden
- Falls Skills in YAML aber nicht mehr im Curriculum: Liste diese auf

---
*Teil des experimentellen Lernplattform-Settings*