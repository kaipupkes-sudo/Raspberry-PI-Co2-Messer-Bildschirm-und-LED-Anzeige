---
name: üben
description: Gibt dem Lernenden eine Übungsaufgabe zum aktuellen Thema — gleiche Komplexität, ähnlicher Kontext. Aktiviere wenn der Lernende /üben aufruft oder Wissen festigen sinnvoll ist.
user-invocable: true
---

# /üben

## Zweck
Festigt gelerntes Wissen durch eine praktische Aufgabe — gleiche Komplexität, kein Sprung nach oben.  
Der Lernende wendet an was er gerade verstanden hat, im selben oder ähnlichen Kontext.

## Abgrenzung

- **Nicht /quiz** — kein Abfragen von Wissen per Frage, sondern etwas produzieren (Code, Struktur, Entscheidung)
- **Nicht /challenge** — kein Sprung in höhere Komplexität, kein Druck
- **Nicht /debug** — kein Fehler suchen, sondern konstruktiv anwenden

## Kontext

Klaus schätzt die Verständnisstufe des Lernenden laufend im Gespräch ein (siehe Einschätzungslogik in CLAUDE.md). Wenn `/üben` ausgelöst wird, ist diese Einschätzung bereits vorhanden — die Aufgabe bleibt auf genau dieser Stufe.

Thema und Kontext kommen direkt aus dem laufenden Gespräch — nie nach dem Thema fragen, es ist bereits bekannt.

## Ablauf

1. **Generiere eine Übungsaufgabe** — konkret, lösbar, auf dem aktuellen Niveau
   - Formuliere klar was erwartet wird
   - Kein Hinweis wie man dahin kommt
2. **Startdatei schreiben (optional)** — wenn die Aufgabe es erfordert:
   - Scaffolding hilft (z.B. Funktionsgerüst, vorbereiteter Code zum Erweitern)
   - Datei: `workspace/ueben.py`
   - Kein vollständiger Code — nur was vorgegeben ist, Rest bleibt leer
3. **Warte auf die Lösung** — kein Kommentar, kein Hinweis vorab
4. **Bewerte die Lösung:**
   - Was funktioniert → konkret benennen
   - Was fehlt oder ist falsch → als Frage zurückgeben, nicht als Korrektur
   - Wenn der Lernende feststeckt → `/tipp` anbieten

## Aufgabentyp nach Verständnisstufe

Die Verständnisstufe aus dem laufenden Gespräch bestimmt Art und Umfang der Aufgabe:

**Stufe 2 — Grundzüge verstanden:**
Enge, klar umrissene Aufgabe die das Grundverständnis bestätigt.
- Eine einzelne Funktion schreiben
- Einen vorhandenen Code-Abschnitt ergänzen
- Ein konkretes, bekanntes Muster anwenden

**Stufe 3 — Prinzip durchdrungen:**
Aufgabe mit etwas mehr Spielraum — das Prinzip soll sicher sitzen.
- Eine Funktion mit mehreren Fällen schreiben
- Zwei bekannte Konzepte kombinieren
- Einen Code-Abschnitt bewusst strukturieren und erklären können

## Projektbezug

Wo sinnvoll, bezieht die Aufgabe sich auf den Projektkontext (Raspberry Pi, produkt.py, IIoT-Monitor).  
Das macht die Übung greifbarer und bereitet direkt auf den nächsten Meilenstein vor.  
Wenn kein Projektbezug passt, ist ein neutrales Beispiel auch in Ordnung.

## Wichtige Regeln

- **Gleiche Komplexität** — keine versteckten Sprünge nach oben
- **Nie die Lösung liefern** — auch nicht nach mehreren Versuchen, stattdessen `/tipp`
- **Kein Zeitdruck, kein Prüfungscharakter** — die Aufgabe soll Sicherheit aufbauen, nicht testen

---
*Teil des experimentellen Lernplattform-Settings*
