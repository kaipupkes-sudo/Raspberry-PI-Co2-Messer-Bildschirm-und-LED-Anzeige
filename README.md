# IIoT-Lernbegleiter

Ein experimentelles Lernumgebungs-Setting für Claude Code — entwickelt an der TUHH.

---

## Konzept

Dieses Projekt nutzt Claude Code als strukturierten Lernbegleiter für Auszubildende. Claude agiert als Ausbilder ("Klaus") und führt Lernende durch ein praxisnahes IIoT-Projekt auf einem Raspberry Pi — vom ersten Codeabschnitt bis zum fertigen CO₂- und Raumklima-Monitor.

Die Pädagogik ist in `CLAUDE.md` definiert: kein Lösungslieferant, sondern ein Tutor der mit Fragen führt, Verständnis aufbaut und Lernfortschritt dokumentiert.

---

## Projektrahmen

Ein Hardware-Hersteller hat einen Raspberry Pi im Einsatz, der auf Knopfdruck eine LED schaltet. Der verantwortliche Entwickler hat das Unternehmen verlassen — der hinterlassene Code ist unkommentiert und nicht wartbar. Auszubildende übernehmen den Auftrag: Code analysieren, aufräumen und schrittweise zu einem vollständigen Raumklima-Monitor ausbauen.

Der Ausgangscode liegt in `workspace/produkt.py`.

---

## Struktur

| Datei / Ordner | Inhalt |
|---|---|
| `CLAUDE.md` | Verhaltens- und Pädagogikregeln für Claude |
| `CURRICULUM.md` | Lerninhalte, Meilensteine, Bloom-Taxonomie |
| `skill_tree.yaml` | Kompetenzstand des Lernenden (wird automatisch gepflegt) |
| `LERNPROFIL.md` | Individueller Fortschritt und Lernziele |
| `GLOSSAR.md` | Automatisch gepflegtes Fachbegriff-Glossar |
| `workspace/` | Arbeitsbereich des Lernenden |
| `aufgaben/` | Aufgaben die Klaus situativ einsetzen kann |
| `skilltree.html` | Visuelle Darstellung des Kompetenzstands |

---

## Skills (Commands)

Lernende können folgende Commands im Chat aufrufen:

| Command | Funktion |
|---|---|
| `/quiz` | Verständnisfragen zum aktuellen Thema |
| `/üben` | Praktische Aufgabe auf aktuellem Niveau |
| `/challenge` | Anspruchsvolle Aufgabe ohne Hilfestellung |
| `/debug` | Fehlerhaften Code analysieren und korrigieren |
| `/tipp` | Gezielter Hinweis ohne Lösungsverraten |
| `/progress` | Lernstand dokumentieren (LERNPROFIL + skill_tree) |
| `/continue` | Wiedereinstieg nach geschlossenem Kontext |

---

## Technisches

- Basiert auf Claude Code mit `CLAUDE.md` als Verhaltenssteuerung
- Skills sind als Markdown-Dateien in `.claude/commands/` definiert
- `skill_tree.yaml` wird von `skilltree.html` direkt beim Laden eingelesen
- Lernfortschritt liegt ausschließlich lokal — keine externe Datenhaltung

---

*Dieses Setting ist ein Experiment: Kann Claude Code als strukturierte Lernumgebung funktionieren?*
