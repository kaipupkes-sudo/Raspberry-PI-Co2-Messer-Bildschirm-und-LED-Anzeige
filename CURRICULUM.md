---
ausbildungsberuf: Fachinformatiker Systemintegration
lehrjahr: 1
lernfeld: LF 7 — Cyberphysische Systeme
zeitraum: 3 Wochen Blockunterricht
programmiersprache: Python
hardware: Raspberry Pi, Sensoren, Aktoren
version: 0.1
---

# Curriculum — Python & Raspberry Pi Grundlagen

## Überblick

### Projektbeschreibung

[Wird von der Lehrkraft gepflegt — kurze Beschreibung des Projekts das die SuS über den Kurs hinweg entwickeln]

### Lernziele

Am Ende des Kurses können die Lernenden:

- Ein hardwarenahe Python-Programm eigenständig entwickeln und strukturieren
- Sensordaten einlesen, verarbeiten und auf Basis dieser Daten Aktoren ansteuern
- Kontrollstrukturen, Funktionen und Datenstrukturen situationsgerecht einsetzen
- Eigene Lösungsansätze begründen und mit alternativen Ansätzen vergleichen
- Code lesbar, wartbar und sinnvoll strukturiert schreiben

### Hinweise für die Lehrkraft

[Pädagogische Hinweise, Besonderheiten der Lerngruppe, Differenzierung]

---

## Themenblöcke

### 1 Kontrollstrukturen

#### 1.1 Entscheidungen

##### 1.1.1 if / elif / else

- **Erinnern** — Kennt die Syntax von if, elif und else und kann sie aufschreiben
- **Verstehen** — Erklärt den Unterschied zwischen if-elif und mehreren if-Blöcken hintereinander
- **Anwenden** — Setzt if/elif/else eigenständig zur Fallunterscheidung ein
- **Analysieren** — Begründet warum eine bestimmte Reihenfolge der Bedingungen notwendig ist
- **Bewerten** — Entscheidet ob elif oder ein neues if die bessere Wahl ist und begründet das

##### 1.1.2 Truthy / Falsy

- **Erinnern** — Nennt Beispiele für Truthy- und Falsy-Werte in Python (0, "", None, …)
- **Verstehen** — Erklärt warum `if x:` und `if x == True:` sich unterschiedlich verhalten können
- **Anwenden** — Nutzt Truthy/Falsy-Werte bewusst in Bedingungen statt explizite Vergleiche
- **Analysieren** — Erkennt Fehler die durch unbeabsichtigtes Truthy/Falsy-Verhalten entstehen

#### 1.2 Schleifen

##### 1.2.1 for-Schleife

- **Erinnern** — Kennt die Syntax einer for-Schleife mit range()
- **Verstehen** — Erklärt was range() mit einem, zwei und drei Parametern jeweils bewirkt
- **Anwenden** — Setzt for-Schleifen zur Iteration über Sequenzen und mit range() ein
- **Analysieren** — Erkennt off-by-one-Fehler und erklärt warum sie entstehen
- **Bewerten** — Entscheidet wann eine for-Schleife einer while-Schleife vorzuziehen ist

##### 1.2.2 while-Schleife

- **Erinnern** — Kennt die Syntax einer while-Schleife
- **Verstehen** — Erklärt warum eine fehlende Abbruchbedingung zu einer Endlosschleife führt
- **Anwenden** — Schreibt eine while-Schleife mit sinnvoller Abbruchbedingung
- **Anwenden** — Setzt eine Endlosschleife mit `while True` als bewusstes Pattern ein
- **Analysieren** — Vergleicht Boolean-Flag vs. break als zwei Wege eine while-Schleife zu beenden
- **Bewerten** — Entscheidet wann eine while-Schleife einer for-Schleife vorzuziehen ist

##### 1.2.3 break / continue / pass

- **Erinnern** — Kennt die Schlüsselwörter break, continue und pass und ihre Grundfunktion
- **Verstehen** — Erklärt den Unterschied zwischen break und continue an einem Beispiel
- **Anwenden** — Setzt break zum vorzeitigen Abbruch einer Schleife ein
- **Anwenden** — Nutzt continue um bestimmte Durchläufe gezielt zu überspringen
- **Analysieren** — Begründet warum break an falscher Stelle zu unerwartetem Verhalten führt
- **Bewerten** — Entscheidet ob break oder eine angepasste Schleifenbedingung die bessere Lösung ist

---

### [N] [Themenblock] — Platzhalter

[Weitere Themenblöcke nach gleichem Muster ergänzen]

#### [N.1] [Unterthema]

##### [N.1.1] [Konzept]

- **Erinnern** — 
- **Verstehen** — 
- **Anwenden** — 
- **Analysieren** — 
- **Bewerten** — 
- **Erschaffen** —