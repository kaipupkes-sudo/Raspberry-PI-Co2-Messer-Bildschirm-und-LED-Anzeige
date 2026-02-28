# Aufgabe: Passwort-Prüfung

## Kompetenz
- Kontrollstrukturen > Kann if/elif/else zur Fallunterscheidung einsetzen
- Kontrollstrukturen > Kann while-Schleife mit Abbruchbedingung schreiben

## Typ
Übung

## Beschreibung
Schreibe ein Programm, das den Benutzer nach einem Passwort fragt. Wenn das Passwort richtig ist (z.B. "geheim123"), wird "Zugang gewährt" ausgegeben. Wenn es falsch ist, darf der Benutzer es erneut versuchen — aber maximal 3 Mal. Nach 3 Fehlversuchen: "Zugang gesperrt".

## Hinweise für Claude
<!-- Nicht dem Lernenden zeigen -->
- Braucht einen Zähler für Versuche — gute Gelegenheit, Variable als Zustandsspeicher zu üben
- while-Bedingung muss zwei Dinge prüfen: Versuche UND ob noch nicht richtig
- Typischer Fehler: break vergessen oder an falscher Stelle
- Wenn Lernender `and` nutzt ohne es zu kennen: kurz thematisieren, nicht überspringen
