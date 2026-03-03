## skills
- Werden automatisch durch claude ausgeführt, wenn claude denkt dass es passt.


## commands
- werden vom user getriggert.

## allowed-tools
Read — Dateien lesen. Braucht /progress um LERNPROFIL.md und CURRICULUM.md einzulesen.

Edit — Gezielte Änderungen in bestehenden Dateien. Ersetzt einen bestimmten Textblock durch einen anderen. Gut für: "Ändere den Fortschritt von 2/5 auf 3/5". Schickt nur den Diff, nicht die ganze Datei.

Write — Ganze Datei überschreiben. Schreibt den kompletten Inhalt neu. Nötig wenn eine Datei komplett neu erstellt wird oder so viele Änderungen nötig sind, dass Edit unpraktisch wäre.

Bash — Shell-Befehle ausführen. Bräuchte /progress eigentlich nicht — es liest und schreibt nur Markdown-Dateien, keine Systembefehle nötig.

---
## Vorgehen weiter

Was du beschreibst ist im Grunde ein zweistufiger Workflow:


Lehrperson bearbeitet CURRICULUM.md
        ↓
/update-curriculum (Lehrer-Agent)
  1. Liest CURRICULUM.md + curriculum.yaml
  2. Zeigt Diff: "Diese Einträge sind neu: ..."
  3. Lehrperson bestätigt
  4. Fügt neue Einträge als status: open in curriculum.yaml ein
  5. "Seite neu laden — Skill Tree zeigt bereits den neuen Stand"
Da der Skill Tree jetzt live aus YAML lädt, fällt Schritt 5 fast komplett weg.

Zum Python-Skript: Ja, sinnvoll — aber nur für den mechanischen Diff-Teil. Das Skript findet neue Einträge in CURRICULUM.md die noch nicht in curriculum.yaml stehen. Der Agent ruft das Skript auf, interpretiert das Ergebnis, und fragt die Lehrperson interaktiv.

In Claude Code wäre das dann eine neue Command-Datei:


.claude/commands/update-curriculum.md
Mit allowed-tools: Read, Write, Edit, Bash damit der Agent das Python-Skript ausführen kann.

