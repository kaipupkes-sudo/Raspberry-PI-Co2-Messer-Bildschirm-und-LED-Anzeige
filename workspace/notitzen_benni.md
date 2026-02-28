## skills
- Werden automatisch durch claude ausgeführt, wenn claude denkt dass es passt.


## commands
- werden vom user getriggert.

## allowed-tools
Read — Dateien lesen. Braucht /progress um LERNPROFIL.md und CURRICULUM.md einzulesen.

Edit — Gezielte Änderungen in bestehenden Dateien. Ersetzt einen bestimmten Textblock durch einen anderen. Gut für: "Ändere den Fortschritt von 2/5 auf 3/5". Schickt nur den Diff, nicht die ganze Datei.

Write — Ganze Datei überschreiben. Schreibt den kompletten Inhalt neu. Nötig wenn eine Datei komplett neu erstellt wird oder so viele Änderungen nötig sind, dass Edit unpraktisch wäre.

Bash — Shell-Befehle ausführen. Bräuchte /progress eigentlich nicht — es liest und schreibt nur Markdown-Dateien, keine Systembefehle nötig.